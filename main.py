# -*- coding: utf-8 -*-

from AtendenteVirtual import SraAtendenteVirtual

atendente = SraAtendenteVirtual()
atendente.getBot().message_loop(atendente.ReceberMensagem)

while True:
    pass