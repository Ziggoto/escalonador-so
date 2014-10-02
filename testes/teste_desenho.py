from PIL import Image
from arbitro.fifo import FIFO
from arbitro.prioridade import FilaPrioridade
from arbitro.round_robin import RoundRobin

import base64
import io


f = RoundRobin(processos_aptos=20)

f.executa()
f.executa()
f.executa()
f.executa()
f.executa()
d = f.draw_img()


binary =  base64.b64decode(d)
output = io.BytesIO(binary)
img = Image.open(output)
img.save("teste.png", format='PNG')