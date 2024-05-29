from school_suite import operations
from school_suite import order
from school_suite import precedente_successivo

if __name__ == "__main__":
    while True:
        menu = int(
            input(
                "Premi 1 per fare esercizi sui numeri CRESCENTI, 2 per i numeri DECRESCENTI, 3 per le DIVISIONI, 4 per PRECEDENTE SUCCESSIVO, oppure un tasto qualsiasi per chiudere "
            )
        )
        if menu == 1:
            order.lista_crescente()
        elif menu == 2:
            order.lista_decrescente()
        elif menu == 3:
            operations.generatore_divisioni()
        elif menu == 4:
            precedente_successivo.precedente_successivo()
        else:
            break
