"""
    Entity module
"""


class Player:
    def __init__(self, identification, name, p_strength):
        self.__id = identification
        self.__name = name
        self.__p_strength = p_strength

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def p_strength(self):
        return self.__p_strength

    @p_strength.setter
    def p_strength(self, p_strength):
        self.__p_strength = p_strength

