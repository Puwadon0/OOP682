# ISP: การแยกอินเทอร์เฟซ
# "ไม่ควรบังคับให้ Client พึ่งพาเมธอดที่พวกเขาไม่ได้ใช้งาน" (อย่าทำ Interface ที่เทอะทะ) [9]


class Machine:
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def fax(self, document):
        pass


class OldPrinter(Machine):
    def print(self, document):
        print("Printing Document... ")

    def scan(self, document):
        raise NotImplementedError("This printer cannot scan.. ")

    def fax(self, document):
        raise NotImplementedError("This printer cannot fax.. ")
