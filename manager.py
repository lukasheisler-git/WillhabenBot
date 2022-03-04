from whad import Anzeige
import click
import pickle
import os
from time import sleep


def main():
    print("Willkommen im Anzeigen Manager. ")
    while(1):
        print('Folgende Anzeigen sind vorhanden: ')
        print('Funktion kommt später')

        if click.confirm('Neue Anzeige hinzufügen ? ', default = True):
            print('____________________')
            name = input('Name der Anzeige: ')
            title = input('Titel der Anzeige: ')
            price = input('Preis der Anzeige: ')
            print("Beschreibung einfügen. STRG+D zum speichern")
            contents = []
            while True:
                try:
                    line = input()
                except EOFError:
                    break
                contents.append(line)
            
            print('Kategorieauswahl: ')

        new = Anzeige(name, title, price, contents, [0,0,0])
        new.save()
        sleep(2)
        break


if __name__ == '__main__':
    main()