from state import State
from transition import Transition

class System (object):
    def __init__(self, name : str, states : list[State], transitions : list[Transition]):
        self.name = name
        self.states = states
        self.transitions = transitions 
