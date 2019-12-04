"""
순환 객체에서 시작하는 일부를 건너뛰고 데이터를 추출하고자 할 때 itertools.dropwhile(function, iterable)을 사용할 수 있다.
생략이 필요한 정확한 위치(인덱스)를 알경우 islice를 이용할 수 있다.
"""

from itertools import dropwhile

# 데이터의 처음 시작이 '#'일 경우
with open('test.txt') as f:
    # dropwhile은 조건 함수를 만족한 이후 부터 동작하지 않는다.
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')
        """
        lmn
        opqrst
        uvws
        # 1234
        # 567
        0000
        """
print('\n')

# 만일 모든 라인의 주석을 무시하고자 할 경우 아래와 같이 구성
with open('test.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')
        """
        lmn
        opqrst
        uvws
        0000
        """