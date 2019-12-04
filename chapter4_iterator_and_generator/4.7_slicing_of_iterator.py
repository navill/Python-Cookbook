"""
이터레이너와 제너레이터는 일반적으로 연산이 이루어지기 전까지
데이터의 길이를 알 수 없고 인덱싱을 구현하지 않기 때문에 slicing이 불가능하다.
단, 이터레이터는 뒤로 감을 수 없기 때문에 필요하다면 list로 변환 후 데이터를 처리해야한다.
"""


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# c[10:30]  -> 에러
import itertools

for i in itertools.islice(c, 10, 30):
    print(i)
