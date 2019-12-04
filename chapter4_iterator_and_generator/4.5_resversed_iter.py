"""
역방향 순환은 객체가 __reversed__() 특별 메소드를 구현하고 있거나 크기를 알 경우 사용 가능
두 조건을 만족하지 못할 경우 순환 객체를 list 타입으로 변환하여 순환할 수 있지만, 메모리 낭비가 심하다
"""


class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


cd = CountDown(5)

for i in cd:
    print(i)
    # 5,4,3,2,1

for i in reversed(cd):
    print(i)
    # 1,2,3,4,5
