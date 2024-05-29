import random


class PrecedenteSuccessivo:
    def __init__(self):
        self.value = random.randint(0, 300)

    def precedente(self):
        precedente = self.value - 1
        guess = int(input(f"Qual è il precedente del numero {self.value}? "))
        if guess == precedente:
            print("Bravo!", end="\n\n")
        else:
            print("Spiacente, il numero era: ", precedente, end="\n\n")

    def successivo(self):
        successivo = self.value + 1
        guess = int(input(f"Qual è il successivo del numero {self.value}? "))
        if guess == successivo:
            print("Bravo!", end="\n\n")
        else:
            print("Spiacente, il numero era: ", successivo, end="\n\n")


def precedente_successivo():
    ps = PrecedenteSuccessivo()
    ps.precedente()
    ps.successivo()
