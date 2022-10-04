class Car:

    def __init__(self, nom, rang, yil):
        self.nom = nom
        self.rang = rang
        self.yil = yil

class BMW(Car):

    def get_info(self):

        info += f"Mashina nomi: {self.nom}, rangi: {self.rang}"
        return info

    def get_age(self):

        yil = self.yil - yil

        return yil

mashina = BMW("Mercedes","qora",2021)

mashina.get_age(2022)