from __future__ import annotations
from run_stage27u_support import *
from run_stage27u_support import _append_outer_row

def run_campaign(a,od,say,campaign_Ns,W,candidates,failures):
    all_outer=[];all_hist=[];all_cont=[];support_rows=[];prev_best=None;barrier_total=0
    for N in campaign_Ns:
        dim=len(odd_indices(N));starts=energy_calibrated_starts(N,a.random_starts,q_low=QLOW,q_high=QHIGH,seed=20260903+N)
        if prev_best is not None:
            y=np.zeros(dim);y[:min(dim,len(prev_best))]=prev_best[:min(dim,len(prev_best))];starts.insert(1,y)
        for c in candidates:
            try:
                y=candidate_high_odd(c,N,QHIGH)
                if np.dot(y,y)<=5.0*(1+1e-12):starts.append(y)
            except Exception:pass
    
        level1,calls,barriers=multistart_search(N,W,starts,q_low=QLOW,q_high=QHIGH,A=5,ridge=RIDGE,dps=180,maxiter=a.outer_maxiter)
        barrier_total+=barriers
        for r in level1:
            _append_outer_row(all_outer,N,'LEVEL1',r)
            if r.get('eval_status')=='UNEXPECTED_START_EXCEPTION':
                failures.append(dict(N=N,phase='level1_start',start_id=r.get('start_id'),error=r.get('error',r.get('message',''))))
        valid_level1=[r for r in level1 if r.get('scientific_valid') and 'y' in r and np.isfinite(r.get('margin',math.nan))]
        if not valid_level1:
            raise RuntimeError(f'NO_VALID_LEVEL1_START N={N}')
        finalists=valid_level1[:max(1,a.level2_finalists)]
    
        pooled=list(W);validated=[]
        for rank,r in enumerate(finalists):
            try:
                cc=complete_low_lift_high(r['y'],N,QLOW,QHIGH)
                vr=validate_fixed_candidate(QHIGH,N,cc.u_high,pooled,ridge=RIDGE,dps=220,max_outer=a.continuum_max_outer)
                pooled=dedupe(pooled+vr['witnesses']);tot=cc.prefix_energy_high+max(0.0,float(vr['m2']))
                validated.append((tot-5,r['y'],cc,vr))
                all_cont.append(dict(N=N,rank=rank,status=vr['status'],margin=tot-5,total_lb=tot,
                                     prefix_energy=cc.prefix_energy_high,tail_lb=vr['m2'],witness_count=len(vr['witnesses']),
                                     y_json=y_json(r['y'])))
                for h in vr['history']:all_hist.append(dict(N=N,rank=rank,**h))
            except Exception as exc:
                failures.append(dict(N=N,phase='continuum',rank=rank,error=repr(exc),traceback=traceback.format_exc(limit=8)))
    
        refined=[];obj=CoherentObjective(N,pooled,q_low=QLOW,q_high=QHIGH,A=5,ridge=RIDGE,dps=200)
        for rank,r in enumerate(finalists[:4]):
            try:
                rr=local_search(obj,r['y'],maxiter=max(80,a.outer_maxiter//2));ev=rr['eval'];barrier_total+=obj.barrier_evaluations;obj.barrier_evaluations=0
                row=dict(start_id=rank,margin=(ev.value if ev.scientific_valid else math.nan),
                         total_lb=(ev.total_lb if ev.scientific_valid else math.nan),prefix_energy=(ev.prefix_energy if ev.scientific_valid else math.nan),
                         tail_lb=(ev.tail_lb if ev.scientific_valid else math.nan),scientific_valid=ev.scientific_valid,eval_status=ev.status,
                         success=rr['success'],message=rr['message'],grad_fd_error=rr.get('grad_fd_error'),
                         grad_check_status=rr.get('grad_check_status'),grad_check_count=rr.get('grad_check_count'),y=rr['y'])
                _append_outer_row(all_outer,N,'LEVEL2_REOPT',row,rank)
                if ev.scientific_valid and np.isfinite(ev.value):refined.append((ev.value,rr['y'],ev))
            except Exception as exc:
                failures.append(dict(N=N,phase='reopt',rank=rank,error=repr(exc),traceback=traceback.format_exc(limit=8)))
    
        pool_candidates=[]
        for z in validated:
            if np.isfinite(z[0]):pool_candidates.append((z[0],z[1]))
        for z in refined:
            if np.isfinite(z[0]):pool_candidates.append((z[0],z[1]))
        for r in finalists:
            if np.isfinite(r['margin']):pool_candidates.append((r['margin'],r['y']))
        if not pool_candidates:raise RuntimeError(f'NO_FINITE_CANDIDATE N={N}')
        pool_candidates.sort(key=lambda x:x[0]);_,best_y=pool_candidates[0];best_y=np.asarray(best_y,float)
        ccfinal=complete_low_lift_high(best_y,N,QLOW,QHIGH)
        try:
            vfinal=validate_fixed_candidate(QHIGH,N,ccfinal.u_high,pooled,ridge=RIDGE,dps=220,max_outer=a.continuum_max_outer)
            pooled=dedupe(pooled+vfinal['witnesses']);final_margin=ccfinal.prefix_energy_high+max(0.0,float(vfinal['m2']))-5.0
            final_status=vfinal['status']
            all_cont.append(dict(N=N,rank='FINAL',status=final_status,margin=final_margin,total_lb=final_margin+5.0,
                                 prefix_energy=ccfinal.prefix_energy_high,tail_lb=vfinal['m2'],witness_count=len(pooled),y_json=y_json(best_y)))
            for h in vfinal['history']:all_hist.append(dict(N=N,rank='FINAL',**h))
        except Exception as exc:
            failures.append(dict(N=N,phase='final_continuum',error=repr(exc),traceback=traceback.format_exc(limit=8)))
            final_margin=math.nan;final_status='FINAL_CONTINUUM_FAILED'
    
        if not np.isfinite(final_margin):
            raise RuntimeError(f'NONFINITE_FINAL_MARGIN N={N} status={final_status}')
        prev_best=best_y
        all_outer.append(dict(N=N,phase='FINAL_VALIDATED',start_id=-1,margin=final_margin,total_lb=final_margin+5.0,
                              prefix_energy=ccfinal.prefix_energy_high,tail_lb=(final_margin+5.0-ccfinal.prefix_energy_high),
                              scientific_valid=True,eval_status='FINAL',success=True,message=final_status,
                              grad_fd_error=math.nan,grad_check_status='NOT_APPLICABLE',grad_check_count=0,y_json=y_json(best_y)))
        np.savez_compressed(od/'candidate_artifacts'/f'N{N}_best.npz',y_high=prev_best,witnesses=np.asarray(pooled,float),q_low=QLOW,q_high=QHIGH,N=N,
                            reported_margin=final_margin,continuum_status=np.asarray(final_status))
        for j,w in enumerate(pooled):support_rows.append(dict(N=N,index=j,lambda_=w[0],s=w[1]))
        say('STAGE27U_N',N,'BEST_MARGIN',final_margin,'STATUS',final_status,'W',len(pooled),'STARTS',len(starts),'CALLS',calls,'BARRIERS',barriers)
    return all_outer,all_hist,all_cont,support_rows,barrier_total
