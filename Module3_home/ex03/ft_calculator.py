class calculator:

    def __init__(self, vector: list[float]):
        self.vector = vector

    def __add__(self, object) -> None:
        for entry in range(len(self.vector)):
            self.vector[entry] += object
        print(self)

    def __mul__(self, object) -> None:
        for entry in range(len(self.vector)):
            self.vector[entry] *= object
        print(self)

    def __sub__(self, object) -> None:
        for entry in range(len(self.vector)):
            self.vector[entry] -= object
        print(self)

    def __truediv__(self, object) -> None:
        if object == 0:
            return (print("Division by 0 can't occurs"))
        for entry in range(len(self.vector)):
            self.vector[entry] /= object
        print(self)

    def __repr__(self):
        lst = []
        for e in self.vector:
            lst.append(str(e))
        return str(lst)
