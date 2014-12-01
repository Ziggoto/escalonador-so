from PIL import Image, ImageDraw, ImageFont
from processo import Processo
from cores import Cores

import os.path
import io
import base64

class Caixa:
    width = 80
    height = 50
    
    def __init__(self, dr, pos, processo, cor="white"):
        self.dr = dr
        self.pos = pos
        self.x, self.y = pos
        self.processo = processo
        
        fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'FreeSansBold.ttf')
        fonte_caixa = ImageFont.truetype(fn, 11)
        
        nova_pos = ((self.x, self.y), (self.x + Caixa.width, self.y + Caixa.height))
        dr.rectangle(nova_pos, fill=cor if processo is not None else "white", outline="black")
        
        #dr.text((self.x + Caixa.width/3, self.y + Caixa.height/3), processo, fill="black")
        
        #Solucao porca:
        if processo is not None:
            dr.text((self.x+2, self.y+2), "PID: "+str(processo.pid), fill="black", font=fonte_caixa)
            dr.text((self.x+2, self.y+10), "Tempo R.: "+str(processo.tempo_restante), fill="black", font=fonte_caixa)
            dr.text((self.x+2, self.y+10*2), "Tempo T.: "+str(processo.tempo_necessario), fill="black", font=fonte_caixa)
<<<<<<< HEAD
            dr.text((self.x+2, self.y+10*3), "Memo.: "+str(processo.memoria_necessaria), fill="black", font=fonte_caixa)
=======
            dr.text((self.x+2, self.y+10*3), "Priori.: "+str(processo.prioridade), fill="black", font=fonte_caixa)
>>>>>>> 9d85dfde7b76008f6842309b231b3b9009670490

class Desenho():
    
    def __init__(self, escalonador):
        fila = escalonador.aptos if escalonador.algoritimo != "Fila de Prioridade com RoundRobin" else escalonador.filas
        self.quantum = escalonador.quantum
        self.algoritimo = escalonador.algoritimo
        self.cores = escalonador.cores
<<<<<<< HEAD
        self.RAM = escalonador.memoria.RAM
=======
>>>>>>> 9d85dfde7b76008f6842309b231b3b9009670490
        self.fila_aptos = fila
        
        self.tamanho_fila = len(self.fila_aptos)
        self.tamanho_fonte = 12
        self.isFilaPrioridade = True if self.algoritimo == "Fila de Prioridade com RoundRobin" else False
        
        self.multiplicador = 4 if self.isFilaPrioridade else 1
        tamanho_multiplicador = 10 if self.multiplicador == 4 else 1 #Gambiarra
        
        self.x = 1200
        
        self.max_filas = (1200 / Caixa.width) - 2 #Calculado a partir de muitas e muitas tentativas
        self.y = (130 + self.tamanho_fonte + (self.tamanho_fila / self.max_filas + 1) \
<<<<<<< HEAD
                   * Caixa.height * tamanho_multiplicador) + 100
=======
                   * Caixa.height * tamanho_multiplicador)
>>>>>>> 9d85dfde7b76008f6842309b231b3b9009670490
        
        self.im = Image.new('RGB', (self.x, self.y), "white")
        self.dr = ImageDraw.Draw(self.im)
        
        #print "Chegou ate aqui..."
        fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'FreeSansBold.ttf')
        self.fonte = ImageFont.truetype(fn, self.tamanho_fonte)
        self.fonte_titulo = ImageFont.truetype(fn, 22)
        
        self.dr.setfont(self.fonte)
        
    def draw(self):
        dr = self.dr
        
        dr.text((5, 5), "Quantum: "+str(self.quantum), fill="black")
        dr.text((self.x/2, 5), self.algoritimo, fill="black", font=self.fonte_titulo)
        dr.text((30, 35+self.tamanho_fonte), "Cores:", fill="black")
        
        #Desenha os cores
        pos = 0
        for i in self.cores.cores:
            if(i == None):
                Caixa(dr, (35+pos*Caixa.width, 60), None, "#00FF00")
            else:
                Caixa(dr, (35+pos*Caixa.width, 60), i, "#00FF00")
            pos += 1
<<<<<<< HEAD

        #Desenha a Memoria Virtual
        blocos_ram = len(self.RAM.pos)
        pos_inicial = 70+Caixa.height
        dr.text((30, pos_inicial), "Memoria Virtual (RAM):", fill="black")
        #dr.text((blocos_ram * Caixa.width + 60, pos_inicial), "Disco:", fill="black")

        for pos in range(blocos_ram):
            Caixa(dr, (35+pos*Caixa.width, pos_inicial+15), self.RAM.pos[pos].conteudo, "#FFFFFF")
            tamanho = self.RAM.pos[pos].tamanho
            dr.text(((35+pos*Caixa.width)+(Caixa.width / 3.), pos_inicial+15+Caixa.height+5), str(tamanho)+"KB", fill="black")

        pos_inicial += 40 + Caixa.height
        dr.text((30, pos_inicial), "Fila de aptos:", fill="black") #Ta certo...
        
        m = self.max_filas

=======
        
        pos_inicial = 70+Caixa.height
        dr.text((30, pos_inicial), "Fila de aptos:", fill="black") #Ta certo...
        
        m = self.max_filas
        
>>>>>>> 9d85dfde7b76008f6842309b231b3b9009670490
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
                    Caixa(dr, (30+j*Caixa.width, 
                        ((pos_inicial + 5) + 35 * k * 2) \
                                + self.tamanho_fonte+i*Caixa.height), fila[k][cont], "#FF5252")
                    cont += 1
        
        self.quantum += 1
        
        #Salva a imagem
        output = io.BytesIO()
        self.im.save(output, format='JPEG')
        binary = output.getvalue()
        encoded = base64.b64encode(binary)
<<<<<<< HEAD
        return encoded
=======
        return encoded
        
        
>>>>>>> 9d85dfde7b76008f6842309b231b3b9009670490
