class Racer:
    def __init__(self, name: str, team: int, age: int):
        """
        Создание и подготовка к работе объекта "Гонщик"
        :param name: имя гонщика
        :param team: название команды
        :param age: возраст
        """

    def is_racer(self) -> bool:
        """
        Функция которая проверяет является ли словарь гонщиком
        :return: Является ли объект гонщиком или нет
        """
        ...

    def take_a_test_ride(self) -> str:
        print('Тестовый заезд гонщика команды пройден')
        """
        Гонщик проходит тестовый заезд
        """
        ...
    def going_off_the_track(self) -> str:
        print('Гонщик сошел с трассы')
        """
        Гонщик сходит с трассы.
        """
        ...

    def complete_a_qualify(self,place: int) -> str:
        print('Квалификация гонщика команды пройдена, место:')
        """
        Гонщик проходит квалификацию, занимает место от 1 до 20.
        """
        ...

    def complete_a_main_race(self,place: int) -> str:
        print('Основная гонка гонщика команды пройдена, место:')
        """
        Гонщик проходит основную гонку, занимает место от 1 до 20.
        """
        ...
if __name__ == "__main__":
    racer_a = Racer(Lewis_Hamilton, Mercedes, 34)
    racer_b = Racer(Max_Verstappen, Red_Bull, 23)
    racer_c = Racer(Carlos_Sains, Ferrarri, 26)

