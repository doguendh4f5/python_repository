# 01
letters = 'python'
print(letters[1])
print(letters[3])

# 02
string = "PYTHON"
reversed_string = "".join(reversed(string))
print(reversed_string)

# 03
url = input("url = ")
right_index = url.rfind('kr')
print(right_index)
domain = url[right_index] + url[right_index+1]
print(domain)

# 04
file_name = "보고서.xlsx"
suffix = 'xlsx'
print(file_name.endswith(suffix))

# 05
file_name2 = "2020_보고서.xlsx"
print(file_name2.startswith("2020"))

# 06
score = int(input("점수를 입력해주세요 : "))
if score >= 81:
    print("A")
elif score >= 61:
    print("B")
elif score >= 41:
    print("C")
elif score >= 21:
    print("D")
else:
    print("E")

# 07
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 08
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
result = input("투자 종목 이름을 입력해주세요 : ")
if result in warn_investment_list:
    print("투자 경고 종목입니다.")
if result not in warn_investment_list:
    print("투자 경고 종목이 아닙니다.")

# 09
list = [100, 200, 300]
for i in list:
    print(i+10)

# 10
list2 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in list2:
    print(len(str(i)))

