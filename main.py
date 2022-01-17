from ChatBot import Interagir, Voz
from ChatBot.utils import process_entrada, detectar_karen

i = Interagir()
v = Voz()
while True:
    entrada = v.escute()
    if detectar_karen(entrada):
        entrada = process_entrada(entrada)
        saida = i.saida(entrada)
        print("Karen >", saida)
        v.fale(saida)