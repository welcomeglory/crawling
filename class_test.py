

class Person:

    def __init__(self, name, address,phone,pay):
        self.name = name
        self.address = address
        self.phone = phone
        self.pay = pay

    def raise_pay(self):
        self.pay = self.pay*(1+0.1)
        return self.pay







if __name__ == "__main__":
    person = Person('john', '서울시', '010-1111-2222',3000)
    #print(person.__dict__)
    #person.raise_pay()
    #print(person.__dict__)
    print(person.raise_pay())
    print(person.pay) # 변한 속성값 가져옴
