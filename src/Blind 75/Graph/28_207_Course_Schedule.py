def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    # Return True if no prereqs are specified
    if not prerequisites:
        return True

    # create graph
    graph = [[] for _ in range(numCourses)]
    for req in prerequisites:
        graph[req[0]].append(req[1])
    
    # need dfs -> top sort
    seenCourses = set()
    currPath = set() 
    backtracking = False
    for course in range(len(graph)):
        if course in seenCourses:
            continue

        stack = [course]
        
        while stack:
            currCourse = stack[-1]
            prereqs = graph[currCourse]

            if currCourse in seenCourses:
                stack.pop()
                continue

            if currCourse in currPath and not backtracking:
                return False
            
            currPath.add(currCourse)

            # Node not yet visited
            allNeighborsVisited = True
            for req in prereqs:
                if req not in seenCourses:
                    stack.append(req)
                    allNeighborsVisited = False
                    backtracking = False
                    break
            
            if allNeighborsVisited:
                seenCourses.add(currCourse)
                currPath.remove(currCourse)
                stack.pop()
                backtracking = True
            
    return True
    


print(canFinish(3, [[0,1],[0,2],[1,2],[2,1]])) # False
print(canFinish(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]])) # True
print(canFinish(4, [[0,1],[1,2],[0,3],[3,0]])) # False