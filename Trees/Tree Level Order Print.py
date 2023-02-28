import collections


class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


# def bfs(self, start_node):
#     visited = []
#     queue = [start_node]
#
#     while queue:
#         node = queue.pop(0)
#         if node not in visited:
#             visited.append(node)
#             for neighbor in self.edges[node]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#
#     return visited

def levelOrderPrint(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount, nextCount = 1, 0
    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1
        print(currentNode.val, )
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1
        if currentCount == 0:
            # finished printing current level
            print('\n', )
            currentCount, nextCount = nextCount, currentCount


tree = Node(1)
tree.left.val = 2
tree.right.val = 3
tree.left.left.val = 4
tree.right.left.val = 5
tree.right.right.val = 6
levelOrderPrint(tree)
