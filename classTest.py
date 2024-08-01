


class Student:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def __call__(self, score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        else:
            return "C"











if __name__ == "__main__":

    john = Student(1, 'john','new york')
    # print(john.__dict__)
    grade = john(90) # 90 출력
    print(grade)