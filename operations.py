import random

def generatore_divisioni():
    divisioni = int(input("Quante divisioni vuoi generare? "))
    for i in range(divisioni):
        dividendo = random.randint(10, 60)
        divisore = random.randint(2, 10)
        print(f"\n{dividendo}:{divisore}=", end=2*"\n")
        for j in range(dividendo):
            print("*", end="")
            if (j + 1) % 10 == 0:
                print()
        if dividendo % 10 != 0:
            print()

    input("Premi invio per uscire...")
