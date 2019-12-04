import heapq

"""
우선순위 큐를 heapq를 이용해 구현(우선순위가 동일할 경우 입력 순으로 출력(pop))
"""


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # heappush syntax: heappush(heap, item)
        # 아래와 같이 tuple을 이용하여 (우선순위, 인덱스, 아이템)으로 아이템을 구성한 후 추가 작업을 구현할 수 있다.
        # tuple에 index가 없이 동일한 우선 순위를 갖을 경우 'unorderable types' 에러 발생
        # -> 동일한 우선 순위를 갖더라도 index에 의해 우선 순위를 결정하게 된다.
        # [Doc] https://docs.python.org/3.7/library/heapq.html#module-heapq
        # heapq는 기본적으로 min heap으로 구성되어있기 때문에 -priority를 사용
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # item[-1] = item
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Item({self.name})'


q = PriorityQueue()
q.push(Item('jihoon'), 7)
q.push(Item('apple'), 1)
q.push(Item('banana'), 2)
q.push(Item('grape'), 5)
q.push(Item('jihoon'), 4)
print(q.pop())  # jihoon
print(q.pop())  # grape
print(q.pop())  # jihoon
print(q.pop())  # banana