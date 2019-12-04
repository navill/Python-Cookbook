prices = {
    'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
}


"""
dictionary에 있는 데이터에 대한 연산(min, max, sort 등...)이 필요할 경우

"""


# 최소값
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# 정렬
sorted_price = sorted(zip(prices.values(), prices.keys()))
print(sorted_price)