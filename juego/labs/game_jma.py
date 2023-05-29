from enum import Enum
# User Choices


class UserChoice (Enum):
    INVALID = -1
    PAPER = 1
    ROCK = 2
    SCISSORS = 3
    QUIT = 0


def game_loop():
    """
    Arranca el bucle principal del juego
    """
    while True:
        # Leo la selección del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        # Siempre y cuando no quiera parar
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
    """
    Imprime un menu de instrucciones y lee la respuesta del usuario
    mediante una llamada a `input`.
    Devuelve lo que haya elegido el usario, como una cadena45455
    """
    user_choice = UserChoice.INVALID
    while user_choice == user_choice.INVALID:
        print("Select One number: ")
        print(f'{UserChoice.PAPER.value}.Paper')
        print(f'{UserChoice.ROCK.value}.Rock')
        print(f'{UserChoice.SCISSORS.value}.Scissors')
        print(f'------------------')
        print(f'{UserChoice.QUIT.value}.Quit the game')
        try:
            user_choice = int(input('Please selec an option: '))
        except ValueError:
            user_choice = UserChoice.INVALID
        except TypeError:
            user_choice = user_choice.INVALID

        # valido lo que ha dicho
        if user_choice != UserChoice.INVALID:
            break  # ok y nos vamos

    return user_choice


def is_exit(user_choice):
    """
    Predicado que recib ela respuesta del usuario y devuelve `True` si
    ha pedido salir del juego
    """
    return True


def generate_computer_choice():
    """
    Genera una jugada del ordenador de forma aleatoria. El ordenador no puede elegir
    para el juego, solo Piedra, Papel o Tijera
    """
    pass
    return


def evaluate_move(user_choice, computer_choice):
    """
    Recibe dos jugadas, determina cual ha ganado y devuelve un mensaje con el resultado.
    Por ejemplo: recibe Papel y Piedra, y devuelve "Papel envuelve Piedra"
    """
    pass
    return


def print_result(result):
    """
    Imprime en plan bonito el resultado.
    No devuelve nada
    """
    pass


def log_error(error):
    """
    Recibe una excepción del tipo que sea y guarda toda la info
    en sentry.io o lo que sea
    """
    print('Unhandled Exception!')
    print(error)


if __name__ == "__main__":
    try:
        game_loop()
    except Exception as error:
        log_error(error)
