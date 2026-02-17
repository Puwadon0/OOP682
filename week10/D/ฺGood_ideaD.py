# Dependency Inversion Principle (DIP): การกลับด้านความขึ้นต่อกัน
# โมดูลระดับสูงไม่ควรขึ้นกับโมดูลระดับต่ำ ทั้งคู่ควรขึ้นอยู่กับ Abstractions (นามธรรม) [10]
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class MySQLDatabase(Database):
    def save(self, data):
        print("Saving data to MYSQL database...")


class PostgresSQLDatabase(Database):
    def save(self, data):
        print("Saving data to PostgreSQL database...")


class App:
    # พึ่งพา Abstraction
    def __init__(self, database: Database):
        self.database = database


# ส่งสิ่งที่ต้องใช้เข้าไป (Injection)
app = App(MySQLDatabase())
app = App(PostgresSQLDatabase())
