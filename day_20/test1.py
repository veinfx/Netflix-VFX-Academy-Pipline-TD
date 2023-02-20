import pymongo
from pymongo import MongoClient


class User:
    first_name = None
    last_name = None
    k_name = None
    email = None  # (uuid로 사용해보기)
    phone = None
    address = None
    gender = None
    department = None
    activate = True

    def __init__(self, **kwargs):
        print(kwargs)
        pass

    def value(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "k_name": self.k_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "gender": self.gender,
            "department": self.department,
            "activate": self.activate
        }


class MongoAPI:
    ip = "192.168.3.116"
    port = 27017
    client = None
    _db = None
    _collection = None
    update_user = None

    def __init__(self):
        self._db = None
        self.client = MongoClient(self.ip, self.port)
        print("Mongo Enter")

    def __del__(self):  # 접속하면 안정성을 위해 닫아야 한다.
        if self.client:
            self.client.close()
            print("Mongo closed.")

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, value):
        if self.client is None:
            raise Exception("Client is not exists.")
        self._db = self.client[value]  # client가 [DB이름]을 적는다. 없으면 생성.

    @property
    def collection(self):
        return self._collection

    @collection.setter
    def collection(self, value):
        if self.db is None:
            raise Exception("DB is not exists")
        self._collection = self.db[value]

    def add_user(self, value):
        if not value:
            raise Exception("Noooooo")

        email = value.get("email", None)        # == value.["email"]
        if email is None:
            raise Exception("no email")

        isused = self.get_user(email)
        if isused:
            raise Exception("user already exists")      #raise는 그냥 종료되니까 나중에 error return 다른 걸로 바꿀것.
        result = self.collection.insert_one(value)
        return result

    def get_user(self, value):
        result = self.collection.find_one({'email': value})
        return result

    def update_user(self, value):
        result = self.collection.update_one({'email': value['email']}, {"$set": value})
        return result

    def delete_user(self, value):
        result = self.collection.delete_one({'email': value['email']}, {"$set": value['email']})
        return result

def main():
    mongpi = MongoAPI()
    mongpi.db = 'yjtestyj'
    mongpi.collection = 'mytestmy'
    new_user = {
        "first_name": 'yoonju',
        "last_name": 'Park',
        "k_name": 'updatetest_박윤주',
        "email": 'updateplease@gmail.com',
        "phone": None,
        "address": None,
        "gender": None,
        "department": None,
        "activate": True
    }
    # result = mongpi.add_user(new_user)
    # print(mongpi)
    # print(mongpi.collection)

    # result = mongpi.add_user(new_user)
    # print(result)

    # result = mongpi.get_user('updateplease@gmail.com')
    # print(result)

    result = mongpi.update_user({
            "first_name": 'sunjun',
            "last_name": 'Park',
            "k_name": 'updatetest_박윤주',
            "email": 'updateplease@gmail.com',
            "phone": None,
            "address": None,
            "gender": None,
            "department": None,
            "activate": True
        })
    print(result)

    # result = mongpi.delete_user(new_user)
    # print(result)

if __name__ == "__main__":
    main()