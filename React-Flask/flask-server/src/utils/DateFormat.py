import datetime

class DateFormat():

    # FORMATAR FORMATO DE DATA
    @classmethod
    def convert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')
