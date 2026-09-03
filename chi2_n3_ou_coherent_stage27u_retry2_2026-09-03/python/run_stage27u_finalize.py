from __future__ import annotations
from run_stage27u_support import *
from run_stage27u_support import _append_outer_row

def finalize_run(a,od,say,log,campaign_Ns,lift,ident,W,candidates,perN,max_gerr,barrier_total,failures,all_outer,all_hist,all_cont,support_rows):
    pd.DataFrame(all_outer).to_csv(od/'stage27u_outer_search.csv',index=False)
    pd.DataFrame(all_hist).to_csv(od/'stage27u_outer_history.csv',index=False)
    pd.DataFrame(all_cont).to_csv(od/'stage27u_continuum_validation.csv',index=False)
    pd.DataFrame(support_rows).to_csv(od/'stage27u_active_support.csv',index=False)
    pd.DataFrame(failures).to_csv(od/'stage27u_failures.csv',index=False)
    
    odf=pd.DataFrame(all_outer);frows=odf[odf.phase.astype(str)=='FINAL_VALIDATED'] if len(odf) else pd.DataFrame()
    best_by_N={int(r.N):float(r.margin) for _,r in frows.iterrows()} if len(frows) else {}
    margins=list(best_by_N.values());cdf=pd.DataFrame(all_cont)
    stationary_negative=False
    if len(cdf):
        fin=cdf[cdf['rank'].astype(str)=='FINAL']
        stationary_negative=bool(np.any((fin.status.astype(str)=='COHERENT_CONTINUUM_STATIONARY') & (fin.margin.astype(float)<-0.1))) if len(fin) else False
    if failures:
        status='COHERENT_OUTER_MINIMAX_UNRESOLVED_NUMERIC_FAILURES'
    elif margins and len(margins)==len(campaign_Ns) and min(margins)>=0.1:
        status='COHERENT_HIGHQ_OBSTRUCTION_STRONG_NUMERIC_EVIDENCE'
    elif stationary_negative:
        status='COHERENT_SURVIVOR_FOUND'
    else:
        status='COHERENT_OUTER_MINIMAX_UNRESOLVED'
    summary=dict(stage='Stage27U retry2 OU-coherent lifted minimax',q_low=QLOW,q_high=QHIGH,ridge=RIDGE,
                 lift_validation_max_error=max(r['max_relative_error'] for r in lift),
                 kernel_identity_max_error=max(max(r['feature_error_160'],r['feature_error_240'],r['kernel_error']) for r in ident),
                 gradient_audit_max_error=max_gerr,gradient_stable_checks_by_N=perN,
                 witness_seed_count=len(W),loaded_existing_candidates=len(candidates),best_margin_by_N=best_by_N,
                 barrier_evaluations=int(barrier_total),failures=len(failures),status=status,
                 note='Retry2: overflow regions are algorithmic barriers only; gradient audit is interior/active-set-stable. No Stage28 or theorem claim.')
    (od/'stage27u_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    say('STAGE27U_RETRY2_COMPLETED',json.dumps(summary,sort_keys=True));log.close()
    return summary
