class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, amount):
        self.salary += amount
        print(f"{self.name}의 연봉이 {self.salary}으로 증가되었습니다.")

kim = Employee("Kim", 5000)
lee = Employee("Lee", 6000)

print(f"{kim.name}의 연봉은 {kim.salary}입니다.") #클래스 밖에서 객체의 속성에 접근할 때는 self라는 이름 쓸수 없음. 외부에서는 인스턴스 이름을 직접 써야함
print(f"{lee.name}의 연봉은 {lee.salary}입니다.")

kim.raise_salary(2000)
kim.raise_salary(1000)