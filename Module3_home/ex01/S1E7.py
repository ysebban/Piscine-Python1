from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Init Baratheon Class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """ Method to kill a Baratheon"""
        if self.is_alive is True:
            self.is_alive = False

    def __str__(self):
        """Returns __str__ for Baratheon"""
        return str((f"('{self.family_name}' ",
                    f"'{self.eyes}' ",
                    f"{self.hairs})"))

    def __repr__(self):
        """Returns __repr__ for Baratheon"""
        return str((f"('{self.family_name}' ",
                    f"'{self.eyes}' ",
                    f"{self.hairs})"))


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Init Lannister Class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """ Method to kill a Lannister"""
        if self.is_alive is True:
            self.is_alive = False

    def __str__(self):
        """Returns __str__ for Lannister"""
        return str((f"('{self.family_name}' ",
                    f"'{self.eyes}' ",
                    f"{self.hairs})"))

    def __repr__(self):
        """Returns __repr__ for Lannister"""
        return str((f"('{self.family_name}' ",
                    f"'{self.eyes}' ",
                    f"{self.hairs})"))

    def create_lannister(name: str, is_alive=True):
        """Returns new Lannister instance"""
        return (Lannister(name, is_alive=True))
