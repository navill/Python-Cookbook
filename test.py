from collections import namedtuple

Result = namedtuple('Result', 'count average')


# subgenerator
# 딕셔너리의 항목당 평균을 구한다.
# caller의 group.send(None)을 이용해 항목의 평균이 끝날 때 average의 동작을 중지시킨다.
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # 두 번째 for문 '*'로 이동
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    # 반환된 Result는 위임자의 yield from의 값이 된다.
    return Result(count, average)


# delegating generator(위임자)
def grouper(results, key):
    while True:
        results[key] = yield from average()


# client or caller
def main(data):
    results = {}
    for key, values in data.items():  # for-1
        group = grouper(results, key)
        # priming - 제너레이터 기동
        next(group)
        # 각 그룹의 데이터를 처리하기 위한 반복문
        for value in values:  # for-2('*')
            # caller(client)가 보내는 값은 subgenerator의 term에 바인딩 된다
            group.send(value)
        # 하나의 그룹이 끝나면 클라이언트에 None을 인가하여
        # 현재 실행 중인 그룹의 average()가 중단시킨다.
        # important!!
        group.send(None)
    print(results)
    # {'girls;kg': Result(count=10, average=42.040000000000006),
    # 'girls;m': Result(count=10, average=1.4279999999999997),
    # 'boys;kg': Result(count=9, average=40.422222222222224),
    # 'boys;m': Result(count=9, average=1.3888888888888888)}
    return results


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print(f'{result.count:2} {group:5} averaging {result.average:.2f}{unit}')


data = {'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
        'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
        'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
        }

if __name__ == '__main__':
    result = main(data)
    report(result)

#  9 boys  averaging 40.42kg
#  9 boys  averaging 1.39m
# 10 girls averaging 42.04kg
# 10 girls averaging 1.43m
