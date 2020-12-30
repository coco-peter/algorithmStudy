a = "peter"
print(a)
def test():
    a = "coco"
    print(a)
test()
print(a)

#19
#1차원 배열 초기화 [0 for i in range(19)]
#2차원 배열 초기화 [[0 for col in range(19)] for row in range(19)]
# 겁나헷갈림 ㅡㅡ
#

# d = [[0 for i in range(19)] for j in range(19)]
#
# for y in range(0,19):
#         num = map(int,input().split())
#         a = list(num)
#         for x in range(0,19):
#             d[y][x] = a[x]
#
# a = int(input())
#
# for i in range(0,a):
#     x,y = map(int, input().split())
#     for x1 in range(0,19):
#         if d[y-1][x1] == 1:
#             d[y-1][x1] = 0
#         else:
#             d[y-1][x1] = 1
#         if d[x1][x-1] == 1:
#             d[x1][x-1] = 0
#         else:
#             d[x1][x-1] = 1
#
#
# for y in range(0,19):
#     for x in range(0,19):
#         print("%d " %(d[y][x]) , end="")
#     print("")

# [y][x] 라고 생각하면 편하다.
# 헷갈릴대는 아래의 예제를 참고하자

# d = [[0 for cols in range(10)] for rows in range(5)]
#
# for y in range(0,5):
#     for x in range(0,10):
#         print("%d " %(d[y][x]) , end="")
#     print("")

#18 range 역순은 빼줄 값을 인덱스에 추가해야함. 증감도 만약 +2로 하려면 저렇게 해야겠지??
# a = int(input())
# b = input().split()
# c = list(b)
#
# for i in range(a-1,-1,-1):
#     print("%d " %int(c[i]), end="")

#17 제곱은 ** 이용
# a, r, n = map(int, input().split())
#
# sum = a * r ** (n -1)
# print(sum)

#16 int(a, 16)이라는 뜻은 a가 16진수이면 그것을 10진수로 바꾸겠다는것이다 아래 #12도 같은 의미
# 그렇다면 10진수를 8 16 으로 바꾸려면?? format(변수 , 'b' 'o' 'x' ) 'b' 2진수 'o' 8진수 'x' 16진수
# a = input()
# b = int(a, 16)
# # print(b)
#
# for i in range(1,16):
#     print("%X*%X=%X"%(b,i,b*i))

#15 만약 print뒤에 \n를 없애고 싶다면 end = ''를 쓰자
# a = input()
# b = ord("a")
# while b != ord(a) + 1:
#     print("%s " %chr(b), end='')
#     b = b + 1

#14
# - 출력은 맨앞이 1일텐데 -3 이 나오네?? --> 나중에 다시 확인
# a = int(input())
# b = ~a
# print(b)

#13
# a = input()
# print(chr(ord(a)+1))           # ord() : 아스키 -> 문자(A -> 65) , chr() : 문자 -> 아스키(65 -> A)

#12
# a = input()
# b = int(a,8)              a를 int형 8진수로 변경
# print("%d" %b)


#11
# a = int(input())
# print("%x" %a)            --> %x는 소문자로 %X는 대문자로 출력 16진수


#10
# %d "10진수" %o "8진수"
# a = input()
# print("%o" %int(a))

#9
# f = input()
# print("%.11lf" %float(f))

#8
# 여기서 배울 수 있는것은 그냥 input을 통해 받는것은 무조건 str형이다.
# 그래서 인지는 모르겠지만 int형으로 받으면 list화가 되지 않는다. 이게 맞는건가??
# 뭐지...???
# inputNum = input()
# count = len(inputNum)

# for i in inputNum:
#     print("[%d]" %(int(i) * pow(10,count - 1)))
#     count = count - 1




#7 python에서는 단어를 입력 받을 때, list로 안받아도 되는것인가..???
# 당연히 list화 해야하는줄 알았는데 그냥 for문에서 저렇게 받아도 하나씩 읽어오네..?? 뭐지;;;
# 물론 list화 해도 되긴 됨.
# inputword = input()
# for i in inputword:
#     print("\'%s\'" %i)

#1
# 입력 2개 이상 받을 때 !!! --> 이건 암기하자
# inputChar1, inputChar2 = input().split()
# print(inputChar2, inputChar1)

#2
# 이건좀 신기하네?? 그냥 print만 해도 띄어쓰기 기능이 있나??
# inputNum = int(input())
# print(inputNum,inputNum,inputNum)

#3
# 구분자를 따로 지정하고 싶다면 아래처럼 !
# inputH, inputM = input().split(":")
# print("%d:%d" %(int(inputH), int(inputM)))

#4
# int(input()) 이건 되는데 2개 이상받을 때는 아래처럼 map을 이용해서 받아와야한다.
# 사실 하나일때도 map이 정석이긴 하다.
# %2d만 하면 2칸을 차지하는건데 %02로 하면 빈칸은 0으로 채워준다.
# year, month, day = map(int,input().split("."))
# print("%04d.%02d.%02d" %(year, month, day))

#5
# %d로 출력하면 int형 변수에서 앞자리에 0이 있는것은 무시된다. 어찌보면 당연한 결과
# frontNum , backNum = map(str, input().split("-"))
# print("%s%s" %(frontNum, backNum))

#6
# 여기 좀 이해 안감 C랑 비교했을때..
# data = [None] * 50
# # data = input()
# print(data)
# data = input()
# print(data)

