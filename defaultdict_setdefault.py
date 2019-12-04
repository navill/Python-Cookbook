from collections import defaultdict, OrderedDict

# defaultdict
e = defaultdict(list)
e['a'].append(1)
e['a'].append(2)
e['b'].append(3)
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})
print(e)

# setdecault
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(3)
# {'a': [1, 2], 'b': [3]}
print(d)


"""
# OrderedDict
OrderedDict는 double linked list로 이루어져있기 때문에 많은 데이터를 처리할 경우 메모리 소모량(일반 딕셔너리의 두 배)을 고려해야한다.
새로운 아이템을 삽입할 경우 리스트의 마지막에 추가한다.
-> 삽입 순서와 관련 있는 키를 기억
"""
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
