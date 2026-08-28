class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visted = {}
        if node is None:
            return None
        def dfs(node):
            if node in visted:
                return visted[node]
            newNode = Node(node.val)
            visted[node] = newNode          # mark before recursing -> breaks cycles
            for i in range(len(node.neighbors)):
                newNode.neighbors.append(dfs(node.neighbors[i]))
            return newNode
        new = dfs(node)
        return new