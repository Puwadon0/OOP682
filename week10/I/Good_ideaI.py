# ISP: การแยกอินเทอร์เฟซ
# "ไม่ควรบังคับให้ Client พึ่งพาเมธอดที่พวกเขาไม่ได้ใช้งาน" (อย่าทำ Interface ที่เทอะทะ) [9]

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self, document):
        print("Printing document...")

    def scan(self, document):
        print("Scanning document...")

    def fax(self, document):
        print("Faxing document...")
