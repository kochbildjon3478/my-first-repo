class Streamer:
    # ... твой существующий код (__init__, add_donate, total_donates, average_donate) ...

    def print_stats(self):
        print(f"Стример: {self.nickname}")
        print(f"Подписчики: {self.subscribers}")
        print(f"Всего донатов: {self.total_donates()}")
        print(f"Средний донат: {self.average_donate()}")

# Создаем тестового стримера
streamer = Streamer("GolubKin", 1200)
streamer.add_donate(500)
streamer.add_donate(150)

# Вызываем функцию для проверки
streamer.print_stats()
