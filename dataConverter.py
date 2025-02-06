import datetime

class DataConverter:

    def convert_datetime_to_google_format(obj: datetime.datetime) -> str:
        """
        Returns string that can be used to make request to Google calendar
        """
        return obj.isoformat() + "Z"


    def get_week_start(obj: datetime.datetime) -> datetime.datetime:
        """
        Return start of the week in which obj is located
        """
        date = obj.date()
        number_of_day = date.isocalendar()[2]
        result = datetime.datetime(date.year, date.month, date.day)
        result -= datetime.timedelta(days=(number_of_day - 1))
        return result


    def get_week_bounds(obj: datetime.datetime) -> (datetime.datetime, datetime.datetime):
        """
        This function returns start and end of the week, based on time of the day of the needed week
        """
        start = DataConverter.get_week_start(obj)
        end = start + datetime.timedelta(days=7)
        return start, end