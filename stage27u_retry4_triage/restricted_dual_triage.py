from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
PKG = REPO / 'chi2_n3_ou_coherent_stage27u_retry2_2026-09-03'
PKG_PY = PKG / 'python'
sys.path.insert(0, str(PKG_PY))

from coherence_lift import complete_low_lift_high
from joint_tail_core import scaled_hermites_mp, full_cross_kernel_mp

QLOW = 0.05
QHIGH = 0.10
RIDGE = 1e-11
A = 5.0


def _feature_data(q, N, u, w, ridge=RIDGE, dps=260):
    old = mp.mp.dps; mp.mp.dps = int(dps)
    try:
        qmp = mp.mpf(str(float(q)))
        lam = mp.mpf(str(float(w[0]))); s = mp.mpf(str(float(w[1])))
        eps = mp.mpf(str(float(q) ** 1.5))
        g = scaled_hermites_mp(qmp, lam, s, int(N))
        tail2 = full_cross_kernel_mp(qmp, lam, s, lam, s) - mp.fsum(g[n]*g[n] for n in range(int(N)+1))
        if not mp.isfinite(tail2) or tail2 <= mp.mpf('1e-90'):
            return None
        d = mp.sqrt(tail2)
        uu = np.asarray(u, float)
        raw = mp.mpf(1) + eps * mp.fsum(mp.mpf(str(float(uu[n]))) * g[n] for n in range(3, int(N)+1))
        c = raw / d
        cjj = mp.mpf(1) + mp.mpf(str(float(ridge)))
        neg = min(c, mp.mpf(0))
        single = (neg*neg)/(cjj*eps*eps)
        return dict(w=(float(w[0]),float(w[1])), g=g, tail2=tail2, d=d, c=c, cjj=cjj, single=single, eps=eps)
    finally:
        mp.mp.dps = old


def _pair_lb(q, N, fi, fj, dps=260):
    old = mp.mp.dps; mp.mp.dps = int(dps)
    try:
        qmp = mp.mpf(str(float(q)))
        wi, wj = fi['w'], fj['w']
        cross = full_cross_kernel_mp(qmp, wi[0], wi[1], wj[0], wj[1]) - mp.fsum(fi['g'][n] * fj['g'][n] for n in range(int(N)+1))
        cij = cross / (fi['d'] * fj['d'])
        a = fi['cjj']; d = fj['cjj']; b = cij
        ci = fi['c']; cj = fj['c']; eps = fi['eps']
        best_f = mp.mpf(0); mode = 'zero'; alpha = (mp.mpf(0), mp.mpf(0))
        if ci < 0:
            ai = -ci/a; f = -ci*ci/a
            if f < best_f: best_f=f; mode='axis_i'; alpha=(ai,mp.mpf(0))
        if cj < 0:
            aj = -cj/d; f = -cj*cj/d
            if f < best_f: best_f=f; mode='axis_j'; alpha=(mp.mpf(0),aj)
        det = a*d-b*b
        if det > mp.mpf('1e-80'):
            ai = (-d*ci + b*cj)/det
            aj = ( b*ci - a*cj)/det
            if ai > 0 and aj > 0:
                f = a*ai*ai + 2*b*ai*aj + d*aj*aj + 2*ci*ai + 2*cj*aj
                if f < best_f: best_f=f; mode='interior'; alpha=(ai,aj)
        lb = -best_f/(eps*eps)
        return dict(lb=float(lb), mode=mode, alpha_i=float(alpha[0]), alpha_j=float(alpha[1]), corr=float(cij), det=float(det))
    finally:
        mp.mp.dps = old


def restricted_bounds(N, y, witnesses, dps=260, topk=12):
    cc = complete_low_lift_high(np.asarray(y,float), int(N), QLOW, QHIGH)
    E = float(cc.prefix_energy_high)
    feats=[]
    for j,w in enumerate(np.asarray(witnesses,float)):
        try:
            f=_feature_data(QHIGH,N,cc.u_high,tuple(map(float,w)),dps=dps)
        except Exception:
            f=None
        if f is not None:
            f['index']=j; feats.append(f)
    if not feats:
        return dict(prefix_energy=E,prefix_margin=E-A,single_lb=0.0,single_margin=E-A, single_index=-1,pair_lb=0.0,pair_margin=E-A,pair_i=-1,pair_j=-1,pair_mode='none',finite_witnesses=0)
    feats.sort(key=lambda f: float(f['single']), reverse=True)
    best1=feats[0]; single=float(best1['single'])
    top=feats[:min(int(topk),len(feats))]
    best_pair=dict(lb=single,mode='single',i=best1['index'],j=-1,corr=0.0,det=math.nan)
    for a in range(len(top)):
        for b in range(a+1,len(top)):
            try:
                z=_pair_lb(QHIGH,N,top[a],top[b],dps=dps)
            except Exception:
                continue
            if z['lb'] > best_pair['lb']:
                best_pair=dict(z,i=top[a]['index'],j=top[b]['index'])
    return dict(prefix_energy=E,prefix_margin=E-A, single_lb=single,single_margin=E+single-A,single_index=int(best1['index']), single_lambda=best1['w'][0],single_s=best1['w'][1], pair_lb=float(best_pair['lb']),pair_margin=E+float(best_pair['lb'])-A, pair_i=int(best_pair['i']),pair_j=int(best_pair['j']),pair_mode=str(best_pair['mode']), pair_corr=float(best_pair.get('corr',0.0)),pair_det=float(best_pair.get('det',math.nan)), finite_witnesses=len(feats))


def summarize_failures(result_dir: Path):
    p=result_dir/'stage27u_failures.csv'
    if not p.exists() or p.stat().st_size<=1:
        return []
    df=pd.read_csv(p); rows=[]
    if len(df):
        for (N,phase),g in df.groupby([pd.to_numeric(df.get('N'),errors='coerce'),df.get('phase').astype(str)],dropna=False):
            rows.append(dict(N=(None if pd.isna(N) else int(N)),phase=str(phase),count=int(len(g))))
    return rows


def run(result_dir: Path, outdir: Path, dps=260, topk=12):
    rows=[]
    for N in (32,48,64,80):
        p=result_dir/'candidate_artifacts'/f'N{N}_best.npz'
        if not p.exists():
            rows.append(dict(N=N,status='MISSING_ARTIFACT')); continue
        z=np.load(p,allow_pickle=False)
        y=np.asarray(z['y_high'],float); W=np.asarray(z['witnesses'],float)
        r=restricted_bounds(N,y,W,dps=dps,topk=topk)
        rep=float(z['reported_margin']) if 'reported_margin' in z else math.nan
        cstatus=str(z['continuum_status']) if 'continuum_status' in z else ''
        if r['prefix_margin']>=0.1: tri='PREFIX_POINTWISE_POSITIVE'
        elif r['single_margin']>=0.1: tri='SINGLE_WITNESS_POINTWISE_POSITIVE'
        elif r['pair_margin']>=0.1: tri='PAIR_WITNESS_POINTWISE_POSITIVE'
        else: tri='POINTWISE_NOT_POSITIVE_BY_RESTRICTED_DUAL'
        rows.append(dict(N=N,status=tri,reported_margin=rep,continuum_status=cstatus,witness_count=len(W),**r))
    outdir.mkdir(parents=True,exist_ok=True)
    df=pd.DataFrame(rows); df.to_csv(outdir/'stage27u_retry4_triage.csv',index=False)
    fail=summarize_failures(result_dir)
    high={int(r['N']):r['status'] for r in rows if r.get('N') in (48,64,80)}
    high_all=all(high.get(N,'').endswith('POINTWISE_POSITIVE') for N in (48,64,80))
    n32=next((r for r in rows if r.get('N')==32),{})
    if high_all and not str(n32.get('status','')).endswith('POINTWISE_POSITIVE'):
        decision='HIGH_N_FINALS_POINTWISE_POSITIVE_FOCUS_N32_BOUNDARY'
    elif high_all:
        decision='ALL_FINALS_POINTWISE_POSITIVE_BUT_GLOBAL_MINIMAX_NOT_CERTIFIED'
    else:
        decision='NNQP_REPAIR_STILL_REQUIRED_FOR_HIGH_N_TRIAGE'
    summary=dict(stage='Stage27U retry4 read-only restricted-dual triage',dps=int(dps),topk=int(topk), result_dir=str(result_dir),failure_breakdown=fail,decision=decision, note='Pointwise replay of saved final candidates only; not a global outer-minimax certificate and not a theorem.')
    (outdir/'stage27u_retry4_triage_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print('STAGE27U_RETRY4_TRIAGE_COMPLETED',json.dumps(summary,sort_keys=True))
    return df,summary


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--retry3-result-dir',required=True); ap.add_argument('--outdir',default='_stage27u_retry4_triage_20260903'); ap.add_argument('--dps',type=int,default=260); ap.add_argument('--topk',type=int,default=12)
    a=ap.parse_args(); run(Path(a.retry3_result_dir),Path(a.outdir),dps=a.dps,topk=a.topk)

if __name__=='__main__': main()
