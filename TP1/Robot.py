class Robot:
    def __init__(self, type):
        conteneurA = 0
        conteneurB = 0
        conteneurC = 0
        type = type

    def setter(self, nbA,nbB,nbC):
        self.conteneurA = nbA
        self.conteneurB = nbB
        self.conteneurC = nbC

    def add(self,number, type):
        #add objects to the robot
        if (type =='A'):
            self.conteneurA += number
        if (type =='B'):
            self.conteneurB += number
        if (type =='C'):
            self.conteneurC += number

    def calculConstVitesse(self):
        if self.type == 'X':
            return 1 + self.conteneurA + self.contenurB * 3
        elif self.type == 'Y':
            return 1.5 + 0.6*(self.conteneurA + self.contenurB * 3 + self.conteneurC*6)
        elif self.type == 'Z':
            return 2.5+ 0.2(self.conteneurA + self.contenurB * 3 + self.conteneurC*6)
