import numpy as np


class Team:
    def __init__(self, name):

        self.name = name
        self.score = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            sys.exit("Country name not recongnised, exiting")
        else:
            self._name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = np.random.randint(0, 5)
