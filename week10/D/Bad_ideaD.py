# Dependency Inversion Principle (DIP): การกลับด้านความขึ้นต่อกัน
# โมดูลระดับสูงไม่ควรขึ้นกับโมดูลระดับต่ำ ทั้งคู่ควรขึ้นอยู่กับ Abstractions (นามธรรม) [10]


class App:
    def __init__(self):
        self.database = MySQLDatabase()

    def save_data(self, data):
        self.database.save(data)


class MySQLDatabase:
    def save(self, data):
        print("Saving data to MYSQL database...")


app = App()
app.save_data("Some important data")
