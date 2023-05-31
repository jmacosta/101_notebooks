from enum import Enum


# User Choices
class UserChoice(Enum):
    INVALID = -1
    PAPER = 0
    ROCK = 1
    SCISSORS = 2
    QUIT = 3


def game_loop():
    """
    Arranca el bucle principal del juego
    """
    while True:
        # Leo la selección del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        # Siempre y cunado no quiera parar
        if not is_exit(user_choice):
            # genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            # evalúo la jugada
            result = evaluate_move(user_choice, comp_choice)
            # muestro el ganador en pantalla y vuelta al principio
            print_result(result)
        else:
            # el humano es un gallina: salgo
            break


def read_user_choice():
    """"
    Lee una selección del usuario (piedra, papel, tijera o salir)
    y la devuelve
    """
    user_choice = UserChoice.INVALID
    while user_choice == UserChoice.INVALID:
        print("Select one number:")
        print(f'{UserChoice.PAPER.value}. Paper')
        print(f'{UserChoice.ROCK.value}. Rock')
        print(f'{UserChoice.SCISSORS.value}. Scissors')
        print(f'--------------------')
        print(f'{UserChoice.QUIT.value}. Quit the game')

        try:
            user_choice = int(input('Enter your choice: '))
        except ValueError:

            user_choice = UserChoice.INVALID

        # valido lo que me ha dicho
        if user_choice != UserChoice.INVALID:
            break  # ok y nos vamos

    return user_choice


def is_exit(user_choice):
    """
    Predicado que devuelve True si el usuario ha decido parar y False
    si quiere seguir jugando
    """
    return True


def generate_computer_choice():
    """
    Genera y devuelve una jugada al azar
    """
    return None


def evaluate_move(user_choice, comp_choice):
    """
    Compara las dos jugadas y devuelve un texto ocn el resultado
    """
    return None


def print_result(result):
    """
    Imprime en bonito el resultado
    """
    return None


def log_error(error):
    """"
    Grarda los datos del error en crashlytics
    """
    print(error)


if __name__ == "__main__":

    try:
        game_loop()
    except Exception as error:
        log_error(error)
