class MeuObjeto:
    def __init__(self):
        self.propriedade = "valor"


def test_propriedade_de_objeto():
    objeto = MeuObjeto()
    assert objeto.propriedade == "valor"
