LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    key = root
    flag = True

    def less(self, other):
        if not self or not other:
            return False
        return self.value <= other.value

    def check(root, left=None):
        nonlocal flag, key
        if not root:
            return
        if less(root, root.left) \
                or less(root.right, root) \
                or left and less(key, root.right):
            flag = False
        check(root.left, True)
        check(root.right, False)
    check(root)
    return flag


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)
    node3.value = 6
    assert not solution(node5)


if __name__ == '__main__':
    test()
