# -*- coding: utf-8 -*-
__author__ = 'fabio'

import random
import math
import beans.bloco as bloco
import core.disco as disco

class MemoriaVirtual():

    def __init__(self, escalonador,tamanho=4):
        self.RAM = Memoria(tamanho)
        self.disco = disco.Disco(self.RAM.tamanho_pratico * 10)

        self.escalonador = escalonador

    def swap(self):
        '''
        Passa um processo da RAM para o Disco
        :param processo: Processo em questão
        :return: True ou False
        '''

        for i in self.RAM.pos:
            if not self.escalonador.cores.is_processing(i.conteudo):
                #Se nao tiver sendo processado...
                self.disco.malloc(i.conteudo)
                self.RAM.dealloc(i.conteudo)
                return True
        return False

    def reverse_swap(self, processo):
        '''
        Passa o processo do Disco para a RAM
        :param processo:
        :return: True ou False
        '''
        return False

    def malloc(self, processo):
        return self.RAM.malloc(processo)

    def dealloc(self, processo):
        return self.RAM.dealloc(processo)

    def is_full(self, processo):
        pos = self.RAM.pos
        for i in pos:
            if i.conteudo == None:
                return False
        return True

    def has_memory_for(self, processo):
        posicoes_vazias = self.get_empty_positions()

        for i in posicoes_vazias:
            if i.tamanho > processo.memoria_necessaria:
                return True

        aux = 0
        for i in posicoes_vazias:
            aux += i.tamanho
            if aux >= processo.memoria_necessaria:
                return True

        return False

    def is_in_memory(self, processo):
        for i in self.RAM.pos:
            if i.conteudo == processo:
                return True
        return False


    def get_empty_positions(self):
        lista = self.RAM.pos
        nova_lista = []

        for i in lista:
            if i.is_vazio():
                nova_lista.append(i)

        return nova_lista

    def teste(self):
        print type(self.escalonador)

class Memoria():

    def __init__(self, tamanho=1):
        self.tamanho_real = tamanho
        self.tamanho_pratico = tamanho * 1024
        self.pos = []

        aux = self.tamanho_pratico
        while aux > 0:
            b = bloco.BlocoRAM()
            if b.tamanho <= aux:
                self.pos.append(b)
                aux -= b.tamanho


    def malloc(self, processo):
        '''
        Aloca usando o conceito do Merge-fit.

        Minha lógica:
            - Se a memória necessária do objeto for menor que a do bloco. Aloca normal
            - Senão, se a memória necessária do objeto for maior que a do bloco, faz o merge
        :param processo:
        :return:
        '''

        b = self.get_bloco_alocavel()

        if b == False:
            return False

        if b.tamanho >= processo.memoria_necessaria:
            b.conteudo = processo
        else:
            #TODO Testar depois se isso aqui funciona
            b = self.merge(b, processo.memoria_necessaria)
            b.conteudo = processo

        return True


    def merge(self, b, tamanho):
        '''
        Lógica do Merge-fit.
        :param b: bloco a ser mesclado
        :param tamanho: tamanho minimo pro novo bloco ter
        :return: Referência ao novo bloco
        '''

        i = self.pos.index(b)
        old_pid = b._PID #Pega o PID do antigo bloco :v
        aux = b.tamanho
        lista_adjacentes = []
        cont = 1
        while aux < tamanho:
            bloco_adjacente = self.pos[i+cont]
            lista_adjacentes.append(bloco_adjacente)
            aux += bloco_adjacente.tamanho
            cont += 1
        novo_bloco = bloco.BlocoRAM(tamanho)
        novo_bloco._PID = old_pid #Atualiza o PID dele na marra xD
        self.pos[i] = novo_bloco

        #Retira os antigos blocos da lista
        for i in lista_adjacentes:
            self.pos.remove(i)
            #del self.pos[index]

        return novo_bloco

    def split(self):
        """
        Lógica do Split. Aumenta o número de blocos da RAM
        :return:
        """
        for i in self.pos:
            p = i.conteudo
            if p.memoria_necessaria < i.tamanho:
                bloco_ocupado = bloco.BlocoRAM(p.memoria_necessaria)
                bloco_ocupado = p #Copia o conteúdo no novo bloco
                novo_bloco = bloco.BlocoRAM(i.tamanho - p.memoria_necessaria)

                #Insere valores na memória
                p = bloco_ocupado
                self.pos.insert(self.pos.index(p) ,novo_bloco)


    def dealloc(self, processo):
        for i in self.pos:
            if i.conteudo == processo:
                i.conteudo = None
                return True
        return False

    def get_bloco_alocavel(self):
        for i in self.pos:
            if i.conteudo == None:
                return i
        return False

    def is_alocavel(self):
        if self.get_bloco_alocavel() != False:
            return True
        return False


    def teste(self):
        print self.pos

    def __str__(self):
        return str(self.pos)
