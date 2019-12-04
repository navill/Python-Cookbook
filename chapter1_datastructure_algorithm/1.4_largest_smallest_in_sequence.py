import heapq

"""
[heap] https://www.notion.so/afmadadans/Heap-Heap-sort-c0de11eaad3845f1995e718b7d5a32d4
heapq.nsmallest & heapq.nlargest
시퀀스에 포함된 항목 중 가장 작거나 큰 값을 구할 때 유용
가장 먼저 데이터를 heapify
>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> heap = list(nums)
>>> heapq.heapify(heap)
>>> heap
[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]

만일 최대값 또는 최소값을 찾고자 할 때는 max() & min()가 더 빠른 성능을 보인다.
N의 크기가 컬렉션과 비슷할 경우, 정렬 후 인덱싱을 하는 것이 더 빠를 수 있다.
"""


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# Prints [-4, 1, 2]
print(heapq.nsmallest(3, nums))
# Prints [42, 37, 23]
print(heapq.nlargest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda k: k['price'])
print(cheap)