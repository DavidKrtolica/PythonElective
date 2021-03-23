class Deck:
    def __init__(self, cards):
        self.__cards = cards

    @property
    def cards(self):
        return self.__cards

    def __getitem__(self, key):
        return self.__cards[key]

    def __setitem__(self, key, value):
        self.__cards[key] = value

    def __delitem__(self, key):
        del self.__cards[key]

    def __len__(self):
        return len(self.__cards)

    def __add__(self, other):
        return Deck(self.cards + other.cards)
    
    def __str__(self):
        return str(self.__cards)

    def __repr__(self):
        return f'{self.__dict__}'