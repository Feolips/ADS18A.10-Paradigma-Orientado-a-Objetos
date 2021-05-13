 # Aluno: Felipe Souza Vieira
 # Atividade 02 para 12/02/2021
 # Questões 07 e 08

'''
1. Crie uma classe com três variáveis: nome, sobrenome e salário mensal.
Defina um construtor para iniciar essas variáveis. Então, demonstre o
salário anual de três objetos da sua classe. OBS: inserir comentários
nos trechos de código informando que tipo de conceito está sendo usado,
por exemplo: na linha de código que um objeto está sendo instanciado 
coloque um comentário identificando essa ação.
'''

 # Classe contendo todas as funções (init, def_set e def_get):
class salario:
    # Construtor - função init
    def __init__(self,nome=None,sobrenome=None,sMensal=0.0):
        self.setNome(nome)
        self.setSobrenome(sobrenome)
        self.setsMensal(sMensal)
    # Função set para atribuir valor à variável 'nome':
    def setNome(self, nome):
        self.nome = nome
        return
    # Função get para recuperar o valor contido em 'nome':
    def getNome(self):
        return self.nome()
    # Função set para atribuir valor à variável 'sobrenome':
    def setSobrenome(self, sobrenome):
        self.sobrenome = sobrenome
        return
    # Função get para recuperar o valor contido em 'sobrenome':
    def getNome(self):
        return self.sobrenome()
    # Função set para atribuir valor à variável 'sMensal':
    def setsMensal(self,sMensal):
        self.sMensal = sMensal
        return
    # Função get para recuperar o valor contido em 'sMensal':
    def getsMensal(self):
        return self.sMensal()
    # Função get para recuperar o salário anual:
    def getsAnual(self):
        return (self.getsMensal() * 12.0)
    # Função get para recuperar o aumento de 45% sobre o anual:
    def getsAnualAumento(self):
        return(self.getsAnual() * 1.45)

# Fim da Classe.

# ============Início do programa principal (main)============

# Laço para a criação de 3 objetos:
for i in range(1,4,1):
    # Instanciamento da classe:
    novoEmpregado = salario()
    # Entrada dos dados nome, sobrenome e salário mensal:
    novoEmpregado.setNome(str(input('Informe o primeiro nome do {}º funcionário: '.format(i))))
    novoEmpregado.setSobrenome(str(input('Informe o sobrenome de {}: '.format(novoEmpregado.getNome()))))
    novoEmpregado.setsMensal(float(input('Informe o salário mensal de {}: R$'.format(novoEmpregado.getNome))))
    # Retorno do salário anual, aumento e fim do laço:
    print('O salário anual de {} (fora 13º e outros benefícios) é de R${:.2f}.'.format(novoEmpregado.getNome(), novoEmpregado.getsAnual()))
    print('Com um aumento de 45%% o salário anual de {} passará a R${:.2f}.'.format(novoEmpregado.getNome(),novoEmpregado.getsAnualAumento()))
    print('=' * 40)

print('Fim do programa')
# ============Fim do programa principal (main)============