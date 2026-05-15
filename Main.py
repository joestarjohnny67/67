from traceback import print_tb


class Main:
    def __init__(self, dinheiro = 67):
        self.dinheiro = dinheiro
    def selecao(self):
        print("--------------------")
        print("| SISTEMA BANCARIO |")
        print("--------------------\n")
        print("1.Saque")
        print("2.Deposito")
        print("3.Trasferência")
        print("4.Consulta de saldo\n")
        ecolha = int(input)
    def saque(self):
        saque = float(input(f"Você tem R${self.dinheiro}, quanto quer sacar?"))
        if self.dinheiro > saque:
            self.dinheiro -= saque
            print(f"Você sacou {saque}, e agora tem {self.dinheiro} na conta")
        else: print("Valor invalido")
        print("")

banco = Main()
banco.selecao()