"""
# 1
print("Hello")
print('hello','everyone')
print('hello', end='!!!')
print('hello', end='')
print('hello', sep="줄 사이 입니당")

a = 123
b = 'hello'
print(a,b)
print(a, 456, b, 'World')

#2
print("Hello Python!")
print("Nice to meet you.")
print('Hello"Python"')
print("Hello'Python'")
print('Hello','Python!')
print('Hello'+'Python!')


# 4
s1 = '화면에 직접 출력'
s2 = 'ab\c'
s3 = 'does'
print(s1)
print(s2)
print(s3)
print(s1[0])
print(s2[1])
print(s3[1:3])
print(s3[-1])
print(s3[-2])



# 5

a = 2
b = 3.14
c = a+b
print(a)
print(b)
print(c)
print(round(c,2)) # 소수점 반올림 함수
print("%.2f"%(c))
print(a+b)
print(a,b,a+b,c)
d=1e2 # 10의 2승
e=1e-2
print(d)
print(e)


# 6
item1 = '사과'
price1 = 1000
item2 = '바나나'
price2 = 500
print(item1, price1)
print(item2, price2)




# 7

item1 = '사과'
price1 = 1000
item2 = '바나나'
price2 = 500
print(item1, price1)
print(item2, price2)
print(item1, price1, sep=',', end='/')
print(item2, price2)



# 8
item1 = '사과'
price1 = 1000
item2 = '바나나'
price2 = 500
str1 = '{}는 {}원입니다.'
print(str1.format(item1, price1))
print(str1.format(item2, price2))

"""

# 9

item1 = '사과'
price1 = 1000
item2 = '바나나'
price2 = 500
str2 = '%s는 %d원입니다.'
print(str2%(item1, price1))
print(str2%(item2, price2))