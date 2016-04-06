import itertools

def answer(N, K):
    nodes = range(N)
    edges = list(itertools.combinations(nodes, 2))

    #for graph in itertools.combinations(edges, K):
    #    print graph

    count = 0
    for graph in itertools.combinations(edges, K):
        connected_nodes = sorted(list(set(y for x in graph for y in x)))
        if connected_nodes == nodes:
            tree = {}
            for graph_edge in graph:
                if graph_edge[0] not in tree:
                    tree[graph_edge[0]] = []
                tree[graph_edge[0]].append(graph_edge[1])
                if graph_edge[1] not in tree:
                    tree[graph_edge[1]] = []
                tree[graph_edge[1]].append(graph_edge[0])

            current = tree.keys()[0]
            node_list = []
            def traverse_tree(current, tree):
                if current not in node_list:
                    node_list.append(current)
                    if current in tree:
                        next_nodes = tree[current]
                        for node in next_nodes:
                            traverse_tree(node, tree)
                return

            traverse_tree(current, tree)
            if nodes == sorted(node_list):
                count += 1

    return count

for x in range(1, 10):
    for i in range(x - 1, ((x * (x - 1)) / 2) + 1):
        print x,",", i, ":", answer(x, i)

print answer(2, 1)

print answer(4, 3)
print answer(4, 4)
print answer(4, 5)
print answer(4, 6)

print answer(5, 4)

print answer(5, 10)
print answer(5, 9)
