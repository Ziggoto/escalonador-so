class Cores:
    
    def __init__(self, max=4):
        self.max = max
        self.cores = []
        
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
       
    # Diminui o tempo restante dos processos
    def processa(self):
        p = None
        for i in range(self.max):
            p = self.cores[i]
            if p.tempo_restante > 1 and p.tempo_restante is not None:
                p.tempo_restante -= 1
            else:
                self.cores[i] = None
