from PIL import Image, ImageDraw, ImageFont
from processo import Processo
from cores import Cores

import os.path

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
        
        self.x = 1200
        self.y = (130 + self.tamanho_fonte + (self.tamanho_fila / self.max_filas + 1)  * Caixa.height * self.multiplicador)
        
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
                Caixa(dr, (35+pos*30, 60), " ")
            else:
                Caixa(dr, (35+pos*30, 60), str(i))
            pos += 1
        
        dr.text((30, 100), "Fila de aptos:", fill="black")
        
        m = self.max_filas 
        
        #Desenha a fila de aptos
        fila = [self.fila_aptos] if not self.isFilaPrioridade else self.fila_aptos
        print fila
        for k in range(self.multiplicador):
            for i in range(self.tamanho_fila/m + 1):
                if self.tamanho_fila < m:
                    aux = self.tamanho_fila
                else:
                    aux = m
                    self.tamanho_fila -= m
                
                cont = 0
                for j in range(len(fila[k])):
                    Caixa(dr, (30+j*30, (105 + 35 * k) + self.tamanho_fonte+i*30), str(fila[k][cont]))
                    cont += 1
                
        self.im.save("../static/escalonador.png")        
        self.quantum += 1