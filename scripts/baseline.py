import gurobipy as gp
from gurobipy import GRB

def main():
    try:
        # 初始化环境 / Initialize the environment
        with gp.Env(empty=True) as env:
            env.setParam("OutputFlag", 0)
            env.start()
            with gp.Model("Network_Revenue", env=env) as model:
                # 非负整数座位 / Nonnegative integer seats
                x = model.addVars(
                    [1, 2, 3], lb=0, vtype=GRB.INTEGER, name="seats"
                )
                # 航段容量 / Leg capacities
                model.addConstr(x[1] + x[3] <= 100, "Leg_1")
                model.addConstr(x[2] + x[3] <= 100, "Leg_2")
                # 最大化收益 / Maximize revenue
                model.setObjective(
                    200*x[1] + 150*x[2] + 300*x[3], GRB.MAXIMIZE
                )
                model.optimize()
                if model.Status == GRB.OPTIMAL:
                    print(f"Optimal revenue: {model.ObjVal:,.2f}")
                    for j in [1, 2, 3]:
                        print(f"Product {j}: {round(x[j].X)} seats")
                else:
                    print(f"No optimum; status: {model.Status}")
    except gp.GurobiError as error:
        print(f"Gurobi error {error.errno}: {error}")

if __name__ == "__main__":
    main()
