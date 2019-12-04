prices = {
    'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
}


"""
dictionary에 있는 데이터에 대한 연산(min, max, sort 등...)이 필요할 경우
zip()은 단 한번만 소비할 수 있는 이터레이터 생성 

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) -> 정상 출력(zip 소모)
print(max(prices_and_names)) -> ValueError: max의 인자가 비어있음

가장 낮은 가격을 가지고 있는 주식은?
# 일반적인 방법
min(prices, key=lambda k: prices[k])  # FB 리턴
min_value = prices(min(prices, key=lambda k: prices[k]))  # FB의 값(최소) 리턴
# zip을 이용한 방법
prices_and_names = zip(prices.values(), prices.keys())

여러 엔트리가 동일한 값을 가질 경우 자동으로 키를 비교하여 정렬한다.
>>> prices = { 'AAA' : 45.23, 'ZZZ': 45.23 } 
>>> min(zip(prices.values(), prices.keys())) 
(45.23, 'AAA')
>>> max(zip(prices.values(), prices.keys())) 
(45.23, 'ZZZ')

# 아래에 반환된 view 객체는 집합 연산을 지원
dict.keys() -> key-view 반환
dict.items() -> item-view 반환
"""

# 최소값
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# 정렬
sorted_price = sorted(zip(prices.values(), prices.keys()))
print(sorted_price)