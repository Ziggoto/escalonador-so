from PIL import Image, ImageDraw, ImageFont
from processo import Processo
from cores import Cores

import os.path
import io
import base64

class Caixa:
    width = 30
    height = 30
    
    def __init__(self, dr, pos, processo):
        self.dr = dr
        self.pos = pos
        self.x, self.y = pos
        self.processo = processo
        
        nova_pos = ((self.x, self.y), (self.x + Caixa.width, self.y + Caixa.height))
        dr.rectangle(nova_pos, fill="white", outline="black")
        
        dr.text((self.x + Caixa.width/3, self.y + Caixa.height/3), processo, fill="black")

class Desenho():
    
    def __init__(self, cores=Cores(), algoritimo="", fila_aptos = []):
        self.tamanho_fila = len(fila_aptos)
        self.tamanho_fonte = 12
        self.max_filas = 37 #Calculado a partir de muitas e muitas tentativas
        self.isFilaPrioridade = True if algoritimo == "Fila de Prioridade com RoundRobin" else False
        
        self.multiplicador = 4 if self.isFilaPrioridade else 1
        tamanho_multiplicador = 10 if self.multiplicador == 4 else 1 #Gambiarra
        
        self.x = 1200
        self.y = (130 + self.tamanho_fonte + (self.tamanho_fila / self.max_filas + 1)  * Caixa.height * tamanho_multiplicador)
        
        self.im = Image.new('RGB', (self.x, self.y), "white")
        self.dr = ImageDraw.Draw(self.im)
        
        #print "Chegou ate aqui..."
        fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'FreeSansBold.ttf')
        self.fonte = ImageFont.truetype(fn, self.tamanho_fonte)
        self.fonte_titulo = ImageFont.truetype(fn, 22)
        self.dr.setfont(self.fonte)
        
        self.quantum = 1
        self.algoritimo = algoritimo
        self.cores = cores
        self.fila_aptos = fila_aptos
        
    def draw(self):
        dr = self.dr
        
        dr.text((5, 5), "Quantum: "+str(self.quantum), fill="black")
        dr.text((self.x/2, 5), self.algoritimo, fill="black", font=self.fonte_titulo)
        dr.text((30, 35+self.tamanho_fonte), "Cores:", fill="black")
        
        #Desenha os cores
        pos = 0
        for i in self.cores.cores:
            if(i == None):
                Caixa(dr, (35+pos*Caixa.width, 60), " ")
            else:
                Caixa(dr, (35+pos*Caixa.width, 60), str(i))
            pos += 1
        
        dr.text((30, 70+Caixa.height), "Fila de aptos:", fill="black")
        
        m = self.max_filas #37
        
        #Desenha a fila de aptos
        fila = [self.fila_aptos] if not self.isFilaPrioridade else self.fila_aptos
        for k in range(self.multiplicador):
            tamanho = len(fila[k])
            for i in range(tamanho/m + 1):
                if tamanho < m:
                    aux = tamanho
                else:
                    aux = m
                    tamanho -= m
                
                cont = 0
                for j in range(aux):
                    Caixa(dr, (30+j*Caixa.width, (105 + 35 * k * 2) + self.tamanho_fonte+i*30), str(fila[k][cont]))
                    cont += 1
        
        self.quantum += 1
        
        #Salva a imagem
        output = io.BytesIO()
        self.im.save(output, format='JPEG')
        binary = output.getvalue()
        encoded = base64.b64encode(binary)
        return encoded
        
        