import datetime

class SystemClock:
    def __init__(self):
        self._current_time = datetime.datetime.now()

    def get_current_time(self):
        return self._current_time

    def fast_forward(self, hours=0, minutes=0, seconds=0):
        delta = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        self._current_time += delta
        print(f"Clock fast-forwarded by {delta}. New time: {self._current_time}")

    def rewind(self, hours=0, minutes=0, seconds=0):
        delta = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        self._current_time -= delta
        print(f"Clock rewound by {delta}. New time: {self._current_time}")

    def set_time(self, year, month, day, hour, minute, second):
        try:
            self._current_time = datetime.datetime(year, month, day, hour, minute, second)
            print(f"Clock set to: {self._current_time}")
        except ValueError as e:
            print(f"Error setting time: {e}. Please provide a valid date and time.")

# Example Usage
if __name__ == "__main__":
    clock = SystemClock()
    print(f"Initial time: {clock.get_current_time()}")

    clock.fast_forward(hours=1, minutes=30)
    clock.rewind(minutes=15)
    clock.set_time(2025, 7, 16, 10, 0, 0)
