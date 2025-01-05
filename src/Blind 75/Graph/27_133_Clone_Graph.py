class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors


def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    if not node:
        return None
    nodesCopy = {}
    currNode = node
    stack = []
    stack.append(currNode)
    while stack:
        currNode = stack.pop()
        if currNode not in nodesCopy:
            nodesCopy[currNode] = Node(currNode.val, [])
        for neighbor in currNode.neighbors:
            if neighbor not in nodesCopy:
                nodesCopy[neighbor] = Node(neighbor.val, [])
                stack.append(neighbor)
            nodesCopy[currNode].neighbors.append(nodesCopy[neighbor])
    
    return nodesCopy[node] if node else None