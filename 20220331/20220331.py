# 1

price_list = [32100, 32150, 32000, 32500]

for i in range(len(price_list)):
    print(i, price_list[i])


# 2

price_list = [32100, 32150, 32000, 32500]

for i in range(1, 4):
    print(90+i*10, price_list[i])


# 3

for i in range(2002, 2051, 4):
    print(i)


# 4

for i in range(0, 10):
    print(round(i*0.1, 1))


# 5

ticker = "btc_krw"
print(ticker.upper())


# 6

file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))


# 7

a = "hello world"
print(a.split(' '))


# 8

date = "2020-05-01"
a, b, c = date.split(sep='-')
print(f"{a}년 {b}월 {c}일")


# 9

listed_stocks = "5,969,782,550"
print(int(listed_stocks.replace(",", "")))


# 10

a = "hello world"
b, c = a.split(sep=' ')
print(b)
print(c)


# 11

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])


# 12

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])


# 13

list = [3, 100, 23, 44]
for i in list:
    if i % 3 == 0:
        print(i)
