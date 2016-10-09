from graph import Graph
from collections import deque

def route_exists_dfs(graph, n1, n2):
	seen = set()
	proc = [n1]

	while proc:
		n = proc.pop()
		if n == n2:
			return True

		seen.add(n)
		neighbours = [ne for ne in graph[n] if ne not in seen]
		proc.extend(neighbours)

	return False

def route_exists_bfs(graph, n1, n2):
	seen = set()
	proc = deque([n1])

	while proc:
		n = proc.popleft()
		if n == n2:
			return True

		seen.add(n)
		neighbours = [ne for ne in graph[n] if ne not in seen]
		proc.extend(neighbours)

	return False

if __name__ == '__main__':
	g = Graph()
	g1 = g.connected_graph
	g2 = g.disconnected_graph

	assert route_exists_dfs(g1, 1, 4) == True
	assert route_exists_dfs(g2, 1, 4) == False

	tests = (
		((g1, 1, 4), True),
		((g2, 1, 4), False),
	)

	for i, (params, sol) in enumerate(tests):
		assert route_exists_dfs(*params) == sol
		print "DFS Test %d passed." % (i, )
		assert route_exists_bfs(*params) == sol
		print "BFS Test %d passed." % (i, )