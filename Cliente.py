#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:40:26 2018

@author: cmdrlias
"""

class Cliente:
    
    def __init__(self, nm_cliente, id_telegram):
        self.nm_cliente = nm_cliente
        self.id_telegram = id_telegram
        self.lista_compra_produto = []
        
    def getNm_cliente(self):
        return self.nm_cliente
    
    def getId_telegram(self):
        return self.id_telegram
    
    def getLista_compra_produto(self):
        return self.lista_compra_produto
    
    def setNm_cliente(self, nm_cliente):
        self.nm_cliente = nm_cliente
        
    def setId_telegram(self, id_telegram):
        self.id_telegram = id_telegram
        
    def setLista_compra_produto(self, lista_compra_produto):
        self.lista_compra_produto = lista_compra_produto