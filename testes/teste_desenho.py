from PIL import Image
from arbitro.fifo import FIFO
from arbitro.prioridade import FilaPrioridade
from arbitro.round_robin import RoundRobin
<<<<<<< HEAD
from core.escalonador import Escalonador
from core.desenha import Desenho
=======
>>>>>>> 9d85dfde7b76008f6842309b231b3b9009670490

import base64
import io


<<<<<<< HEAD
escalonador = Escalonador()
desenho = Desenho(escalonador).draw()
binario = base64.b64decode(desenho)

img = open("teste.png", "wb")
img.write(binario)
img.close()
=======
f = RoundRobin(processos_aptos=256)

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
>>>>>>> 9d85dfde7b76008f6842309b231b3b9009670490
