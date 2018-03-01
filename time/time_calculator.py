import datetime
# from django.utils import timezone


# returns the date after given days
# if true is passed, hence will be calculated backwords
def days_hence(d=1, back=False):
    if back:
        return datetime.datetime.now() - datetime.timedelta(days=d)
    return datetime.datetime.now() + datetime.timedelta(days=d)


# Ensure if the given age is adult, default is 18
# birth_date = datetime.date(1987, 8, 13)
def is_adult(birth_date=None, y=18):
    today = datetime.datetime.now().date()
    adult_date = (datetime.date(today.year - y, today.month, today.day) +
                  datetime.timedelta(hours=24))
    if birth_date > adult_date:
        return False
    return True
