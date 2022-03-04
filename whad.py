import os
import pickle

class Anzeige:
    def __init__(self, name, title, price, description, cat):
        self.name = name
        self.title = title
        self.price = price
        self.description = description
        self.cat = cat

    def print(self):
        print('Anzeige %'.format(self.name))
        print(self.title)
        print('Preis: ' + str(self.price))
        print(self.description)
        print('_______________________')
        print('Categories: ')
        print(self.cat)

    def save(self):
        try:
            os.makedirs(os.path.join(os.path.dirname(__file__), 'Ads/{}'.format(self.name)))
            name = 'Ads/name/' + self.name + '.pkl'
            file = open(name, "wb")
            pickle.dump(self, file)
            file.close()
        except:
            print('Achtung. Es gibt bereits eine Anzeige mit diesem Namen.')
        

