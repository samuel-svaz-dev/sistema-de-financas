from rich import print
from src.modelos.transacao import Transacao

class Conta:

    def __init__(self, codigo, titular, saldo = 0.0):
        self.codigo = codigo
        self.titular = titular
        self.saldo = saldo
        self.historico = []


    def adiciona_transacao(self, transacao):
        if transacao.tipo == 'RECEITA':
            self.saldo = self.saldo + transacao.valor
        elif transacao.tipo == 'DESPESA':
            if transacao.valor > self.saldo:
                print(f'[bold red]Saldo Insuficiente![/]')
                return
            else:
                self.saldo = self.saldo - transacao.valor
        self.historico.append(transacao)


    def exibir_extrato(self):
        print(f'[blue] === EXTRATO DA CONTA {self.codigo} - Titular {self.titular} === [/]')
        print(f'[bold]Saldo atual: R${self.saldo:.2f}[/]'.center(55))
        for transacao in self.historico:
            transacao.exibir()
