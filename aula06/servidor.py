from controller.servidor_controller import ServidorController
from view.servidor_view import ServidorView

HOST = "0.0.0.0"
PORTA = 5000


if __name__ == "__main__":
    ServidorController(HOST, PORTA, ServidorView()).executar()
