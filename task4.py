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

# Пошук найменшого значення в двійковому дереві пошуку
def find_min_value(root):
    current = root
    # Найменше значення завжди знаходиться в лівій гілці дерева
    while current.left is not None:
        current = current.left
    return current.value

# Пошук суми всіх значень у двійковому дереві пошуку
def find_sum_of_values(root):
    if root is None:
        return 0
    return root.value + find_sum_of_values(root.left) + find_sum_of_values(root.right)

# Клас для коментарів з ієрархічною структурою
class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        indent = "    " * level
        print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)

# Приклад використання дерева пошуку
tree_root = None
values = [20, 10, 30, 5, 15, 25, 35]
for v in values:
    tree_root = insert(tree_root, v)

# max_value = find_max_value(tree_root)
# print(f"Найбільше значення в дереві: {max_value}")

# min_value = find_min_value(tree_root)
# print(f"Найменше значення в дереві: {min_value}")

# sum_of_values = find_sum_of_values(tree_root)
# print(f"Сума всіх значень в дереві: {sum_of_values}")

# Приклад використання класу Comment
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()