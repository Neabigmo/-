# Fisher closure audit

精确恒等式和 Gaussian replay 均通过；但 Cramér–Rao、Stam、D3 Poincaré 与 polar budget 的标量联立仍允许 `C_z^2>0`。

审计中的抽象 witness 取 `epsilon=1/5`、`V_a=1`、`V_b=4/5`、`A^2=0`、`C^2=1/5`，同时满足两条预算、Cramér–Rao 等号、Stam 等号和 Poincaré 上界，却保留非零角向项。它不是原始分布的反例，只精确指出缺失的结构：需要一个把不同 theta 的条件 Fisher/score 与目标 angular identity 连接起来的额外等号或传输不等式。

