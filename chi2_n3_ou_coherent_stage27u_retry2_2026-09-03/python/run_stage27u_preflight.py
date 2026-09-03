from __future__ import annotations
from run_stage27u_support import *
from run_stage27u_support import _append_outer_row

def run_preflight(a,od,say,campaign_Ns):
    lift=regression_rows();pd.DataFrame(lift).to_csv(od/'stage27u_lift_validation.csv',index=False)
    ident=kernel_identity_rows();pd.DataFrame(ident).to_csv(od/'stage27u_kernel_identity.csv',index=False)
    pd.DataFrame(ident).to_csv(od/'stage27u_coherence_identity.csv',index=False)
    if max(r['max_relative_error'] for r in lift)>1e-7:
        raise RuntimeError('COHERENCE_IMPLEMENTATION_ERROR: direct/lift regression too large')
    if max(max(r['feature_error_160'],r['feature_error_240'],r['kernel_error']) for r in ident)>1e-20:
        raise RuntimeError('COHERENCE_IMPLEMENTATION_ERROR: feature/kernel identity failed')
    
    W,wsources=load_witnesses(a.stage27r_dir,a.stage27s_dir);say('WITNESS_POOL',len(W),wsources)
    
    grad_rows=gradient_audit_rows(W,campaign_Ns);gdf=pd.DataFrame(grad_rows);gdf.to_csv(od/'stage27u_gradient_audit.csv',index=False)
    stable=gdf[gdf.status.astype(str)=='CHECKED_STABLE_ACTIVE_SET']
    perN={N:int(np.sum(stable.N.astype(int)==N)) for N in campaign_Ns}
    gerr=pd.to_numeric(stable.grad_fd_error,errors='coerce').dropna()
    max_gerr=float(gerr.max()) if len(gerr) else math.inf
    say('GRADIENT_AUDIT','stable_by_N',perN,'max_error',max_gerr)
    if any(perN[N]<2 for N in campaign_Ns) or not np.isfinite(max_gerr) or max_gerr>2e-3:
        raise RuntimeError(f'GRADIENT_AUDIT_FAILED stable_by_N={perN} max_error={max_gerr}')
    
    cand_roots=list(a.stage15_dir)+list(a.stage16_dir)
    candidates,skipped=discover_candidates(cand_roots);say('CANDIDATES',len(candidates),'SKIPPED_ROOTS',len(skipped))
    ca=[]
    if not a.skip_existing_candidate_audit: existing_candidate_audit(candidates,W,ca)
    pd.DataFrame(ca).to_csv(od/'stage27u_existing_candidate_audit.csv',index=False)
    return lift,ident,W,candidates,perN,max_gerr
