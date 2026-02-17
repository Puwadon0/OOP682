# Single Responsibility Principle (SRP)
# หนึ่งคลาสควรมีเหตุผลเดียวในการเปลี่ยนแปลง (หน้าที่เดียว) [6]
class PDFReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate_pdf(self):
        pass

    def generate_excel(self):
        pass

    def send_email(self):
        pass


class ExcelReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
        pass


class EmailSendder:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self, report):
        pass
