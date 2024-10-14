# Завдання 1
# Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві пошуку або в AVL-дереві. 
# Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Вставка елементів в бінарне дерево пошуку
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Пошук найбільшого значення в двійковому дереві пошуку
def find_max_value(root):
    current = root
    # Найбільше значення завжди знаходиться в правій гілці дерева
    while current.right is not None:
        current = current.right
    return current.value

# Приклад використання
tree_root = None
values = [20, 10, 30, 5, 15, 25, 35]
for v in values:
    tree_root = insert(tree_root, v)

max_value = find_max_value(tree_root)
print(f"Найбільше значення в дереві: {max_value}")