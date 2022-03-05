from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def create_bt(value_queue):
    """Crear arbol binario"""

    if len(value_queue) <= 0:
        return None, None

    root = Node(value_queue.popleft())

    current_queue = deque()
    current_queue.append(root)

    while len(current_queue) > 0 and len(value_queue) > 0:

        current_node = current_queue.popleft()

        left = value_queue.popleft()
        if left is not None:
            current_node.left = Node(left)
            current_queue.append(current_node.left)

        right = value_queue.popleft()
        if right is not None:
            current_node.right = Node(right)
            current_queue.append(current_node.right)

    return root


def create_bt_fls(value_list):
    """crear arbol desde lista"""

    return create_bt(deque(value_list))


def lca_arr(bst, v1, v2):

    if v1 <= bst.value <= v2 or v1 >= bst.value >= v2:
        return bst
    elif bst.value > v1 and bst.value > v2:
        return lca_arr(bst.left, v1, v2)
    else:
        return lca_arr(bst.right, v1, v2)


arr = create_bt_fls([4, 2, 1, 3, 5, 7, 6])
num1 = int(input("Introduce el nodo izquierdo: "))
num2 = int(input("Introduce el nodo derecho: "))

lca = lca_arr(arr, num1, num2)



print(lca.value)