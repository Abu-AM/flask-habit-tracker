import datetime


def date_range(start: datetime.date):
    return [start + datetime.timedelta(days=i) for i in range(-3, 4)]


if __name__ == "__main__":
    date_list = date_range(datetime.datetime.now())
    for date in date_list:
        print(date)
