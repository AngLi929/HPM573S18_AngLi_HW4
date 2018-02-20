from enum import Enum
import numpy as np

class Coin(Enum):
    Head = 1
    Tail = 0


class Game(object):
    def __init__(self, id, prob):
        self._id = id
        self._prob = prob
        self._rnd = np.random
        self.outcome = []

    def simulate(self, n_time_steps):

        t = 0
        while t < n_time_steps:

            if self._rnd.sample() < self._prob:
                self.outcome.append(1)

            else:
                self.outcome.append(0)
            t += 1

    def get_outcome(self):

        return self.outcome

    def get_exp_cost(self):
        exp_cost = -250
        for i in range(len(self.outcome)-2):
            if self.outcome[i] == 0 and self.outcome[i+1] == 0 and self.outcome[i+2] == 1:
                    exp_cost += 100
        return exp_cost

    def get_exp_time(self):
        t = 0
        for i in range(len(self.outcome) - 2):
            if self.outcome[i] == 0 and self.outcome[i + 1] == 0 and self.outcome[i + 2] == 1:
                t += 1
        return t


class Games():
    def __init__(self, realization_times, prob):
        self._prob = prob
        self._realization_times = realization_times
        self.games = []
        self.expected_cost = []
        self.time = []
        for i in range(realization_times):
            game = Game(i, prob)
            self.games.append(game)

    def simulate(self, n_time_steps):
        for game in self.games:
            game.simulate(n_time_steps)

    def get_ave_exp_cost(self):

        for game in self.games:
            value = game.get_exp_cost()
            self.expected_cost.append(value)
            ave_exp_cost = sum(self.expected_cost) / len(self.expected_cost)
        return ave_exp_cost

    def get_total_time(self):

        for game in self.games:
            x = game.get_exp_time()
            self.time.append(x)
            total_time = sum(self.time)
        return total_time


