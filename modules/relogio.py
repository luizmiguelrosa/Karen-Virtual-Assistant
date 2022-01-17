from time import localtime

# Irei mudar totalmente então ignore

class acoes:
    def __init__(self):
        self.listames = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        self.listadia = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        self.palavras_chave = ["Dia", "dia", "Horas", "horas", "Horário", "horário", "Horario", "horario"]
        pass
    
    #Função de Horário
    def horario(self):
        t = localtime()
        hora = t[3]
        minuto = t[4]

        if minuto > 0:
            if minuto < 10:
                minuto = f'0{minuto}'
            saida = f'São {hora} horas e {minuto} minutos !'
            return saida
        else:
            saida = f'São {hora} horas em ponto'
            return saida
    #---------------------------------------------------------

    #Função de Dia
    def dia(self):
        d = localtime()
        dia_n = d[2]
        dia_s = d[6]
        mes_n = d[1]
        ano = d[0]
    
        mes = self.listames[mes_n -1]
        dia = self.listadia[dia_s]

        if dia_n == 1:
            saida = f'Hoje são {dia}, primeiro de {mes} de {ano}'
            return saida
        else:
            saida = f'Hoje são {dia}, {dia_n} de {mes} de {ano}'
            return saida
    #--------------------------------------------------------------

    #Função de Saida
    def saida(self, entrada):
        acoes.__init__(self)
        palavras_chave = self.palavras_chave
        for palavra in palavras_chave:
            if palavra in entrada:
                if palavra in palavras_chave[0:2]:
                    result = acoes.dia(self)
                    return result
                elif palavra in palavras_chave[2:7]:
                    result = acoes.horario(self)
                    return result
    #----------------------------------------------------