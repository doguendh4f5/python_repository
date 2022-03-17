watch = 100000
a = 'pig'
b = 'dad'

print(a)
print(b)
print(watch)
print(a+b)
print(a+' '+b)

aa = 1
bb = 100
aa, bb = bb, aa
print(aa)
print(bb)

# 예제입니다

a1 = [10, 20, 30]
b1 = a1
a1[0] = 200  # 포인터 개념 같음...
print(b1)

# print 사용 예제입니다

print("Hello World")
print('Hello World')
print(1)
print("1") # 문자 1

c = 1
print("c="+str(c)) # str은 괄호 안 값 문자로
print("c=",c) # 한 칸 띄워짐
print("c={}".format(c)) # c를 포맷해 괄호 안에 문자 형태로 나타냄 형 변환 