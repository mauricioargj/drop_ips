#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time


def del_rules():
    arquivo = open(data, 'r')
    for linha in arquivo:
        res = linha.split()
        os.system('iptables -D INPUT -s ' + res[0] + ' -j DROP')

        os.system('rm -f ' + data)


def drop_ips():
    os.system('wget https://url/blocklist/blocklist.txt &>/dev/null')
    arquivo = open(data, 'r')
    for linha in arquivo:
        res = linha.split()
        os.system('iptables -I INPUT -s ' + res[0] + ' -j DROP')


"""
Iniciando Script
"""

data = "./blocklist.txt"

if os.path.isfile(data):
    print("Abrindo Arquivo")
    time.sleep(1)
    print("Deletando Regras")
    del_rules()
    print ("Aplicando Drop nos Ips")
    drop_ips()
else:
    print("O arquivo não existe")
    os.system('service firewalld restart &>/dev/null')
    time.sleep(7)
    drop_ips()
