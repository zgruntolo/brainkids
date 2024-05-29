import random
import textwrap


def genera_divisione():
    dividendo = random.randint(10, 60)
    divisore = random.randint(2, 10)

    print(f"\n{dividendo}:{divisore}=", end="\n\n")
    for line in textwrap.wrap("*" * dividendo, 10):
        print(line)


def generatore_divisioni():
    while True:
        try:
            divisioni = int(input("Quante divisioni vuoi generare? "))
            if divisioni <= 0:
                raise ValueError("Il numero deve essere positivo.")
            break
        except ValueError as e:
            print(
                f"Input non valido: {e}. Per favore inserisci un numero intero positivo."
            )

    for _ in range(divisioni):
        genera_divisione()

    input("Premi invio per uscire...")
