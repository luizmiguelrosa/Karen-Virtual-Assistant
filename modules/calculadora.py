from decimal import Decimal

# Irei mudar totalmente então ignore

class acoes:
    def __init__(self):
        self.incorreto = {
            'Quanto é um mais um\n':'1 + 1 é igual a 2',
            'Quanto é dois mais dois\n':'2 + 2 é igual a 4'
        }
        self.oper = ['+', '-', 'x', '/', 'dividido']
        pass

    def process_decimal(self, entrada, posiop):
        vir = entrada[9:posiop - 1]
        v2 = entrada[posiop + 1:].strip(' ')

        if ',' in vir or ',' in v2:
            vir = vir.replace(',', '.')
            v2 = v2.replace(',', '.')
            n1 = Decimal(vir)
            n2 = Decimal(v2)
        else:
            n1 = int(entrada[9:posiop - 1])
            n2 = int(entrada[posiop + 1:].strip(' '))
        return n1, n2

    def process_data(self, entrada):
        if entrada in self.incorreto:
            for frase in self.incorreto:
                if entrada == frase:
                    result = self.incorreto[frase]
                    return result
        else:
            for op in self.oper:
                posiop = entrada.find(op)
                if op == entrada[posiop]:
                    break
            n1, n2 = acoes.process_decimal(self, entrada, posiop)
            if op == self.oper[0]:
                igual = n1 + n2
                return f'{n1} mais {n2} é igual a {igual}'
            elif op == self.oper[1]:
                igual = n1 - n2
                return f'{n1} menos {n2} é igual a {igual}'
            elif op == self.oper[2]:
                igual = n1 * n2
                return f'{n1} vezes {n2} é igual a {igual}'
            elif op == self.oper[3] or op == self.oper[3]:
                igual = n1 / n2
                return f'{n1} dividido por {n2} é igual a {igual}'
    
    def saida(self, entrada):
        acoes.__init__(self)
        return acoes.process_data(self, entrada.strip('\n'))