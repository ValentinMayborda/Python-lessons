def calculate(expenditure: float, fuel_price: float, distance: float) -> float:
    """
    Функція розраховує вартість пального
    :param expenditure: витрата пального на 100 км
    :param fuel_price: вартість палива
    :param distance: дистація на яку розраховується витрата
    :return: повертає значення вартості в флоат, округлене до 2 цифр після коми
    """
    return round(expenditure / 100 * fuel_price * distance, 2)
