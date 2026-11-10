import gurobipy as gp
from gurobipy import GRB

with gp.Env(empty=True) as env:
    env.setParam("OutputFlag", 0)
    env.start()
    with gp.Model("Demand_Limits", env=env) as model:
        # 整数座位分配 / Integer seat allocations
        x = model.addVars(
            [1, 2, 3], lb=0, vtype=GRB.INTEGER, name="seats"
        )
        # 航段容量 / Leg capacities
        model.addConstr(x[1] + x[3] <= 100, "Leg_1")
        model.addConstr(x[2] + x[3] <= 100, "Leg_2")
        # 新增需求上限 / Additional demand limits
        model.addConstr(x[1] <= 60, "Demand_AB")
        model.addConstr(x[2] <= 80, "Demand_BC")
        model.setObjective(
            200*x[1] + 150*x[2] + 300*x[3], GRB.MAXIMIZE
        )
        model.optimize()
        if model.Status == GRB.OPTIMAL:
            a, b, c = (round(x[j].X) for j in [1, 2, 3])
            print(f"Optimal revenue: {model.ObjVal:,.2f}")
            print(f"A-B: {a}; B-C: {b}; A-C: {c}")
            print(f"Leg 1: {a+c}/100; Leg 2: {b+c}/100")
        else:
            print(f"No optimum; status: {model.Status}")
