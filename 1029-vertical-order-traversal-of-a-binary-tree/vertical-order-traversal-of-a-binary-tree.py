class Solution:
    def verticalTraversal(self, root):
        nodes = []

        def dfs(node, row, col):
            if not node:
                return

            nodes.append((col, row, node.val))

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        nodes.sort()

        answer = []
        current_col = float("-inf")

        for col, row, value in nodes:
            if col != current_col:
                answer.append([])
                current_col = col

            answer[-1].append(value)

        return answer