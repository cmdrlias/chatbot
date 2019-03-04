#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:40:48 2018

@author: cmdrlias
"""

class Produto():
    
    def __init__(self, nm_produto, ds_produto, vr_produto):
        self.nm_produto = nm_produto
        self.ds_produto = ds_produto
        self.vr_produto = vr_produto
    
    def getNm_produto(self):
        return self.nm_produto
    
    def getDs_produto(self):
        return self.ds_produto
    
    def getVr_produto(self):
        return self.vr_produto
    
    def setNm_produto(self, nm_produto):
        self.nm_produto = nm_produto
    
    def setDs_produto(self, ds_produto):
        self.ds_produto = ds_produto
    
    def setVr_produto(self, vr_produto):
        self.vr_produto = vr_produto
        
    def getInfo(self):
        return self.nm_produto + " " + self.ds_produto + " - R$" + str(self.vr_produto)