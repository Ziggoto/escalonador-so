from PIL import Image, ImageDraw, ImageFont

class Caixa:
    
    def __init__(self, dr, pos, texto):
        self.dr = dr
        self.pos = pos
        self.x, self.y = pos
        self.texto = texto
        
        self.width = 30
        self.height = 30
        
        nova_pos = ((self.x, self.y), (self.x + self.width, self.y + self.height))
        dr.rectangle(nova_pos, fill="white", outline="black")
        
        dr.text((self.x + self.width/3, self.y + self.height/3), self.texto, fill="black")

class Desenho():
    
    def __init__(self, cores=4, algoritimo="", tamanho_fila=20,size=(1200, 350)):
        self.size = size
        self.x, self.y = size
        self.im = Image.new('RGB', self.size, "white")
        self.dr = ImageDraw.Draw(self.im)
        self.tamanho_fonte = 12
        
        self.fonte = ImageFont.truetype("FreeSansBold.ttf", self.tamanho_fonte)
        self.fonte_titulo = ImageFont.truetype("FreeSansBold.ttf", 22)
        self.dr.setfont(self.fonte)
        
        self.quantum = 1
        self.algoritimo = algoritimo
        self.cores = cores
        self.tamanho_fila = tamanho_fila
        
    def draw(self):
        dr = self.dr
        
        dr.text((5, 5), "Quantum: "+str(self.quantum), fill="black")
        dr.text((self.x/2, 5), self.algoritimo, fill="black", font=self.fonte_titulo)
        dr.text((30, 35+self.tamanho_fonte), "Cores:", fill="black")
        
        for i in range(self.cores):
            Caixa(dr, (30+i*30, 60), str(i+1))
        
        dr.text((30, 100), "Fila de aptos:", fill="black")
        
        m = 37 #Calculado a partir de muitas e muitas tentativas
        
        for i in range(self.tamanho_fila/m + 1):
            if self.tamanho_fila < m:
               aux = self.tamanho_fila
            else:
                aux = m
                self.tamanho_fila -= m
            
            for j in range(aux):
                Caixa(dr, (30+j*30, 100+self.tamanho_fonte+i*30), str(j+1))
                
        self.im.save("../static/escalonador.png")        
        self.quantum += 1
        

d = Desenho(tamanho_fila=50)
d.draw()