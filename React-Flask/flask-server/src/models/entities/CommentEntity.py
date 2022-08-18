
from utils.DateFormat import DateFormat


class Comment():
    # somente a id eh obriagatoria, quando colocamos os outros campos = None
    def __init__(self, id,
                 username=None,
                 text=None
                 ) -> None:
        self.id = id
        self.username = username
        self.text = text

# Define o formato da resposta JSON que aparece no navegador, consumido em 'models'

    def to_JSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'text': self.text
        }
