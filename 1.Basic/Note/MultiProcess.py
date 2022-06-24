# # Before
# total1 = total2 = total3 = 0

# for i in range(0, 100000000):
#     total1 += i
# print(total1)

# for i in range(100000001, 200000000):
#     total2 += i
# print(total2)

# for i in range(200000001, 300000000):
#     total3 += i
# print(total3)

# print(">>>> End <<<<")

# 하나의 CPU당 하나씩 실행해줌 process

# After
from multiprocessing import Process

def start_get(start, end):
    total = 0
    for i in range(start, end):
        total += i
    print(total)

if __name__ == '__main__':
    # 프로세스를 생성 합니다.
    p0 = Process(target=start_get, args=(0, 100000000))
    p1 = Process(target=start_get, args=(100000001, 200000000))
    p2 = Process(target=start_get, args=(200000001, 300000000))

    # 프로세스의 시작
    p0.start()
    p1.start()
    p2.start()

    # 순서를 정리 : 다른 프로세스가 종료될때 까지 대기
    p0.join()
    p1.join()
    p2.join()

    print(">>>> END <<<<")