import random

arrays = {
    "Посортований масив": list(range(100)),
    "Майже посортований масив": [i if i not in (50, 51) else 51 if i == 50 else 50 for i in range(100)],
    "Посортований в зворотньому порядку масив": list(range(100, 0, -1)),
    "масив з рандомними значеннями": [random.randint(0, 1000) for _ in range(100)],
    "Масив з однаковими значеннями": [500] * 100,
    "Великий масив": [random.randint(0, 1000) for _ in range(1000)]
}