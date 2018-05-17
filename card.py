import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])


class Puke:
    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = 'hong fang mei hei'.split()

    def __init__(self):
        self.cards = [Card(rank,suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]


puke = Puke()
for p in puke:
    print(p)