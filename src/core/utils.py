from datetime import datetime


def calculate_coffee_cups(since: str) -> str:
    start = datetime.strptime(since, "%Y-%m-%d")
    end = datetime.now()
    total_coffee: float = (end - start).days * 2

    magnitude = 0
    while abs(total_coffee) >= 1000:
        magnitude += 1
        total_coffee = round(total_coffee / 1000.0, 1)

    return "{:.{}f}{}".format(total_coffee, 1, ["", "k", "m"][magnitude])
