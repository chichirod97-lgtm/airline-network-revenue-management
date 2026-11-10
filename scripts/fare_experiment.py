import gurobipy as gp
from gurobipy import GRB

# 无需求上限 / No demand limits
with gp.Env(empty=True) as env:
    env.setParam("OutputFlag", 0)
    env.start()
    print("A-C fare | A-B | B-C | A-C | Revenue")
    for fare in [250, 300, 350, 400, 450]:
        with gp.Model("Fare_Sensitivity", env=env) as model:
            x = model.addVars(
                [1, 2, 3], lb=0, vtype=GRB.INTEGER, name="seats"
            )
            # 容量约束 / Capacity constraints
            model.addConstr(x[1] + x[3] <= 100)
            model.addConstr(x[2] + x[3] <= 100)
            # 仅改变联程票价 / Vary only the connecting fare
            model.setObjective(
                200*x[1] + 150*x[2] + fare*x[3], GRB.MAXIMIZE
            )
            model.optimize()
            if model.Status == GRB.OPTIMAL:
                a, b, c = (round(x[j].X) for j in [1, 2, 3])
                print(f"{fare} | {a} | {b} | {c} | {model.ObjVal:,.2f}")
            else:
                print(f"Fare {fare}: status {model.Status}")

# 350 时存在多个最优解 / Multiple optimal solutions at fare 350
