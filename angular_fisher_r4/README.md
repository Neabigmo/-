# Angular Fisher R4

这是 R3 之后的有界理论审计分支。它不启动远程计算，不做高维优化、不做参数 campaign、不增加 Hermite 截断，也不做 Gröbner/resultant。

本轮目标是把完整 angular MGF identity 写成精确的 tilted-mixture / Fisher 账本，并检查 Cramér–Rao、Stam 和 D3 圆周 Poincaré 是否足以推出角向缺陷 `C_z` 消失。

运行：

```text
python run_angular_fisher.py
python audit_results.py
pytest -q
```

主要结果位于 `results/`。本轮结论预设为可被审计推翻的二分：若闭合则写 A；若预算仍允许非零 `C_z`，写 B。当前实现给出 B：精确恒等式成立，但三类非负不等式之间仍缺少把角向 Fisher 能量强制为零的跨角度传输/等号结构。

注意：代数 gap witness 只说明这些不等式在抽象变量层面不足以推出 `C_z=0`，不是原始目标概率模型的反例。

