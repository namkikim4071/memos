Factory Pattern
 - Factory를 통한 오브젝트생성

Factory Method Pattern
 - Factory를 통한 오브젝트생성
 - Factory내에 메소드가 존재

Abstract Factory Pattern


Sigleton Pattern
 - 하나의 프로세스내에서 하나의 오브젝트만 관리
 - 데이터 오브젝트와 같이, 메모리 사용이 높으면서 재사용이 가능한 오브젝트 또는 네트워크 연결이 1개일때


Composite Pattern
 - 트리.... 구조를 갖는 패턴

Stretegy Pattern
 - runtime 해동을 정한다.
 - 함수에 Cat을 넣으면, Dog를 넣으면 그 객체에 따라 동작한다.
   ㄴ OOP, OCP

State Pattern
 - 신호등과 같이 상태를 확장가능하게 할 수 있는 패턴
 - 신호등간의 상태가 확인할 수 있다. (Stretegy 패턴과 다른점)

Command Pattern
 - 여래개의 명령을 오브젝트로 관리하여, 쉽게 실행할 수 있는 구조 만들기
 - 예시
   baduk = Dog()
   dog_command = DogCommand(baduk, ['stay', 'sit', 'sit'])

   invoke( ) <-- dog_command 실행, 명령어의 모음을 담고, 모두 실행한다.


Chain of Responsibility (책임 체인 패턴, 책임 연쇄 패턴)
 - Payment (결재방법: 현금, 신용카드, 체크카드...)
 - handler ...
   ㄴ 체인으로 묶음!
   ㄴ 내가 아니면, 다음 핸들러에게 넘김
 - Linked List 구조


Observer Pattern (감시자 패턴)
- 감시자들이 이벤트를 바라보다가 실행, .... Subscriber, Listener <---> polling

    Observer Interface
    Update()

    Observer1 Observer2
    Update

    Event
    ob1, ob2, ob2 : List 형태
    addObserver()
    notify() : Observer의 update 실행

    Observer <--- Observer 패턴도 가능

Visitor Pattern
  cat
    speak()
    home()
    age()
    accept() <--- 새로운 함수의 기능을 visitor에 넘김
                  ㄴ 이름, 나이를 출력해주는 기능을 넘긴다.

  named Tuple -> f(x) 넣는다.



SOLID
1) Single Responsibility
 - 모듈, 클래스, 메소드는 하나의 책임(기능)만 갖는다.

def add(num1, num2):
    return num1 + num2

def num_print(num):
    print(num)

def add_print(num1, num2): #두가지 책임을 갖는다.
    print(num1 + num2)


2) Open-closed principle
 - 확장은 오픈, 수정은 폐쇄

class Animal:
    def __init__(self, a_type):
        self.a_type = a_type

def hey(animal: Animal):
    if animal.a_type == 'Cat':
        print("meow")
    elif animal.a_type == 'Dog':
        print("bark")
    else:
        raise Exception("Wrong a_type")

kitty = Animal("Cat")
bingo = Animal("Dog")

hey(kitty)
hey(bingo)

## Cow, Sheep
cow = Animal("Cow")
sheep = Animal("Sheep")
hey(cow) #Exception
hey(sheep) #Exception

class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("meow")

class Dog(Animal):
    def speak(self):
        print("bark")

class Sheep(Animal): #Opne
    def speak(self):
        print("meh")

def hey(animal: Animal): #closed
    animal.speak()

kitty = Cat()
bingo = Dog()
sheep = Sheep()

# 동물이 늘어나도 hey함수는 수정할 일이 없다!


3) Liskov Substitution (리스코프 치환 원칙)

T
ㄴ ㄴ ㄴ
SubT1 SubT2 SubT3

T <-- SubT1 SubT2 SubT3 로 바꿔도 우리가 생각한 대로 동작한다.

class Cat:
    def speak(self):
        print("meow")

class BlackCat(Cat):
    def speak(self):
        print("black meow")

def speak(cat: Cat):
    cat.speak()

cat: Cat = Cat() #치환이 가능
speak(cat)
# meow
cat: Cat = BlackCat() #치환이 가능
speak(cat)
# black meow

class Fish(Cat):
    def speak(self):
        raise Exception("Fish cannot speak")  <--- 리스코프 치환에 위배된다.

cat = Fish()
speak(cat) <--- Exception 발생, 리스코프 치환에 위배된다.
##리스코프 치환의 원칙을 지키려면, Fish와 같이 포함할 수 없는 구조를 먼저 개선해야 한다.


4) Interface Segregation (인터페이스 분리원칙)
 - 클라이언트가 사용하지 않는 메소드를 의존하게 만들지 않는다.
 - 큰 인터페이스를 더 작은 인터페이스로

class ICar(abc): #<--너무 큰 개념으로 잡지마라!
    def drive(self):
        pass

    def trunLeft(self):
        pass

    def turnRight(self):
        pass

class Genesis(ICar):
    def drive(self):
        pass

    def trunLeft(self):
        pass

    def turnRight(self):
        pass

class Avante(ICar):
    def drive(self):
        pass

    def trunLeft(self):
        pass

    def turnRight(self):
        pass

nocopeCar = Avante()
secondCar = Genesis()


class ICarBoat(abc): #<--너무 큰 개념으로 잡으면??
    def drive(self):
        pass

    def trunLeft(self):
        pass

    def turnRight(self):
        pass

    def steer(self):
        pass

    def steerRight(self):
        pass

    def steerRight(self):
        pass

class Genesis(ICarBoat):
    def drive(self):
        pass

    def trunLeft(self):
        pass

    def turnRight(self):
        pass

    # def steer(self): #사용하지 않는 메소드가 생김!
    #     pass

    # def steerRight(self):
    #     pass

    # def steerRight(self):
    #     pass



5) Dependency Inversion

Zoo (High Level)
ㄴ Cat (Low Level)
ㄴ Dog
ㄴ Sheep
ㄴ Cow

* Zoo에 Cat, Dog ...의 Dependency가 존재함
* Zoo에 계속 동물이 추가된다면? 코드의 어려움이 발생함.

Zoo --> Animal (추상화모듈) <- Cat, Dog
                          ㄴ 의존성 역전

class Zoo: <-- Zoo를 변경이 없음
    def __init__(self)
        self.animals = []

    def addAnimal(self, animal: Animal): <--의존성역전
        self.animals.append(animal)

    def speekAll(self):
        for animal in animals:
            animal.speak()

class Zoo:
    def __init__(self)
        self.cat = Cat()
        self.dog = Dog()
        ...

    def speekAll(self):
        self.cat.speak() ...



데코레이터?


질문)

1) 이터레이터, 제너레이너

이터러블 -> 이터레이터
    iter()

이터러블 객체가 되려면, 2개의 메소드
__iter__() : 이터러블 객체 자신을 반환
__next__() : 다음 반복을 위한 값 반환, 더이상 업승면 StopIteration 예외발생
** __inter__ : 이터러블 for in 구문, __next__ : 이터레이터로 구부할 수 있음.

class Counter:
    def __init__(self, low, high):
        self.low = ow

    def __iter__
        return self

    def ___next__
        if lower > hight:
            raise StopIteration
        else:
            ..

제너레이터
- yield : 순차적으로 실행한다.
- yield 를 사용해서 생성한 객체 또는 함수

for word in myGennerator():
    print(word)

def CounerGen ()
    whle lower < :
    yield lower


2) dataclass
 ㄴ 데이터클레스
 ㄴ 데이터기반, 중심.... 데이터클래스

파이썬 3.7부터 dataclass라는 모듈이 추가되었다.
말 그대로 데이터를 담는 클래스이고, import 후에 @dataclass 라는 데코레이터를 사용하면 된다.


3) 데코레이터


4) 컨텍스트 관리자
__enter__
__exit__

5) 컨테이너 객체
__contains__

6) 시퀀스
__len__
__getitem__

__getatt__ : 동적속성 조회

__call__ : 호출형 객체



TDD
테스트주도개발
...

