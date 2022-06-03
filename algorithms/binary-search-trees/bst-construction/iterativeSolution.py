class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = self
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = BST(value)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = BST(value)
                    break
                else:
                    node = node.right
        return self

    def contains(self, value):
        node = self
        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
        return False

    def remove(self, value, parent=None):
        node = self
        while node is not None:
            if value < node.value:
                parent = node
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
            else:
                # if node has 2 children
                if node.left is not None and node.right is not None:
                    # current node = smallest value of right subtree
                    node.value = node.right.getMinValue()
                    # remove the smallest value of right subtree
                    # pass in current node as parent node
                    node.right.remove(node.value, node)
                # if node is root node
                elif parent is None:
                    if node.left is not None:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right is not None:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                    else:
                        pass
                # if current node is left child
                elif parent.left == node:
                    parent.left = node.left if node.left is not None else node.right
                # if current node is right child
                elif parent.right == node:
                    parent.right = node.left if node.left is not None else node.right
                break
        return self

    def getMinValue(self):
        node = self
        while node.left is not None:
            node = node.left
        return node.value
