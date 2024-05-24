import datetime

class Client:

    def __int__(self):
        self.name = ''
        self.sex = -1
        self.birthday = ''
        self.phone = ''
        self.tg_id = ''

    def get_age(self):
        bd = self.birthday.split('-')
        bd_date = datetime.date(int(bd[0]), int(bd[1]), int(bd[2]))
        today = datetime.date.today()
        age = today.year - bd_date.year - ((today.month, today.day) < (bd_date.month, bd_date.day))
        return age

tmpClient = Client()