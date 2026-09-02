from __future__ import annotations
from dataclasses import dataclass
import json,re
from pathlib import Path
import numpy as np
import pandas as pd


@dataclass
class Candidate:
    source: str
    name: str
    q: float
    N: int
    u: np.ndarray
    semantics: str


def _infer_qn(name):
    s=str(name)
    mq=re.search(r'q(?:=|_)?([0-9]+(?:p|\.)?[0-9]*)',s,re.I)
    mn=re.search(r'N(?:=|_)?(\d+)',s)
    q=None;N=None
    if mq:
        try:q=float(mq.group(1).replace('p','.'))
        except Exception:pass
    if mn:
        try:N=int(mn.group(1))
        except Exception:pass
    return q,N


def _array_to_u(arr,N=None):
    a=np.asarray(arr,float).reshape(-1)
    if N is None:N=len(a)-1
    if len(a)>=N+1:return a[:N+1].copy()
    return None


def _from_npz(path):
    out=[]
    try:z=np.load(path,allow_pickle=False)
    except Exception:return out
    q=float(z['q']) if 'q' in z and np.asarray(z['q']).size==1 else None
    N=int(z['N']) if 'N' in z and np.asarray(z['N']).size==1 else None
    iq,iN=_infer_qn(path.name);q=q if q is not None else iq;N=N if N is not None else iN
    for key in ('u','odd_u','normalized_u','coefficients_u'):
        if key in z:
            u=_array_to_u(z[key],N)
            if u is not None and q is not None:
                out.append(Candidate(str(path),path.stem,float(q),len(u)-1,u,f'npz:{key}'))
                break
    return out


def _from_json(path):
    try:x=json.loads(path.read_text(encoding='utf-8'))
    except Exception:return []
    rows=x if isinstance(x,list) else [x]
    out=[]
    for j,r in enumerate(rows):
        if not isinstance(r,dict):continue
        q=r.get('q');N=r.get('N')
        iq,iN=_infer_qn(path.name);q=iq if q is None else q;N=iN if N is None else N
        for key in ('u','odd_u','normalized_u','coefficients_u'):
            if key in r and q is not None:
                u=_array_to_u(r[key],int(N) if N is not None else None)
                if u is not None:out.append(Candidate(str(path),f'{path.stem}:{j}',float(q),len(u)-1,u,f'json:{key}'))
                break
    return out


def _from_csv(path):
    try:df=pd.read_csv(path)
    except Exception:return []
    need={'q','n','u'}
    if not need.issubset(set(map(str,df.columns))):return []
    out=[]
    groups=['candidate'] if 'candidate' in df.columns else []
    gb=df.groupby(groups) if groups else [(path.stem,df)]
    for name,g in gb:
        qvals=pd.to_numeric(g.q,errors='coerce').dropna().unique()
        if len(qvals)!=1:continue
        ns=pd.to_numeric(g.n,errors='coerce').astype('Int64')
        if ns.isna().any():continue
        N=int(ns.max());u=np.zeros(N+1,float)
        ok=True
        for _,r in g.iterrows():
            try:u[int(r['n'])]=float(r['u'])
            except Exception:ok=False;break
        if ok:out.append(Candidate(str(path),str(name),float(qvals[0]),N,u,'csv:q,n,u'))
    return out


def discover_candidates(roots):
    out=[]; skipped=[]
    for root in roots or []:
        if not root:continue
        p=Path(root)
        if not p.exists():
            skipped.append(dict(path=str(p),reason='MISSING_ROOT'));continue
        for f in p.rglob('*'):
            if not f.is_file():continue
            got=[]
            if f.suffix.lower()=='.npz':got=_from_npz(f)
            elif f.suffix.lower()=='.json':got=_from_json(f)
            elif f.suffix.lower()=='.csv':got=_from_csv(f)
            if got:out.extend(got)
    uniq=[];seen=set()
    for c in out:
        key=(round(c.q,12),c.N,tuple(np.round(c.u[3:min(len(c.u),25)],12)))
        if key not in seen:seen.add(key);uniq.append(c)
    return uniq,skipped


def candidate_high_odd(c:Candidate,N,q_high=.10,d=3):
    if c.q<=0:raise ValueError('candidate q must be positive')
    idx=list(range(d+2,N+1,2));y=[]
    for n in idx:
        val=float(c.u[n]) if n < len(c.u) else 0.0
        val*= (q_high/c.q)**((n-d)/2.0)
        y.append(val)
    return np.asarray(y,float)
