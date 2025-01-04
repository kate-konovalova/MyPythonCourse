import doctest

# 1-й класс
class Tree:
    def __init__(self, name: str, height: float):
        """
        :param name: дуб, сосна или еще что-то.
        :param height: [м].
        :raises ValueError: Если высота меньше или равна 0.
        """
        if height <= 0:
            raise ValueError("высота дерева должна быть положительной.")

        self.species = name
        self.height = height

    def growth(self, years: int) -> None:
        """

        :param years: сколько лет дереву.

        пример использования для doctest:
        >>> tree = Tree("oak", 5.0)
        >>> tree.grow(3)
        """
        ...

    def cost_estimation(self) -> None:
        """
        расчет стоимости дерева

        Пример использования:
        >>> tree = Tree("березка", 8.0)
        >>> tree.cost_estimation()
        """
        ...


# 2-й класс
class City:
    def __init__(self, name: str, people_count: int):
        """
        :param name: имя города.
        :param people_count: количество жителей.
        :raises ValueError: если количество жителей меньше 1.
        """
        if people_count < 1:
            raise ValueError("это не город.")

        self.name = name
        self.people_count = people_count

    def classify(self) -> None:
        """
        классифицирует город

        пример использования:
        >>> Norilsk = City("Norilsk", 800000)
        >>> table.classify()
        """
        ...

    def method(self) -> None:
        """
        еще метод для города

        пример использования:
        >>> Samara = City("Samara", 1800000)
        >>> table.method()
        """
        ...

# 3-й класс
class Car:
    def __init__(self, model: str, cost: int):
        """
        :param name: mazda, nissan.
        :param cost: 1200000.
        :raises ValueError: Если цена меньше или равна 0.
        """
        if cost <= 0:
            raise ValueError("цена машины должна быть положительной.")

        self.cost = cost
        self.model = model

    def ranking(self, model: str) -> None:
        """

        :param model: марка тачки.

        пример использования для doctest:
        >>> bmw = Car("BMW X6", 11000000)
        >>> bmw.ranking("BMW X6")
        """
        ...

    def selling_price(self) -> None:
        """
        расчет стоимости машины если продать

        пример использования:
        >>> dodge = Car("Dodge Challenger", 1200000)
        >>> tree.selling_price()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()