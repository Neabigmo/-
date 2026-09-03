#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np
import pandas as pd
from outer_minimax import CoherentObjective


def need(p):
    if not p.exists():raise AssertionError(f'missing {p.name}')
    return p


def assert_no_inf(df,name):
    for c in df.columns:
        z=pd.to_numeric(df[c],errors='coerce')
        vals=z.dropna().to_numpy(dtype=float)
        if len(vals) and np.isinf(vals).any():
            raise AssertionError(f'{name}:{c} contains +/-Inf')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--result-dir',required=True);a=ap.parse_args();r=Path(a.result_dir)
    summary=json.loads(need(r/'stage27u_summary.json').read_text(encoding='utf-8'))
    lift=pd.read_csv(need(r/'stage27u_lift_validation.csv'));ker=pd.read_csv(need(r/'stage27u_kernel_identity.csv'))
    grad=pd.read_csv(need(r/'stage27u_gradient_audit.csv'));out=pd.read_csv(need(r/'stage27u_outer_search.csv'))
    cont=pd.read_csv(need(r/'stage27u_continuum_validation.csv'));sup=pd.read_csv(need(r/'stage27u_active_support.csv'))
    fail=pd.read_csv(need(r/'stage27u_failures.csv')) if (r/'stage27u_failures.csv').stat().st_size>1 else pd.DataFrame()

    assert len(lift)>=16 and np.isfinite(lift.max_relative_error.astype(float)).all()
    assert float(lift.max_relative_error.max())<=1e-7
    for c in ('feature_error_160','feature_error_240','kernel_error'):
        assert np.isfinite(ker[c].astype(float)).all() and float(ker[c].max())<=1e-20

    stable=grad[grad.status.astype(str)=='CHECKED_STABLE_ACTIVE_SET']
    for N in (32,48,64,80):
        g=stable[stable.N.astype(int)==N]
        assert len(g)>=2,(N,'too few stable gradient checks',len(g))
        e=pd.to_numeric(g.grad_fd_error,errors='coerce').dropna().astype(float)
        assert len(e)>=2 and np.isfinite(e).all() and float(e.max())<2e-3,(N,float(e.max()) if len(e) else None)
    assert float(summary['gradient_audit_max_error'])<2e-3

    assert set(out.N.astype(int))=={32,48,64,80}
    assert set(out.phase.astype(str)).issuperset({'LEVEL1','FINAL_VALIDATED'})
    assert_no_inf(out,'outer_search');assert_no_inf(cont,'continuum');assert_no_inf(grad,'gradient_audit')
    if len(fail):assert_no_inf(fail,'failures')

    sci=out[out.scientific_valid.astype(str).str.lower().isin(['true','1'])] if 'scientific_valid' in out.columns else out
    for c in ('margin','total_lb','prefix_energy','tail_lb'):
        z=pd.to_numeric(sci[c],errors='coerce')
        assert np.isfinite(z.dropna().astype(float)).all(),c
    if 'eval_status' in out.columns:
        assert not np.any(out.eval_status.astype(str)=='UNEXPECTED_START_EXCEPTION')

    # Retry2 treats overflow regions as algorithmic barriers, not failures or lower bounds.
    if 'eval_status' in out.columns:
        bar=out[out.eval_status.astype(str)=='PREFIX_OVERFLOW_BARRIER']
        if len(bar) and 'scientific_valid' in bar.columns:
            assert not bar.scientific_valid.astype(str).str.lower().isin(['true','1']).any()

    for N in (32,48,64,80):
        p=r/'candidate_artifacts'/f'N{N}_best.npz';assert p.exists()
        z=np.load(p,allow_pickle=False)
        assert int(z['N'])==N and abs(float(z['q_high'])-.10)<1e-15 and abs(float(z['q_low'])-.05)<1e-15
        y=np.asarray(z['y_high'],float);W=np.asarray(z['witnesses'],float)
        assert np.isfinite(y).all() and float(y@y)<=5.000001
        obj=CoherentObjective(N,[tuple(map(float,w)) for w in W],q_low=.05,q_high=.10,A=5,ridge=1e-11,dps=180)
        ev=obj.evaluate(y);rep=float(z['reported_margin'])
        assert ev.scientific_valid and np.isfinite(ev.value) and np.isfinite(rep)
        assert abs(ev.value-rep) <= 2e-5*(1+abs(rep)+abs(ev.value)),(N,ev.value,rep)
        assert obj.prepared['joint']['raw_corr_min_eig']>=-5e-10
        assert abs(obj.prepared['joint']['ridge']-1e-11)<1e-25
        assert abs(float(summary['best_margin_by_N'][str(N)])-rep)<=1e-10*(1+abs(rep))

    assert len(cont)>0
    assert (cont.witness_count.astype(float)>=1).all()
    fin=cont[cont['rank'].astype(str)=='FINAL'];assert set(fin.N.astype(int))=={32,48,64,80}
    assert np.isfinite(fin.margin.astype(float)).all()
    assert (sup['lambda_'].astype(float)>=0).all() and (sup['lambda_'].astype(float)<1).all()

    allowed=('COHERENT_HIGHQ_OBSTRUCTION_STRONG_NUMERIC_EVIDENCE','COHERENT_SURVIVOR_FOUND','COHERENT_OUTER_MINIMAX_UNRESOLVED')
    assert summary['status'] in allowed,summary['status']
    assert int(summary['failures'])==len(fail)
    assert len(fail)==0,f'unexpected numeric failures remain: {len(fail)}'
    print('STAGE27U_RETRY2_NUMERIC_AUDIT_OK')

if __name__=='__main__':main()
