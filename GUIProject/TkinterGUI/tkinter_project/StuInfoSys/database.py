import json


class MysqlDatabase:
    def __init__(self):
        with open("users.json", mode="r", encoding="utf-8") as f:
            self.users = json.load(f)
        with open("students.json", mode="r", encoding="utf-8") as f:
            self.students = json.load(f)

    def all(self):
        return self.students

    def check_login(self, username, password):
        user_correct = False
        pwd_correct = False
        for user in self.users:
            if username == user["username"] and password == user["password"]:
                print("login success")
                return True, "Success"
            else:
                if username == user["username"] and password != user["password"]:
                    return False, "password error"
                else:
                    pass
        return False, "the user does not exist"

    def insert(self, student: dict):
        self.students.append(student)

    def delete_by_name(self, name):
        for stu in self.students:
            if stu["name"] == name:
                self.students.remove(stu)
                return True, f"{name} delete success"
        return False, f"{name} does not exist"

    def search_by_name(self, name):
        for stu in self.students:
            if stu["name"] == name:
                return True, stu
        return False, f"{name} does not exist"

    def modify(self, student):
        for stu in self.students:
            if stu["name"] == student["name"]:
                stu.update(student)


db = MysqlDatabase()

if __name__ == '__main__':
    print(db.users)
    print(db.students)

    ret = db.check_login("admin", "123")
    print(ret)

    print(db.search_by_name("Sam"))
