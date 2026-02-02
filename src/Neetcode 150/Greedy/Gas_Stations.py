def canCompleteCircuit(gas, cost) -> int:
    if sum(gas)-sum(cost) < 0:
        return -1
    tank = 0
    start = 0
    for i in range(len(gas)):
        tank += gas[i]-cost[i]
        if tank < 0:
            start = i+1
            tank = 0

    return -1 if start == len(gas) else start