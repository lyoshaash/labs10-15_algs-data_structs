class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> bool:
    def check_balance(node):
        if node is None:
            return 0, True

        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)

        height = 1 + max(left_height, right_height)
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

        return height, balanced

    _, is_balanced = check_balance(root)
    return is_balanced

def build_tree_example():
    left = Node(int(input("левый узел: ")))
    right = Node(int(input("праывй узел: ")))
    root = Node(int(input("корень: ")), left, right)
    return root

if __name__ == '__main__':
    root = build_tree_example()
    print("дерево сбалансировано" if solution(root) else "дерево не сбалансировано")

