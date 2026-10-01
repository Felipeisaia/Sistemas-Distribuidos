from controller.cliente_controller import ClienteController
from view.cliente_view import ClienteView

HOST_SERVIDOR = "127.0.0.1"
PORTA_SERVIDOR = 5000


if __name__ == "__main__":
    ClienteController(HOST_SERVIDOR, PORTA_SERVIDOR, ClienteView()).iniciar()
