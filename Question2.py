from abc import ABC,abstractmethod

class Transportation(ABC):
    def __init__(self,s,e,d):
        self.start = s
        self.end = e
        self.distance = d

    @abstractmethod
    def calculate(self):
        pass


class Walk(Transportation):
    def __init__(self, s, e, d):
        super().__init__(s, e, d)
    
    def calculate(self):
        return 0
    
class Taxi(Transportation):
    def __init__(self, s, e, d):
        super().__init__(s, e, d)
    
    def calculate(self):
        return self.distance*40

