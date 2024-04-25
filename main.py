# Розроблення програми з таймером, що підраховує
# час. Використати JSON для збереження стану таймера
# (наприклад, поточний час) у файлі. При перезапуску
# програми відновити час збереженого стану за
# допомогою завантаження даних з JSON-файлу.

import time
import json

current_time = time.localtime()


class Time():
    def __init__(self):
        self.hours = current_time.tm_hour
        self.minutes = current_time.tm_min

    def get_time(self):
        return f"{self.hours}:{self.minutes}"

    def save(self, filename='timer.json'):
        dct = {"hours": self.hours,
               "minutes": self.minutes}
        with open(filename, 'w') as file:
            json.dump(dct, file)


timer = Time()
print(timer.get_time())
timer.save()














