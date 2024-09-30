from abc import ABC, abstractmethod
from typing import List

class State:
    
    def __init__(self, name: str, entry, do ,exit):
        self.name = name
        self.entry = entry
        self.do = do
        self.exit = exit
        self.transitions = []

    def add_transitions(self, transitions):
        for transition in transitions:
            if transition.source.capitalize() == self.name.capitalize():
                self.transitions.append(transition)
                
    def print_transitions(self):
        print(f"Transitions from state {self.name}:")
        for transition in self.transitions:
            print(transition)

    def __str__(self):
        return "this is a state : State(" + self.name + "," + self.entry + "," + self.do + "," + self.exit + ")"

    def __repr__(self):
        return self.__str__()