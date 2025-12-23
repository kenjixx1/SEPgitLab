from abc import ABC,abstractmethod

class Transportation(ABC):
    def __init__(self,s,e,d):
        self.start = s
        self.end = e
        self.distance = d
