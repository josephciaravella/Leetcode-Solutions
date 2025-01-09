def validTree(n, edges):
    '''
    check for connectivity and check that there are no cycles
    '''
    nodes = [set() for _ in range(n)] 
    
    for edge in edges:
        nodes[edge[0]].add(edge[1])
        nodes[edge[1]].add(edge[0])
    
    visited = set()
    stack = [0]
    parent = [-1] * n
    while stack:
        curr = stack.pop();
        if curr in visited:
            return False
        visited.add(curr)
        for node in nodes[curr]:
            if parent[node] == -1 and node not in visited:
                parent[node] = curr
            if parent[curr] != node:
                stack.append(node)  

        
    return len(visited) == n 

print(validTree(5, [[0,1],[0,2],[0,3],[1,4]])) # True
print(validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])) # False