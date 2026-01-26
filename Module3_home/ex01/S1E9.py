from abc import ABC, abstractmethod


class Character(ABC):
    """ Abstract class Characters
        In this show every one dies
    """
    def __init__(self, first_name: str, is_alive: bool | None = None):
        """
        the Abstract init is for all characters not just stark
        """
        try:
            assert isinstance(first_name, str), \
                "first_name must be string"
            assert isinstance(is_alive, bool), \
                "is_alive must be bool"
        except AssertionError as e:
            print(f"AssertionError: {e}")
        self.first_name = first_name
        self.is_alive = True if is_alive is None else is_alive

    @abstractmethod
    def die(self):
        """ this one is the abstract kill,
        here to force all herited Class to die"""
        pass


class Stark(Character):
    """ Stark family is the cursed one haha """
    def die(self):
        """Method use to kill a Stark"""
        if self.is_alive is True:
            print(f"{self.first_name} Stark, just died")
            self.is_alive = False
