def countComponents(n, edges):
    nodes = [set() for _ in range(n)] 
    
    for edge in edges:
        nodes[edge[0]].add(edge[1])
        nodes[edge[1]].add(edge[0])
    
    num = 0
    visited = set()
    parent = [-1] * n
    for i in range(n):
        stack = [i]
        while stack:
            curr = stack.pop();
            if curr in visited:
                continue
            visited.add(curr)
            for node in nodes[curr]:
                if parent[node] == -1 and node not in visited:
                    parent[node] = curr
                if parent[curr] != node:
                    stack.append(node)
            if parent[curr] == -1:
                num += 1

        
    return num

print(countComponents(3, [[0,1],[0,2]])) # 1
print(countComponents(6, [[0,1],[1,2],[2,3],[4,5]])) #2