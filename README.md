# 航空网络收益管理 / Network Revenue Management

Bilingual OR course experiment using Python and Gurobi. This is a simplified classroom example, not a full replication of an airline dataset or dynamic booking model.

## View the report
Open `index.html` locally, or serve the repository with GitHub Pages. The HTML has no external dependencies. The interactive fare slider uses an analytical solution, not a browser-based solver.

## Run
Requires Python, gurobipy and an available Gurobi license.

```sh
python -m pip install -r requirements.txt
python scripts/baseline.py
python scripts/fare_experiment.py
python scripts/demand_experiment.py
```

| Scenario | Allocation (AB, BC, AC) | Revenue |
|---|---|---:|
| Baseline | (100,100,0) | 35000 |
| AC fare 400, no demand limits | (0,0,100) | 40000 |
| Demand limits AB≤60, BC≤80; original fares | (60,60,40) | 33000 |

At fare 350 there are multiple optima. Revenues 35000 and 33000 refer to different feasible sets; the baseline allocation violates the added demand limits.

## Files
- `index.html`, `style.css`, `app.js`: bilingual report and analytical fare demonstration.
- `assets/`: original experiment figures supplied by the student.
- `scripts/`: three standalone Gurobi experiments.
- `report.docx`: bilingual report with code appendices.

AI assisted with code, explanations and report assembly; the student executed experiments and supplied results and figures. Mathematical upper bounds validate both scenario optima. See the report for the retrospective mapping to the eight Harris components in the supplied course notes. Actual software versions are not supplied and should be recorded in the notebook.

## GitHub Pages
In repository Settings → Pages, choose Deploy from a branch, branch `main`, folder `/ (root)`, then Save.

Author: RICHINA ORTANCIA DOMINIQUE（杜米妮）
Course: 人工智能与经济管理研究
