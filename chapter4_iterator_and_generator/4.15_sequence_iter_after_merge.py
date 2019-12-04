import heapq
"""
# heap: https://www.notion.so/afmadadans/Heap-Heap-sort-c0de11eaad3845f1995e718b7d5a32d4
# heap sort: https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/
(heapq.merge를 사용할 떄, 각 시퀀스는 반드시 정렬된 상태)
heapq.merge는 시퀀스를 한꺼번에 읽지 않고 순환하며 데이터를 처리하기 때문에 
아주 긴 시퀀스(파일 등)도 무리 없이 처리할 수 있다.

Question: 파일의 정렬 순서는 어떻게 판단하는가?(크기???)
"""
a = [0, 1, 2, 4]
b = [3, 5, 6, 7]
# b = [7, 3, 4, 5, 6]  # -> 순차적으로 출력하고 순환 종료
for c in heapq.merge(a, b):
    print(c)
