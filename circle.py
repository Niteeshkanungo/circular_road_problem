## For cyclic rotation of cars in N len with M number at 1 forward move at each rotation.
## Author = Niteesh Kanungo/ Niteeshkanungo@gmail.com

## Import libraries

import math
import statistics as st
import random

## Data Structure - for a cyclic order of movement. Here only the position at
## the end is going to matter.

class cycle:
    def __init__(self, N, M, T):
        """
        N = len of road
        M = No. of cars
        T = No. of rounds: where a round is defined as in a chance a car is selected on random and
        moved forward.
        Path a blue print/list on which the M cars will move on N spots, its an array

        """
        self.N = N
        self.M = M
        self.T = T

        E = ["E" for i in range(self.N)]

        for i in range(self.M):
            E[i] = "M"

        self.E = E

        if not len(E):
            raise "need at least one element"

        ## It will create a path list based on the arguments
        self._data = E

    ## Helper functions
    def __repr__(self):
        return repr(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, i):
        return self._data[i]

    ## For average value on the current indexes with cars
    def average(self):
        """
        average does not need any parameter, as it was already passes during the
        initialization of the path.
        """
        indices = []
        for i,j in enumerate(self.E):
            if j == "M":
                indices.append(i)
        return(st.mean(indices))

    def std(self):
        """
        returns the standard deviation based on the current path.
        """
        indices = []
        for i,j in enumerate(self.E):
            if j == "M":
                indices.append(i)
        return(st.stdev(indices))

    def turn(self):
        last = self._data.pop(-1)
        self._data.insert(0, last)

        ## Extra helper functions

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]

    def current(self):
        return(self._data[0])

    def rounds(self):
        """
        rounds can be defined as the chance in which each car
        is chosen at random and moved on the path.

        """
        for i in range(self.T):
            self.E = list(self.E)
            indices = []
            for i,j in enumerate(self.E):
                try:
                    if self.E[i] == "M" and self.E[(i+1)] == "E":
                        indices.append(i)
                except IndexError:
                    if self.E[-1] == "M" and self.E[0] == "E":
                        indices.append(i)

            sel = random.choice(indices)
            try:
                self.E[sel] = "E"
                self.E[sel+1] = "M"
            except IndexError:
                self.E[0] = "E"
                self.E[-1] = "M"

        return(self.E)

## initialize the class with N: M: and T: as asked in the question
path = cycle(25,10,50)

## Run the round, it will move the cars as described with equal probability and will return the current state.
path.rounds()

## Returns the average of the path
path.average()

## Returns the standard deviation of the path
path.std()E.md
