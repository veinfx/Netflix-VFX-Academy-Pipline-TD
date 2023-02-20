from pymongo import MongoClient

class User:
    first_name = None
    last_name = None
    K_name = None
    email = None
    phone = None
    address = None
    gender = None
    department = None
    activate = True

    def __init__(self, **kwargs):
        print(kwargs)
        # for arg in kwargs:

        pass

    def value(self):
        return {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "k_name" : self.k_name,
            "email" : self.email,
            "phone" : self.phone,
           "address" : self.address,
            "gender" : self.gender,
            "department" : self.department,
            "activate" : self.activate,
        }

class MongoAPI:
    ip = "192.168.3.116"
    port = 27017
    client = None
    _db = None
    _collection = None

    def __init__(self):
        client = MongoClient(self.ip, self.port)
        print("Mongo Enter")

    def __del__(self):
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
        self._db = self.client[value]

    @property
    def collection(self):
        return self._collection

    @collection.setter
    def collection(self, value):
        if self.db is None:
            raise Exception("DB is not exists.")
        self._collection = self.db[value]

    def add_user(self, value):
        if not value:
            raise Exception("no value")

        email = value["email", None]
        if email is None:
            raise Exception("no email")

        userexist = self.get_user(email)

        if userexist:
            raise Exception("user already exists")      #raise는 그냥 종료되니까 나중에 error return 다른 걸로 바꿀것.

        result = self.collection.insert_one(value)
        return result

    def get_user(self, value):
        result = self.collection.find_one({'email' : value})
        return result

    def update_user(self, value):
        result = self.collection.update_one({'email': value['email']},{"$set":value})
        return result

    def delete_user(self, value):
        result = self.collection.delete_one({'email': value['email']}, {"$set":value['email']})
        return result

def main():

    mong = MongoAPI()
    mong.db = 'avata2'
    mong.collection = 'act'
    # result = mong.add_user(new_user)
    # print(result)

    # print(mong)
    # print(mongo.db)
    # print(mong.collection)

    new_user = {
        "first_name": "sam",
        "last_name": "Worthington",
        "K_name": "샘 워딩턴",
        "email": "sam@avata.com",
        "phone": 1234-1234,
        "address": None,
        "gender": None,
        "department": None,
        "activate": None
    }



    # result = mong.add_user(new_user)
    # print(result)
    # print(mong.collection)

    result = mong.get_user('sam@avata.com')
    print(result)
    # new_user = User(first_name="sungwoo", last_name="park")
    # print(new_user.value)

    # result = mong.update_user((new_user))
    # print(result)

if __name__ == "__main__":
    main()