def table(num):
    # Определим ширину для выравнивания
    width = len(str(num * num))  # ширина равна количеству цифр в максимальном значении

    for x in range(1, num + 1):
        for y in range(1, num + 1):
            # Выводим результат, выравненный по правому краю
            print(f"{x * y:>{width}}", end=" ")
        print()

table(10)