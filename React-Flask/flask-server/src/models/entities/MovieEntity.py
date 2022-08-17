
from utils.DateFormat import DateFormat


class Movie():
    # somente a id eh obriagatoria, quando colocamos os outros campos = None
    def __init__(self, id,
                 title=None,
                 duration=None,
                 released=None
                 ) -> None:
        self.id = id
        self.title = title
        self.duration = duration
        self.released = released

# Define o formato da resposta JSON que aparece no navegador, consumido em 'models'

    def to_JSON(self):
        return{
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'released': DateFormat.convert_date(self.released)
        }
