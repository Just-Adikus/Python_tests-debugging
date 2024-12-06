import math
import logging

# Настройка логирования
logging.basicConfig(
    filename="logs/app.log",  # Файл для записи логов
    filemode="a",             # Режим добавления логов
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO        # Уровень логирования
)

logger = logging.getLogger()  # Создаем объект логгера

# Реализация функций
def factorial(n):
    logger.info(f"factorial called with n={n}")  # Лог входного значения
    if not isinstance(n, int) or n < 0:
        logger.error(f"Invalid input for factorial: n={n}")
        raise ValueError("n must be a non-negative integer")
    result = 1 if n == 0 else n * factorial(n - 1)
    logger.info(f"factorial({n}) = {result}")  # Лог результата
    return result

def is_prime(n):
    logger.info(f"is_prime called with n={n}")
    if not isinstance(n, int) or n <= 1:
        logger.warning(f"Input is not a prime candidate: n={n}")
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            logger.info(f"{n} is not prime; divisible by {i}")
            return False
    logger.info(f"{n} is prime")
    return True

def gcd(a, b):
    logger.info(f"gcd called with a={a}, b={b}")
    while b:
        a, b = b, a % b
    logger.info(f"gcd result = {abs(a)}")
    return abs(a)


if __name__ == "__main__":
    import pdb

    # Точка остановки
    pdb.set_trace()
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Is 7 prime? {is_prime(7)}")
    print(f"GCD of 48 and 18: {gcd(48, 18)}")
