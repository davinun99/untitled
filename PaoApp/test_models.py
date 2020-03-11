from .models import Usuario

class TestModels:
    def test_usuario(self):
        usuario = Usuario("user1","Ulises Suario","user1@hotmail.com","12345abdce")
        assert usuario.nombre_usuario == "user1"
        assert usuario.nombre_real == "Ulises Suario"
        assert  usuario.email == "user1@hotmail.com"
        assert  usuario.contrasegna == "12345abdce"
