from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        """King init shall be baratheon """
        super().__init__(first_name, is_alive)

    def die(self):
        """ Method to kill the king"""
        if self.is_alive is True:
            self.is_alive = False

    def set_eyes(self, color: str):
        """Change king eyes color"""
        self.eyes = color

    def set_hairs(self, color: str):
        """Change king hair color"""
        self.hairs = color

    def get_eyes(self) -> str:
        """Get king eye color"""
        return self.eyes

    def get_hairs(self) -> str:
        """Get king hair color"""
        return self.hairs
