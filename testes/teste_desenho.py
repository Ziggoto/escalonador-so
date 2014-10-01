from PIL import Image
from arbitro.fifo import FIFO
from arbitro.prioridade import FilaPrioridade

import base64
import io


f = FilaPrioridade(processos_aptos=256)
d = f.draw_img()

binary =  base64.b64decode(d)

output = io.BytesIO(binary)
img = Image.open(output)
img.save("teste.png", format='PNG')