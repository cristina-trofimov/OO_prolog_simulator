from models.state import State
from models.event import Event
from models.guard import Guard
from models.action import Action


class Transition:
    def __init__(self, source, target, event: 'Event' = "null" , guard: 'Guard' = "null", action: 'Action' = "null"):
        self.source = source
        self.target = target
        self.event = event
        self.guard = guard
        self.action = action
        
    # def execute(self, context: dict) -> State:
    #     if self.guard is None or self.guard.check(context):
    #         if self.action:
    #             self.action.execute(context)
    #         return self.target
    #     return self.source
    
    def __str__(self):
        return f"this is a transition : Transition({self.source}, {self.target}, {self.event}, {self.guard}, {self.action})"
    
    def __repr__(self):
        return self.__str__()