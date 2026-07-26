# DFS, Leetcode_questions, Easy
from idlelib.tree import TreeNode


# Q_1
# def maximum_depth_of_binary_tree(root: TreeNode) -> int:
#     if not root:
#         return 0
#     return 1 + max(maximum_depth_of_binary_tree(root.left), maximum_depth_of_binary_tree(root.right))


# Q_2
# def same_tree(p: TreeNode, q: TreeNode) -> bool:
#     if not p and not q:
#         return True
#     if not p and not q:
#         return False
#     if p.val != q.val:
#         return False
#     return same_tree(p.left, q.left) and same_tree(p.right, q.right)


# Q_3
# def path_sum(root: TreeNode, targetSum:int, sum_nodes:int = 0) -> bool:
#     if not root:
#         return False
#     if not root.left and not root.right:
#         return (sum_nodes += root.val) == target_sum
#     sum_nodes += root.val
#     return (path_sum(root.left, targetSum, sum_nodes) or path_sum(root.right, targetSum, sum_nodes))


# Q_4
class Treenode:
     def __init__(self, val=None):
         self.val = val
         self.left = None
         self.right = None

root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)
root.right.left = Treenode(6)
root.right.right = Treenode(7)

# def inorder_traversal(root: Treenode):
#     if not root:
#         return
#     inorder_traversal(root.left)
#     print(root.val)
#     inorder_traversal(root.right)

# def helper_to_invert_binary_tree(left_child: Treenode, right_child: Treenode):
#     if left_child is None or right_child is None:
#         return
#     node_value = left_child.val
#     left_child.val = right_child.val
#     right_child.val = node_value
#     helper_to_invert_binary_tree(left_child.left, right_child.right)
#     helper_to_invert_binary_tree(left_child.right, right_child.left)


# def invert_binary_tree(root: Treenode):
#     if not root:
#         return
#     helper_to_invert_binary_tree(root.left, root.right)


# Q_5
# def helper_to_symmetric_tree(left_child: TreeNode, right_child: TreeNode) -> bool:
#     if left_child is None and right_child is None:
#         return True
#     if left_child is None or right_child is None:
#         return False
#     return helper_to_symmetric_tree(left_child.left, right_child.right) and helper_to_symmetric_tree(left_child.right, right_child.left)
#
# def symmetric_tree(root: TreeNode):
#     if not root:
#         return True
#     return helper_to_symmetric_tree(root.left, root.right)


# Q_6
# def diameter_of_binary_tree(root: Treenode) -> int:
#     diameter:int = 0
#     def dfs(node: Treenode) -> int:
#         nonlocal diameter
#         if not node:
#             return 0
#
#         left_child_depth = dfs(node.left)
#         right_child_depth = dfs(node.right)
#
#         diameter = max(diameter, left_child_depth + right_child_depth)
#
#         return 1 + max(left_child_depth, right_child_depth)
#
#     dfs(root)
#     return diameter


# Q_7
# def dfs(visited:list ,grid:list[list[int]], i:int, j:int) -> None:
#     grid[i][j] = 0
#     visited.append((i,j))
#     if not (
#             (i > 0 and grid[i-1][j]) or
#             (j > 0 and grid[i][j-1]) or
#             (i+1 < len(grid) and grid[i+1][j]) or
#             (j+1 < len(grid[0]) and grid[i][j+1])
#     ): return

#     if 0 < i and grid[i-1][j] == 1:
#         dfs(visited, grid, i-1, j)
#     if 0 < j and grid[i][j-1] == 1:
#         dfs(visited, grid, i, j-1)
#     if i+1 < len(grid) and grid[i+1][j] == 1:
#         dfs(visited, grid, i+1, j)
#     if j+1 < len(grid[0]) and grid[i][j+1] == 1:
#         dfs(visited, grid, i, j+1)

# def number_of_islands(grid:list[list[int]]) -> int:
#     count = 0
#     visited = []
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == 1 and (i, j) not in visited:
#                 count += 1
#                 dfs(visited, grid, i, j)
#     return count

# Q_8
# def lowest_common_ancestor(root: Treenode, node1: Treenode, node2: Treenode) -> TreeNode:
#     if not root:
#         return None
#
#     if root == node1 or root == node2:
#         return root
#
#     left_result = lowest_common_ancestor(root.left, node1, node2)
#     right_result = lowest_common_ancestor(root.right, node1, node2)
#
#     if left_result and right_result:
#         return root
#
#     if left_result:
#         return left_result
#     else:
#         return right_result

# Q_9
# global i = 0
# def dfs(nums:list, target:int, combination:list = [], return_list:list = []):
#    if sum(combination) > target:
#        i += 1
#        return
#    if target - sum(combination) in nums:
#        return_list.append(combination + [target - sum(combination)])
#        combination.append(nums[i])
#        dfs(nums, target, combination, return_list)

# def combination_sum(nums:list, target:int) -> list[list[int]]:
#    nums.sort()



# Q_10, Word Search
# def dfs(chars:list[list[int]], visited_chars:str, word:str, i:int, j:int, idx:int) -> bool:
#     visited_chars += chars[i][j]
#
#     if visited_chars == word:
#         return True
#
#     if not (
#         (i > 0 and chars[i-1][j] != word[idx]) or
#         (j > 0 and chars[i][j-1] != word[idx]) or
#         (j+1 < len(chars[0]) and chars[i][j+1] != word[idx]) or
#         (i+1 < len(chars) and chars[i+1][j] != word[idx])
#     ): return False
#
#     if i > 0 and chars[i-1][j] == word[idx]:
#         dfs(chars, visited_chars, word, i-1, j, idx+1)
#     if j > 0 and chars[i][j-1] == word[idx]:
#         dfs(chars, visited_chars, word, i, j-1, idx+1)
#     if j+1 < len(chars[0]) and chars[i][j+1] == word[idx]:
#         dfs(chars, visited_chars, word, i, j+1, idx+1)
#     if i+1 < len(chars) and chars[i+1][j] == word[idx]:
#         dfs(chars, visited_chars, word, i, j+1, idx+1)
#
#
#
#
#
# def word_search(chars:list[list[int]], word:str) -> bool:
#     for i in range (len(chars)):
#         for j in range (len(chars[0])):
#             if chars[i][j] in word[0]:
#                 flag = dfs(chars, "", word, i, j, 1)
#                 if flag:
#                     return True
#
#     return False

# Q_11
def validate_binary_tree(root: TreeNode, min:float = float('-inf'), max:float = float('inf')) -> bool:
    if not root.left and not root.right:
        return True
    if root.left.val >= root.val or root.left.val >= max:
        return False
    if root.right.val <= root.val or root.right.val <= min:
        return False

    return validate_binary_tree(root.left, min, max= root.val) and validate_binary_tree(root.right, min= root.val, max)