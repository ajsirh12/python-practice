from abc import *
class source(metaclass=ABCMeta):    #추상클래스
    @abstractmethod     #추상메소드
    def bonnet(self):
        pass

    @abstractmethod
    def engine_room(self):
        pass


class Car(source):
    button = 3.15
    def __init__(self, name):
        self.cname = name
        self.engine = 2000

    def bonnet(self):
        print('보넷 열기')

    def engine_room(self):
        print('엔진룸 열기')

    @staticmethod   #데코레이터
    def RGB_signal():
        print('신호등보기')

    @classmethod
    def secret_view(cls):
        print(Car.button)

    def dp(self):
        print('Parents')

class google(Car):
    def __init__(self, name, msg):
        super().__init__(name)      # 자식생성자 없으면 자동으로 부모생성자 호출
        self.autodrive = msg    # 자식생성자 명시시 부모생선자는 super()로 호출

    def say(self):
        print(self.cname + ' Ok! Google.')

    def dp(self):
        print(self.cname, str(self.engine) + 'cc', self.autodrive)

class ms(Car):
    def __init__(self, name, msg):
        super().__init__(name)      # 자식생성자 없으면 자동으로 부모생성자 호출
        self.autodrive = msg    # 자식생성자 명시시 부모생성자는 super()로 호출

    def say(self):
        print(self.cname + ' Wing.')
        print(self.cname + ' Mach Speed.')

    def dp(self):
        print(self.cname, self.engine, self.autodrive)

def main():
    li = []
    while True:
        select = int(input('1. 구글, 2. ms, 3. 조회, 4. 종료 : '))

        if select == 1:
            print('구글차를 만듭니다.')
            cname = input('자동차 이름 : ')
            pattern = input('주행 패턴 : ')
            li.append(google(cname, pattern))
        elif select == 2:
            print('MS를 만듭니다.')
            cname = input('자동차 이름 : ')
            pattern = input('주행 패턴 : ')
            li.append(ms(cname, pattern))
        elif select == 3:
            for i in li:
                # print(i.cname, i.autodrive)
                i.dp()
                i.say()
        elif select == 4:
            print('종료')
            break

if __name__ == '__main__':  # 이 파일이 실행될 때 이 라인이 참  # 참조될 때는 거짓
    # print(__name__)
    # g1 = google('Google Car', 'Fast')
    # g1.dp()
    # g1.say()
    #
    # m1 = ms('MS Car', 'Fly')
    # m1.dp()
    # m1.say()
    #
    Car.RGB_signal()
    Car.secret_view()
    main()



