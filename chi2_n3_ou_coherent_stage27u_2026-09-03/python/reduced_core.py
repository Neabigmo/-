#!/usr/bin/env python3
from __future__ import annotations
import math
import numpy as np
from scipy.linalg import solve_triangular

LD=np.longdouble

class FockSystem:
    def __init__(self,N:int,scale:float=0.30,pad:int=8):
        self.N=int(N); self.scale=float(scale)
        deg_t=N//3+3
        self.M=(deg_t+2)//2+pad
        j=np.arange(1,self.M+1,dtype=float)
        phi=(2*j-1)*math.pi/(2*self.M)
        theta=phi/3.0
        amp=LD(math.sqrt(2/3))
        a=np.empty((3,self.M),dtype=LD)
        for k in range(3):
            a[k]=amp*np.cos(theta+2*math.pi*k/3)
        self.a=a
        pw=np.ones((3,N+1,self.M),dtype=LD)
        for n in range(1,N+1):
            pw[:,n]=pw[:,n-1]*a
        self.pw=pw
        self.mean_power_sum=np.mean(np.sum(pw,axis=0),axis=1,dtype=LD)
        self.sqrtfac=np.array([math.exp(.5*math.lgamma(n+1)) for n in range(N+1)],dtype=LD)

    def scaled_r_from_bodd(self,bodd):
        r=np.zeros(self.N+1,dtype=LD); r[0]=1
        ls=math.log(self.scale)
        for n,v in bodd.items():
            if n<=self.N and v!=0:
                r[n]=LD(v)*LD(math.exp(n*ls-.5*math.lgamma(n+1)))
        return r

    def complete(self,r):
        N=self.N; M=self.M; pw=self.pw
        r=np.array(r,dtype=LD,copy=True); r[0]=1
        f=[np.zeros((N+1,M),dtype=LD) for _ in range(3)]
        for q in range(3): f[q][0]=1
        pair=np.zeros((N+1,M),dtype=LD); pair[0]=1
        maxres=0.
        for n in range(1,N+1):
            if n<=2: r[n]=0
            if n>1:
                pair_lower=np.sum(f[0][1:n]*f[1][n-1:0:-1],axis=0,dtype=LD)
                rest=pair_lower+np.sum(pair[1:n]*f[2][n-1:0:-1],axis=0,dtype=LD)
            else:
                pair_lower=np.zeros(M,dtype=LD); rest=np.zeros(M,dtype=LD)
            if n%2==0:
                r[n]=-np.mean(rest,dtype=LD)/self.mean_power_sum[n]
            for q in range(3):
                f[q][n]=r[n]*pw[q,n]
            pair[n]=pair_lower+f[0][n]+f[1][n]
            coeff=rest+r[n]*np.sum(pw[:,n],axis=0)
            maxres=max(maxres,abs(float(np.mean(coeff,dtype=LD))))
            if not np.isfinite(r[n]):
                raise FloatingPointError(f"nonfinite r[{n}]")
        return r,maxres

    def b_from_scaled_r(self,r):
        b=np.zeros(len(r),float)
        ls=math.log(self.scale)
        for n,x in enumerate(r):
            if x==0: continue
            la=float(np.log(abs(LD(x))))+.5*math.lgamma(n+1)-n*ls
            if la>700:
                b[n]=math.copysign(math.inf,float(x))
            else:
                b[n]=math.copysign(math.exp(la),float(x))
        return b

    def normalized_constraint_jacobian(self,b):
        N=self.N; M=self.M
        s=np.zeros(N+1,dtype=LD)
        for n in range(N+1):
            if b[n]!=0:
                s[n]=LD(b[n])/self.sqrtfac[n]
        f=np.zeros((3,N+1,M),dtype=LD)
        for q in range(3):
            for n in range(N+1):
                if s[n]!=0:
                    f[q,n]=s[n]*self.pw[q,n]
        pairs={}
        for q1,q2 in [(0,1),(0,2),(1,2)]:
            arr=np.zeros((N+1,M),dtype=LD)
            for m in range(N+1):
                acc=np.zeros(M,dtype=LD)
                for i in range(m+1):
                    acc += f[q1,i]*f[q2,m-i]
                arr[m]=acc
            pairs[(q1,q2)]=arr
        evens=list(range(4,N+1,2)); cols=list(range(3,N+1))
        J=np.zeros((len(evens),len(cols)),float)
        for ii,m in enumerate(evens):
            gm=self.mean_power_sum[m]
            for jj,l in enumerate(cols):
                if l>m: continue
                k=m-l
                term=(self.pw[0,l]*pairs[(1,2)][k]
                      +self.pw[1,l]*pairs[(0,2)][k]
                      +self.pw[2,l]*pairs[(0,1)][k])
                val=(self.sqrtfac[m]/self.sqrtfac[l]*np.mean(term,dtype=LD)/gm)
                J[ii,jj]=float(val)
        return evens,cols,J

class ReducedProblem:
    def __init__(self,N,d,kappa,scale=.30):
        self.N=N; self.d=d; self.kappa=float(kappa)
        self.q=self.kappa/N
        self.eps=self.q**(d/2)
        self.sys=FockSystem(N,scale=scale)
        self.free_odds=list(range(d+2,N+1,2))
        self.evens=list(range(4,N+1,2))
        self.residual_indices=[n for n in range(3,N+1) if n!=d]

    def state(self,x,need_jac=True):
        bodd={self.d:self.eps}
        for n,v in zip(self.free_odds,x):
            bodd[n]=self.eps*float(v)
        r,maxres=self.sys.complete(self.sys.scaled_r_from_bodd(bodd))
        b=self.sys.b_from_scaled_r(r)
        if not np.all(np.isfinite(b[:self.N+1])):
            raise FloatingPointError("nonfinite b")
        u=b/self.eps
        residual=np.array([u[n] for n in self.residual_indices],float)
        if not need_jac:
            return residual,None,b,u,maxres,None
        evens,cols,J=self.sys.normalized_constraint_jacobian(b)
        cidx={n:i for i,n in enumerate(cols)}
        ecols=[cidx[n] for n in evens]
        ocols=[cidx[n] for n in self.free_odds]
        JE=J[:,ecols]
        JO=J[:,ocols] if ocols else np.zeros((len(evens),0))
        dE_dO=-solve_triangular(JE,JO,lower=True,unit_diagonal=True)
        ridx={n:i for i,n in enumerate(self.residual_indices)}
        JR=np.zeros((len(self.residual_indices),len(self.free_odds)),float)
        for j,n in enumerate(self.free_odds):
            JR[ridx[n],j]=1.0
        for i,n in enumerate(evens):
            if n in ridx:
                JR[ridx[n],:]=dE_dO[i,:]
        aux=dict(evens=evens,cols=cols,J=J,JE=JE,JO=JO,dE_dO=dE_dO)
        return residual,JR,b,u,maxres,aux

def x_from_u(prob,u_map):
    return np.array([float(u_map.get(n,0.0)) for n in prob.free_odds],float)
