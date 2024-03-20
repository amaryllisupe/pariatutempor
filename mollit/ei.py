def insert(self, key: int, value: int) -> None:
    """
    Inserts a new key <key> and value <value> into the tree. If the key already exists, updates its value.
    """
    if key in self.tree:
        self.tree[key] = value
    else:
        self.tree[key] = value
        self._insert(key)

def _insert(self, key: int) -> None:
    """
    Inserts a new key <key> into the tree.
    """
    parent = self._find_parent(key)
    if parent is None:
        self.root = key
    else:
        if key < parent:
            self.left[parent] = key
        else:
            self.right[parent] = key
