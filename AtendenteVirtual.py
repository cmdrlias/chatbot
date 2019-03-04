#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telepot
from Produto import Produto
from Cliente import Cliente

class SraAtendenteVirtual:
    
    def __init__(self):
        self.__valorCompra = 0
        self.__listaClientesCompra = []
        self.__bot = telepot.Bot('787956473:AAEwVbjl-A4Qqtg7z0BIM_CDryEnTWNbOe4')
        self.__clienteAtual = None
        self.__mensagemAtual = ""
        self.__fechandoCompra = False
    
    def ValorTotalVenda(self):
        return self.__valorCompra
    
    def ListarClientesCompra(self):
        return self.__listaClientesCompra
    
    def ReceberMensagem(self, msg):
        
        if (self.__clienteAtual is None):
            id_usuario = msg['from']['id']
            nm_usuario = (msg['from']['first_name'])
            self.__clienteAtual = Cliente(nm_usuario, id_usuario)
        
        self.__mensagemAtual = msg['text']
        
        if(not self.__fechandoCompra):
            self.AtenderCliente(self.__mensagemAtual)
        else:
            self.DefineMetodoPagamento()
            
    def EnviarMensagem(self, mensagem):
        self.__bot.sendMessage(self.__clienteAtual.getId_telegram(), mensagem)

    def AtenderCliente(self,msg):
        
        lista_produtos = [
            Produto("Sanduiche de Frango", "Frango", 10),
            Produto("Sanduiche de Boi", "Boi", 20),
            Produto("Açai", "500ml", 30),
            Produto("Batata Frita", "500gr", 40),
            Produto("Marmita", "Cenoura", 50),
            Produto("Suco de Açai", "500ml", 60),
            Produto("Coca Cola", "1 Litro", 70),
            Produto("Whey Protein", "250ml", 80)
            
        ]
        
        menu = ""
        
        for i in range(len(lista_produtos)):
            menu += str(i + 1) + " - " + lista_produtos[i].getInfo() + "\n"
        
        menu+= "9 - Sair "
        #try:
           
        self.EnviarMensagem("Esolha um item:\n" + menu)    
        x = True
        
        while(x):
            if(int(self.__mensagemAtual) == 9):
                x = False
                self.__fechandoCompra = True  
                self.FecharAtendimento()
            elif (int(self.__mensagemAtual) > 0 and int(self.__mensagemAtual) < 9):
                print(lista_produtos[int(self.__mensagemAtual) - 1].getInfo())
                self.__valorCompra += lista_produtos[int(self.__mensagemAtual) -1].getVr_produto()
                self.EnviarMensagem("Produto adicionado ao carrinho!\n") 
                x = False
            else:
                self.EnviarMensagem("Este produto não existe.\n")
                x = False
                
        
        
         
            
    #except:
       # self.EnviarMensagem("O que você disse?\n")
        
    
    def FecharAtendimento(self):        
        valorTotalCompra = self.__valorCompra
        
        if(self.__valorCompra > 100):
            valorDesconto = self.__valorCompra * 0.05
            valorTotalCompra = self.__valorCompra - valorDesconto
            
        self.EnviarMensagem("O valor total da compra: " + str(valorTotalCompra))
        self.DefineMetodoPagamento()
        
        
    def DefineMetodoPagamento(self):
        self.EnviarMensagem("Pagamento: \n 1 - Dinheiro;\n 2 - Crédito")
        
        if(int(self.__mensagemAtual) == 1):
            self.EnviarMensagem("Pagamento feito em dinheiro com sucesso")
            self.ZerarVariaveis()
        elif(int(self.__mensagemAtual) == 2):
            self.EnviarMensagem("Pagamento feito em crédito com sucesso")
            self.ZerarVariaveis()
        elif(int(self.__mensagemAtual) != 2 and int(self.__mensagemAtual)!=1 and int(self.__mensagemAtual)!=9 ):
            self.EnviarMensagem("Metodo de pagamento inválido! Compra cancelada.")
            self.ZerarVariaveis()
            
    def ZerarVariaveis(self):
        self.__valorTotalCompra = 0
        self.__valorDesconto = 0
        self.__init__()
        
        
    def getBot(self):
        return self.__bot