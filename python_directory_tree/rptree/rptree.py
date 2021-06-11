# rptree.py file
import os
import pathlib

PIPE="|"
ELBOW="|__"
TEE="|--"
PIPE_PREFIX = "|    "
SPACE_PREFIX = "    "

# high lavel directory tree class

class DirectoryTree:
    def __init__(self,root_dir):
        self._generator = _TreeGenerator(root_dir)

    def generator(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)

# low lavel tree generator class
class _TreeGenerator:
    def __init__(self, root_dir):
        self._root_dir = pathlib.Path(root_dir)
        self._tree = []

    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)
