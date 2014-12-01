class Cores:
    
<<<<<<< HEAD
    def __init__(self, memoria, max=4):
        self.max = max
        self.cores = []
        self.memoria = memoria
=======
    def __init__(self, max=4):
        self.max = max
        self.cores = []
>>>>>>> 9d85dfde7b76008f6842309b231b3b9009670490
        
        for i in range(self.max):
            self.cores.append(None)
    
    def add_process(self, process):
        for i in range(len(self.cores)):
            if self.cores[i] is None:
                self.cores[i] = process
                return True
        return False
    
    def rm_process(self, process):
        if self.is_number(process) and self.is_valid_position(process):
            self.cores[process] = None
        else:
            for i in range(self.max):
                if self.cores[i] == process:
                    self.cores[i] = None
                    break
<<<<<<< HEAD

    def is_processing(self, processo):
        for i in self.cores:
            if i == processo:
                return True
        return False
=======
>>>>>>> 9d85dfde7b76008f6842309b231b3b9009670490
    
    def is_number(self, variable):
        if type(variable) == type(1):
            return True
        return False
    
    def is_valid_position(self, number):
        if number <= (len(self.cores) - 1):
            return True
        return False
    
    def is_full(self):
        for i in range(self.max):
            if self.cores[i] == None:
                return False
        return True
    
    def is_empty(self):
        if len(set(self.cores)) == 1 and self.cores[0] is None:
            return True
        else:
            return False
    
    def get_empty_cores(self):
        lista = []
        for i in self.cores:
            if i == None:
                lista.append(i)
        return lista
       
    # Diminui o tempo restante dos processos
    def processa(self):
        p = None
        for i in range(self.max):
            p = self.cores[i]
            if p == None:
                pass
            elif p.tempo_restante is not None and p.tempo_restante > 1:
                p.tempo_restante -= 1
                p.tempo_processando += 1
            else:
<<<<<<< HEAD
                #Desaloca a memoria:
                self.memoria.dealloc(self.cores[i])
                #Aqui mata o processo:
=======
>>>>>>> 9d85dfde7b76008f6842309b231b3b9009670490
                self.cores[i] = None
        return True