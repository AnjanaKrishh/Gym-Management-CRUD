from mysql import connector
import datetime
class DbConnect:
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Anjana#@!123",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None

class GymMemberManager(DbConnect):
    def get_object(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM member WHERE id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None
    def get(self):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "select * from member"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "insert into member(name,place,mobile,plan,fee,joined_date)values(%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("New member added successfully")
        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "SELECT * FROM member WHERE id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            if record is None:
                print("Member not found")
                return None
            else:
                print(record)
                return record
        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "DELETE FROM member WHERE id=%s"
            self.cursor.execute(query, (id,))
            if self.cursor.rowcount > 0:
                self.connect.commit()
                print("Member deleted successfully")
            else:
                print("No member at this id")
                self.connect.rollback()
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k+"=%s"
                    placeholder=placeholder.rstrip(",")
                    query=f"update member set {placeholder} where id=%s"
                    values = [v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("Member details updated successfully")
            else:
                print("member not found")
        except Exception as e:
            print(e)



connection_instance = DbConnect()
print(connection_instance.get_connected())
member_instance = GymMemberManager()
# member_instance.get()
# member_instance.post(name="Sreerag",place="Kochi",mobile="6789054392",plan="2 Month",fee="1200",joined_date=datetime.datetime.today())

member_instance.get()
member_instance.retrieve(4)
# print(member_instance.retrieve())
# member_instance.retrieve(id=1)
member_instance.get()
member_instance.delete(7)
member_instance.put(id=3,place="Malapuram")
member_instance.get()


