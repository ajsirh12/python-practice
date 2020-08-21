class A:
    g = 5   # 공유 클래스와 인스턴스

    def __init__(self):
        pass
        # A.g = 10    #클래스 변수의 증가

        # self.g = 20
        # self.g += 1   #인스턴스 변수

    def inc(self):
        A.g += 1

    def dp(self):
        print(self.g)

    def set(self):
        self.g = 4

# a = A()
# print(A.g)
# a.g = 20
# print(a.g)
# a.dp()

a = A()
a.set()
a.inc()
a.dp()
b = A()
b.inc()
b.dp()
print(A.g)