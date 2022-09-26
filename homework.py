class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                training_type: str,
                duration: float,
                distance: float,
                speed: float,
                calories: float) -> str:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    
        return (f'Тип тренировки: {self.training_type};'\
                f'Длительность: {self.duration} ч.;'\
                f'Дистанция: {self.distance} км;'\
                f'Ср. скорость: {self.speed} км/ч;'\
                f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,           # Количество действий за тренировку
                 duration: float,       # Длительность тренировки (часов)
                 weight: float,         # Вес спортсмена (гк)
                 M_IN_KM: int = 1000,   # Коэффициент перевода из м в км
                ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.M_IN_KM = M_IN_KM

    def get_distance(self, LEN_STEP: float) -> float:
        """Получить дистанцию в км."""
        return self.action * LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info = InfoMessage(self.training_type,
                           self.duration,
                           self.distance,
                           self.speed,
                           self.calories)
        return info
        

class Running(Training):
    """Тренировка: бег."""
    def __init__(self,
                action: int,
                duration: float,
                weight: float,
                M_IN_KM: int,
                ) -> float:
        super().__init__(action,
                        duration,
                        weight,
                        M_IN_KM)
    
    def get_spent_calories(self) -> float:
        """Получить количество затраченных килокалорий."""
        coeff_calorie_1: int = 18   # Коэффициент 1
        coeff_calorie_2: int = 20   # Коэффициент 2
        H_IN_MIN: int = 60          # Коэффициент перевода из часов в минуты
        CAL_IN_KCAL: int = 1000     # Коэффициент перевода из калорий в ккал.
        # промежуточные вычисления:
        avg_speed: float = self.get_mean_speed()
        coeff: float = (coeff_calorie_1 * avg_speed - coeff_calorie_2)
        dur_min: float = self.duration * H_IN_MIN
        # Подсчёт и возврат расхода калорий для данной тренировки:
        return coeff * self.weight / self.M_IN_KM * dur_min / CAL_IN_KCAL


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    #    LEN_STEP: float = self.action * 0.65     # Величина шага в метрах
    pass


class Swimming(Training):
    """Тренировка: плавание."""

    #    LEN_STEP: float = self.action * 1.38     # Величина шага в метрах
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    type_tren_dic = {
        'RUN': Running,
        'WLK': SportsWalking,
        'SWM': Swimming
    }
    train_obj = type_tren_dic[workout_type](*data)
    return train_obj # ГОТОВО !!!


def main(training: Training) -> None:
    """Главная функция."""
    print(training.show_training_info())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

