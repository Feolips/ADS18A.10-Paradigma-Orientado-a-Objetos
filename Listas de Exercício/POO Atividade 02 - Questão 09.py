# Aluno: Felipe Souza Vieira
 # Atividade 02 para 12/02/2021
 # Questão 09

'''
09. A máquina de vender bilhetes vende bilhetes de um único tipo,
com um único preço. Após o cliente introduzir  o dinheiro a máquina
deve verificar se o valor é suficiente para pagar pelo bilhete.
Em caso positivo, deve ser possível imprimir o bilhete. Caso contrário,
deve-se permitir que o cliente introduza mais dinheiro na máquina até
que possa imprimir o bilhete, para isso deve ser informar ao cliente
quanto ainda falta para que possa pagar completamente pelo bilhete.
OBS: inserir comentários nos trechos de código informando que tipo de
conceito está sendo usado, por exemplo: na linha de código que um objeto
está sendo instanciado coloque um comentário identificando essa ação.
'''

 # Classe contendo todas as funções (init, def_set e def_get):
class bilheteria:
    def __init__(self, preco=0.0,valor=0.0,troco=0.0) -> None:
        self.setPreco(preco)
        self.setValor(valor)
        self.setTroco(troco)
    def setPreco(self,preco):
        self.preco = preco
        return
    def setValor(self,valor):
        self.valor = valor
        return
    def setTroco(self,troco):
        self.troco = troco
        return
    def getPreco(self):
        return self.preco()
    def getValor(self):
        return self.valor()
    def getTroco(self):
        return self.troco()
    
# Fim da Classe.

# ============Início do programa principal (main)============

print ("\n" * 30) # Dica do StackOverflow para limpar a tela :D
maquina = bilheteria() # Instanciamento da Classe
maquina.setPreco(float(input("Insira o valor do ingresso: R$"))) # Definição do Preço
maisDinheiro,valor = 0.0
print ("\n" * 30)
# Enquanto o preço não for coberto, continue pedindo dinheiro:
while maquina.preco > maisDinheiro:
    print('Saldo atual: R${}'.format(maquina.getValor(valor)))
    maisDinheiro = float(input("Fundos insuficientes, insira dinheiro: R$"))
    maquina.setValor = maquina.getValor + maisDinheiro