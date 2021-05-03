class Carro:
    def __init__(self, velocidadeMax):
        self.velocidadeMax = velocidadeMax
        self.velocidadeAtual = 0

    def acelerar(self, delta=5):
        if (self.velocidadeAtual + delta) <= self.velocidadeMax:
            self.velocidadeAtual += delta
            print(self.velocidadeAtual)
        else:
            self.velocidadeAtual = self.velocidadeMax
            return 0

    def frear(self, delta=5):
        if (self.velocidadeAtual - delta) >= 0:
            self.velocidadeAtual -= delta
            print(self.velocidadeAtual)

        else:
            self.velocidadeAtual = 0
            return 0


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        c1.acelerar(8)

    for _ in range(10):
        c1.frear(delta=20)


