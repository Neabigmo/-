# Posterior-variance rewrite

With d=1-q, define

    V_q(x)=d+d^2 K_q''(x)=Var_{q,x}(X).

Then V_q>=0, E_nu V_q=d, and the order-four and order-six identities are

    E[d^2/2 V_q'' + 3(V_q-d)^2] = 0,
    E[d^4 V_q'''' + 27d^2 V_q''(V_q-d)
      + 3d^2(V_q')^2 + 54(V_q-d)^3] = 0.

