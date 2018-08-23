
class Experience:
    __domain = None
    __years = None
    __projects = None

    def __init__(self, domain, years, projects = []):
        self.domain = domain
        self.years = years
        self.projects = projects

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, value):
        self.__domain = value

    @property
    def years(self):
        return self.__years

    @years.setter
    def years(self, value):
        self.__years = value

    @property
    def projects(self):
        return self.__projects

    @projects.setter
    def projects(self, value):
        self.__projects = value

    def serialize(self):
        return {
            "domain": self.domain,
            "years": self.years,
            "project": [current_project.serialize() for
                        current_project in self.__projects]
        }
