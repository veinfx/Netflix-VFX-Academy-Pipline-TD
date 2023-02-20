from faker import Faker


# 모듈 안에서 Faker 라는 class 를 가져 와라 즉, faker. 생략 가능

class MyFaker:
    def __init__(self):
        self.fake = Faker('ko_KR')
        Faker.seed()

    def get_name(self):
        name = self.fake.name()
        return name

    def get_email(self):
        email = self.fake.free_email()
        return email

    def get_addr(self):
        addr = self.fake.address()
        return addr


def main(self=None):
    user = MyFaker()
    print(
        user.get_name()
    )


if __name__ == "__main__":
    main()
