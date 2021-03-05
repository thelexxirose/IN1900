from SEIR_interaction import *


def covid19_Norway(beta, filename, num_days, dt):
    region_content = []
    regions = []

    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            l = line.strip("\t\n").split(";")
            region_content.append(l)

    for i in region_content:
        regions.append(RegionInteraction(i[1], int(i[2]), int(i[3]), float(i[4]), float(i[5])))

    problem = ProblemInteraction(regions, "Norway", beta)
    problem.set_initial_condition()

    solver = SolverSEIR(problem, num_days, dt)
    solver.solve()
    plt.figure(figsize=(9, 12))
    index = 1
    for i in problem.region:
        plt.subplot(4, 3, index)
        i.plot()
        index += 1

    plt.subplot(4, 3, index)
    plt.subplots_adjust(hspace=0.75, wspace=0.5)
    problem.plot()
    plt.show()


covid19_Norway(0.5, "fylker.txt", 100, 1.0)
