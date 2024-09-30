from models.state import State
from models.transition import Transition
import os

stateString = "state"
transitionString = "transition"
initialString = "initial"
finalString = "final"

class Input:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.states = []
        self.transitions = []
        self.initial_state = None
        self.final_state = None
        
    def parse(self):
        with open(self.file_path, 'r') as f:
            for line in f:
                
                print ("Currently at line : " + line)
                line = line.strip()
                if not line:  # Skip empty lines
                    print("skipping empty line")
                    continue
                
                parts = line.split('(')
                print("Parts : " + str(parts))
                keyword = parts[0].lower().strip() 
                print("Keyword : " + keyword)
                
                if keyword == stateString:
                    self.parse_state(line)
                elif keyword == transitionString:
                    self.parse_transition(line)
                elif keyword == initialString:
                    self.parse_initial(line)
                elif keyword == finalString:
                    self.parse_final(line)
                else:
                    print(f"Unknown keyword: {keyword}. Skipping line: {line}")
    
    def parse_state(self, line):
        print("Parsing state")
        content = line[6:-2]
        parts = [part.strip() for part in content.split(',')]
        name = parts[0]
        entry = parts[1] if parts[1] != 'null' else "null"
        do = parts[2] if parts[2] != 'null' else "null"
        exit = parts[3] if parts[3] != 'null' else "null"
        self.create_state(name, entry, do, exit)
    
    def parse_transition(self, line):
        print ("Parsing transition")
        content = line[11:-2]
        parts = [part.strip() for part in content.split(',')]
        source = parts[0]
        target = parts[1]
        guard = parts[2] if parts[2] != 'null' else "null"
        action = parts[3] if parts[3] != 'null' else "null"
        self.create_transition(source, target, guard, action)
    
    def parse_initial(self, line):
        content = line[8:-1]
        self.initial_state = content.strip()
    
    def parse_final(self, line):
        content = line[6:-1]
        self.final_state = content.strip()
    
    def create_simulation(self):
        pass
    
    def create_state(self, name, entry, do, exit):
        state = State(name, entry, do, exit) 
        self.states.append(state)
        
    def create_transition(self, source, target, guard, action):
        transition = Transition(source, target, guard, action)
        self.transitions.append(transition)
        
    def print_states(self):
        print("Printing states")
        for state in self.states:
            print(state)
            
    def print_transitions(self):
        print("Printing transitions")
        for transition in self.transitions:
            print(transition)