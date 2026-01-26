class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = 0
        for (x, y) in zip(V1, V2):
            res += x * y
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = []
        for (x, y) in zip(V1, V2):
            res.append(x + y)
        print(f"Add Vector is: {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = []
        for (x, y) in zip(V1, V2):
            res.append(x - y)
        print(f"Add Vector is: {res}")
