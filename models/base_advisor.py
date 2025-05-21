from abc import ABC ,abstractmethod

class Baseadvisor(ABC):
    def __init__(self,name,face_shape,skin_tone):
        self.__name = name
        self._face_shape = face_shape
        self._skin_tone = skin_tone

    @abstractmethod
    def recommend_makeup(self):
        pass

    def get_user_information(self):
        return f" Client :{self.__name} - {self._face_shape} face ,{self._skin_tone} skin"
    @classmethod
    def general_tips(cls):
        return' general Tip: Always mosturie before makeup!'
        