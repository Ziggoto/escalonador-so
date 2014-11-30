from PIL import Image
from arbitro.fifo import FIFO
from arbitro.prioridade import FilaPrioridade
from arbitro.round_robin import RoundRobin
from core.escalonador import Escalonador
from core.desenha import Desenho

import base64
import io


escalonador = Escalonador()
desenho = Desenho(escalonador).draw()
binario = base64.b64decode(desenho)

img = open("teste.png", "wb")
img.write(binario)
img.close()
