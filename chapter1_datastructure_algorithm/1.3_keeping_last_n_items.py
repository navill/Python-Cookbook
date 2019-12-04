from collections import deque

"""
순환이나 프로세싱 중 발견한 마지막 N개의 아이템을 유지
-> collections.deque
deque의 사이즈(N)를 정하고 데이터를 아이템을 추가할 경우, 마지막 N개의 아이템을 유지할 수 있다.
"""


def search(lines, pattern, history=3):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line
        previous_lines.append(line)
    print([i for i in previous_lines])


string = ['1.string: python', '2.string: django', '3.string: AWS', '4.string: python', '5.string: python',
         '6.string: java']
result = search(string, 'python')

for i in result:
    print(i)
