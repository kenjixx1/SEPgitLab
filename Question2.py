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

class Train(Transportation):
    def __init__(self, s, e, d):
        super().__init__(s, e, d)
    
    def calculate(self):
        return self.distance*5

def main():
    t1 = Walk("Dorm", "Classroom", 2)
    t2 = Taxi("Home", "Mall", 10)
    t3 = Train("Station A", "Station B", 8)

    print("Walk cost:", t1.calculate(), "Baht")
    print("Taxi cost:", t2.calculate(), "Baht")
    print("Train cost:", t3.calculate(), "Baht")


if __name__ == "__main__":
    main()