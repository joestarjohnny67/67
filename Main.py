from traceback import print_tb


class Main:
    def __init__(self, dinheiro = 0):
        self.dinheiro = dinheiro
    def saque(self):
        saque = float(input(f"Você tem R${self.dinheiro}, quanto quer sacar?"))
        if self.dinheiro > saque:
            self.dinheiro -= saque
            print(f"Você sacou R${saque}, e agora tem R${self.dinheiro} na conta")
        else: print("Valor invalido")
        print("")
    def deposito(self):
        deposito = float(input(f"Você tem R${self.dinheiro}, quanto quer depositar?"))
        if self.dinheiro > deposito:
            self.dinheiro -= deposito
            print(f"Você depositou R${deposito}, e agora tem R${self.dinheiro} na conta")
        else:
            print("Valor invalido")
    def transferencia(self):
        transferencia = float(input(f"Você tem R${self.dinheiro}, quanto quer transferir?"))
        if self.dinheiro > transferencia:
            self.dinheiro -= transferencia
            pessoa = input("Pra quem você deseja transferir? ")
            print(f"Você transferiu R${transferencia}, para {pessoa} e agora tem R${self.dinheiro} na conta")
        else:
            print("Valor invalido")

banco = Main()
print("--------------------")
print("| SISTEMA BANCÁRIO |")
print("--------------------\n")
print("1.Saque")
print("2.Deposito")
print("3.Transferência")
print("4.Consulta de saldo")
print("5.Sair\n")
escolha = int(input("Qual dessas operações você deseja realizar"))
if escolha == 1: banco.saque()
elif escolha == 2: banco.deposito()
elif escolha == 3: banco.transferencia()
else: print("Sistema encerrado")
