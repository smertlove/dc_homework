import datetime
import json

from api import register_booking

class Booking:

    def __init__(self, room_name, start, end):

        if start > end:
            raise ValueError

        self.room_name = room_name
        self._start = start
        self._end   = end

        self._build_dependent_fields()

    def _build_dependent_fields(self):
        self.duration = (self._end - self._start).seconds // 60
        self.start_date = datetime.datetime.strftime(self._start, "%Y-%m-%d")
        self.end_date = datetime.datetime.strftime(self._end,   "%Y-%m-%d")
        self.start_time = datetime.datetime.strftime(self._start, "%H:%M")
        self.end_time = datetime.datetime.strftime(self._end,   "%H:%M")

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        if value > self._end:
            raise ValueError
        self._start = value
        self._build_dependent_fields()

    @start.deleter
    def start(self):
        self._start = None

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if value < self._start:
            raise ValueError
        self._end = value
        self._build_dependent_fields()

    @end.deleter
    def end(self):
        self._end = None

    def mk_dict(self):
        return {
            "room_name": self.room_name,
            "duration": self.duration,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "start_time": self.start_time,
            "end_time": self.end_time
            }



def create_booking(room_name, start, end):
    print("Начинаем создание бронирования")

    booking = Booking(room_name, start, end)
    try:
        result = register_booking(booking)
    except KeyError:
        result = False
        msg = "Комната не найдена"
    else:
        msg = ("Комната занята", "Бронирование создано")[result]
    finally:
        print("Заканчиваем создание бронирования")

    answer = {
        "created": result,
        "msg": msg,
        "booking": booking.mk_dict()
    }

    return json.dumps(answer)

def main():
    result = Booking(
        "Mail.ru",
        datetime.datetime(2022, 9, 1, 14),
        datetime.datetime(2022, 9, 1, 15, 15)
    )
    pprint(result.mk_json_string())

    result.start = datetime.datetime(2022, 9, 1, 9)

    pprint(result.mk_json_string())






if __name__ == "__main__":
    main()
