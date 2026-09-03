#!/usr/bin/env python3
from __future__ import annotations
from run_stage27u_support import argparse,Path
from run_stage27u_preflight import run_preflight
from run_stage27u_campaign import run_campaign
from run_stage27u_finalize import finalize_run

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stage27r-dir',required=True);ap.add_argument('--stage27s-dir',required=True)
    ap.add_argument('--stage15-dir',action='append',default=[]);ap.add_argument('--stage16-dir',action='append',default=[])
    ap.add_argument('--outdir',default='_stage27u_retry2_results_20260903')
    ap.add_argument('--random-starts',type=int,default=32);ap.add_argument('--level2-finalists',type=int,default=6)
    ap.add_argument('--outer-maxiter',type=int,default=180);ap.add_argument('--continuum-max-outer',type=int,default=6)
    ap.add_argument('--Ns',default='32,48,64,80');ap.add_argument('--skip-existing-candidate-audit',action='store_true')
    a=ap.parse_args();od=Path(a.outdir);od.mkdir(parents=True,exist_ok=True);(od/'candidate_artifacts').mkdir(exist_ok=True)
    log=(od/'stage27u_run.log').open('w',encoding='utf-8',buffering=1)
    def say(*x):
        z=' '.join(map(str,x));print(z,flush=True);print(z,file=log,flush=True)
    failures=[]
    campaign_Ns=[int(x) for x in str(a.Ns).split(',') if str(x).strip()]
    lift,ident,W,candidates,perN,max_gerr=run_preflight(a,od,say,campaign_Ns)
    all_outer,all_hist,all_cont,support_rows,barrier_total=run_campaign(a,od,say,campaign_Ns,W,candidates,failures)
    finalize_run(a,od,say,log,campaign_Ns,lift,ident,W,candidates,perN,max_gerr,barrier_total,failures,all_outer,all_hist,all_cont,support_rows)

if __name__=='__main__':main()
