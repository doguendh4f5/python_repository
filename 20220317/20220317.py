# 20220317 과제 제출
# 201832024 서동주

# 001
print("Hello World")

# 002
print("Mary's cosmetics")

# 003
print('신씨가 소리질렀다. "도둑이야".')

# 004
print('"C:\Windows"')

# 005
print("안녕하세요.\n만나서\t\t반갑습니다.")
# >> \n은 문자열 안에서 줄을 바꿀 때 사용하고 \t는 문자열 사이에 탭 간격을 줄 때 사용한다

# 051
movie_rank=['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

# 052
movie_rank=['닥터 스트레인지', '스플릿', '럭키']
movie_rank.append('배트맨')
print(movie_rank)

# 053
movie_rank=['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

# 058
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 060
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

# 102
print(3 == 5)
# >> 3과 5가 같지 않으므로 False를 반환한다

# 103
print(3 < 5)
# >> 5가 3보다 크므로 True를 반환한다

# 104
x = 4
print(1 < x < 5)
# >> x의 값이 4인데 4는 1보다 크고 5보다 작으므로 True를 반환한다

# 105
print ((3 == 3) and (4 != 3))
# >> (3 == 3)과 (4 != 3) 의 결과값이 모두 True여야 True를 반환하는데 둘 다 참이므로 True를 반환한다
