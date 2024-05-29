import random

def generate_random_list(length):
    """Generate a random list of integers."""
    return [random.randint(0, 100) for _ in range(length)]

def get_user_inputs(length):
    """Get a list of integers from user input."""
    user_list = []
    for _ in range(length):
        user_input = int(input("Inserisci il numero: "))
        user_list.append(user_input)
    return user_list

def check_sorted_list(random_list, user_list):
    """Check if the user input list matches the sorted random list."""
    sorted_random_list = sorted(random_list)
    for i in range(len(user_list)):
        if user_list[i] != sorted_random_list[i]:
            print("C'è un errore!")
            return
    print("Tutto bene!")
    
def check_reverse_sorted_list(random_list, user_list):
    """Check if the user input list matches the sorted random list."""
    sorted_random_list = sorted(random_list, reverse = True)
    for i in range(len(user_list)):
        if user_list[i] != sorted_random_list[i]:
            print("C'è un errore!")
            return
    print("Tutto bene!")

def lista_crescente():
    """Main function to generate random list, get user inputs, and check correctness."""
    numbers = int(input("Quanti numeri vuoi inserire? "))
    random_list = generate_random_list(numbers)
    print(f"Ordina questi numeri in ordine CRESCENTE: {random_list}")
    
    user_list = get_user_inputs(len(random_list))
    
    check_sorted_list(random_list, user_list)
    
def lista_decrescente():
    """Main function to generate random list, get user inputs, and check correctness."""
    numbers = int(input("Quanti numeri vuoi inserire? "))
    random_list = generate_random_list(numbers)
    print(f"Ordina questi numeri in ordine DECRESCENTE: {random_list}")
    
    user_list = get_user_inputs(len(random_list))
    
    check_reverse_sorted_list(random_list, user_list)

