# sequence의 순서를 유지하면서 중복 제거
# sequence 값이 hashable 일 경우
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 5, 10]
print(list(dedupe(a)))


b = set()
b.add(1)
b.add(2)
b.add(3)
b.add(4)
b.add(5)
b.add(6)
print(b)