import random
from datetime import datetime
import os

def play_round(word, num_players):
    random.seed(datetime.now().timestamp())

    # Erzeuge eine Liste mit den Spielertags, wobei einer davon der Spion ist
    player_tags = [word] * (num_players - 1) + ["spion"]

    random.shuffle(player_tags)  # Mische die Tags

    clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')  # Plattformunabhängige Funktion, um die Konsole zu leeren
    clear_screen()

    # Zeige die Tags nacheinander an
    for tag in player_tags:
        input("Begriff anzeigen (Enter drücken)!")
        clear_screen()
        print(tag)
        input("Drücke Enter für nächsten Spieler!")
        clear_screen()

if __name__ == '__main__':
    try:
        num_players = int(input("Anzahl Spieler: "))
        secret_word = input("Geheimwort: ")
        play_round(secret_word, num_players)
    except ValueError:
        print("Bitte eine gültige Zahl für die Anzahl der Spieler eingeben.")
