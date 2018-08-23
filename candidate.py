
import uuid

class Candidate:
    __id = None
    __first_name = ""
    __last_name = ""
    __experience = []

    def __init__(self, first_name,
                 last_name, experience = []):
        self.__id = uuid.uuid4()
        self.__first_name = first_name
        self.__last_name = last_name
        self.__experience = experience

    @property
    def id(self):
        return self.__id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        self.__experience = value

    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "id": self.id,
            "experience": [exp.serialize() for exp in
                           self.experience]
        }

    def add_experience(self, new_experience):
        self.experience.append(new_experience)
