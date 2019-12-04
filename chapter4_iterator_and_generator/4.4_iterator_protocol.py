# depth-first search algorithm with iterator protocol

# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._children = []
#
#     def __repr__(self):
#         return f'Node {self._value}'
#
#     def add_child(self, node):
#         self._children.append(node)
#
#     def __iter__(self):
#         return iter(self._children)
#
#     def depth_first(self):
#         yield self
#         for c in self:
#             yield from c.depth_first()
#
#
# if __name__ == '__main__':
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)
#     child1.add_child(Node(3))
#     child1.add_child(Node(4))
#     child2.add_child(Node(5))
#     child2.add_child(Node(6))
#
#     for ch in root.depth_first():
#         print(ch)



"""
아래의 iterator protocol 반드시 이해할 것
- 쓰기 좋은 코드(아래 코드는 지저분한 코드임)는 아니지만 동작 원리를 이해
"""

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f'Node {self._value}'

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        # iter(iterable) -> iterator 생성
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator:
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter is None:
            self._children_iter = iter(self._node)  # -> iterator 생성
            # _children_iter에는 위에서 생성된 iterator를 담고 있다.
            return self._node

        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))
child2.add_child(Node(6))

for ch in root.depth_first():
    print(ch)
