#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import pandas as pd


def main():
    ap=argparse.ArgumentParser();ap.add_argument('result_dir');ap.add_argument('worklog');a=ap.parse_args()
    r=Path(a.result_dir);w=Path(a.worklog);s=json.loads((r/'stage27t_summary.json').read_text())
    b=pd.read_csv(r/'stage27t_energy_brackets.csv')
    vals=[]
    for _,x in b.iterrows():
        if pd.notna(x.primal_UB): vals.append(f"{x.label}: LB={x.dual_LB:.6g}, UB={x.primal_UB:.6g}, {x.primal_status}")
    text="\n## 2026-09-03 — Stage27T two-sided energy bracket\n\n"
    text+="- 完成内容：完成 zero-tail audit、stable MP dual-Gram finite-tail reconstruction 与两侧能量 bracket；未运行 Stage28 或 OU-coherent multi-q campaign。\n"
    text+=f"- 可信结果：`{s.get('nq_only_scaling_status')}`；validated primal rows={s.get('validated_primal_rows')}。"+("；"+"；".join(vals) if vals else "")+"\n"
    text+="- 异常/限制：结果仍是 adaptive compact numerical-domain evidence，不是全 continuum/theorem certificate；仅 validated upper bounds 可用于 bracket。\n"
    text+="- 下一步：等待 ChatGPT 独立审计；若 NQ-only scaling 被数值排除，则优先理论研究 OU-coherent simultaneous-q tail，但不自动启动。\n"
    old=w.read_text(encoding='utf-8') if w.exists() else '# PROJECT_WORKLOG\n'
    if 'Stage27T two-sided energy bracket' not in old:
        w.write_text(old.rstrip()+"\n"+text,encoding='utf-8')
    print('STAGE27T_WORKLOG_UPDATED',w)
if __name__=='__main__':main()
