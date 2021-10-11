graph = {};
graph["start"]["a"] = 6;
graph["start"]["b"] = 2;

graph["a"] = {};
graph["a"]["fin"] = 1;

graph["b"] = {};
graph["b"]["a"] = 3;
graph["b"]["fin"] = 5;

graph["fin"] = {};

inifinty = float("inf");
costs = {};
costs["a"] = 6;
costs["b"] = 2;
costs["fin"] = inifinty;

parents = {};
parents["a"] = "start";
parents["b"] = "start";
parents["fin"] = None;

processed = [];

node = find_lowest_node(costs);
while node is not None:
    cost = costs[node];
    neighbors = graph[node];
    for n in neighbors.Keys():
        new_cost = cost + neighbors[n];
        if cost[n] > new_cost:
            costs[n] = new_cost;
            parents[n] = node;
        processed.append(node);
        node = find_lowest_node(costs);