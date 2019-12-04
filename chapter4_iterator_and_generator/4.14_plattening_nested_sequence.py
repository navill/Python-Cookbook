from collections.abc import Iterable

"""
중첩된 시퀀스 풀기: 재귀 제너레이터(yield from)
isinstance를 이용해 각 항목을 비교, sequence(예제에서는 list) 일 경우 yield from을 이용해 재귀 실행
ignore_types: str과 bytes를 무시할 타입으로 지정하여 문자열이나 바이트열을 분해하지 않도록 설정
"""


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
            """
            # yield를 이용할 경우
            for i in flatten(x):
                yield i
            """
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
str_items = ['jihoon', 'jihoon1', ['jihoon2', 'jihoon3', ['jihoon4'], 'jihoon5']]
for i in flatten(items):
    print(i)

# ignore_type에 의해 문자열은 분해되지 않음
for i in flatten(str_items):
    print(i)
