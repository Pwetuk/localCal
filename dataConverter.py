import datetime
import calendar

NEED_START = True

class DataConverter:

    def convert_datetime_to_google_format(obj: datetime.datetime) -> str:
        """
        Returns string that can be used to make request to Google calendar
        """

        return (obj + datetime.timedelta(hours=-3)).isoformat() + "Z"

    def get_day_start(obj: datetime.datetime) -> datetime.datetime:

        date = obj.date()
        result = datetime.datetime(date.year, date.month, date.day)
        return result

    def get_week_start(obj: datetime.datetime) -> datetime.datetime:
        """
        Return start of the week in which obj is located
        """
        date = obj.date()
        number_of_day = date.isocalendar()[2]
        result = datetime.datetime(date.year, date.month, date.day)
        result -= datetime.timedelta(days=(number_of_day - 1))
        return result

    def get_month_start(obj: datetime.datetime) -> datetime.datetime:


        date = obj.date()
        result = datetime.datetime(date.year, date.month, 1)
        return result
    
    
    def get_week_bounds(obj: datetime.datetime) -> (datetime.datetime, datetime.datetime):
        """
        This function returns start and end of the week, based on time of the day of the needed week
        """
        start = DataConverter.get_week_start(obj)
        end = start + datetime.timedelta(days=7)
        return start, end

    def get_month_bounds(obj: datetime.datetime) -> (datetime.datetime, datetime.datetime):


        start = DataConverter.get_month_start(obj)
        if start.month != 12:
            end = datetime.datetime(start.year, start.month + 1, start.day)
        else:
            end = datetime.datetime(start.year + 1, start.month + 1, start.day)
        return start, end
    
    def get_day_bounds(obj: datetime.datetime) -> (datetime.datetime, datetime.datetime):
        
        start_day = DataConverter.get_day_start(obj)
        end_day = start_day + datetime.timedelta(days=1)

        return start_day, end_day

    def get_x_next_month(obj: datetime.datetime, number: int, need_start=False) -> datetime.datetime:
        """
        Returns datetime object after number of months. Number can be positive or negative. If negative function returns datetime of previous monthes.
        need_start parameter shows if should start of month or exact same day and time returened.
        If next month have less days than giving returns last day is used
        """

        days = obj.day
        months = obj.month + number - 1
        years = obj.year
        years += (months // 12) 
        
        if months >= 12 or months < 0:
            months = (months % 12)
        
        if need_start:
            new_time = datetime.time(0)
            days = 1
            
        else:
            new_time = obj.time()
        
        months += 1

        if calendar.monthrange(years, months)[1] < days:
            days = calendar.monthrange(years, months)[1]
        
        new_date = datetime.date(years, months, days)
        
        result_date = datetime.datetime.combine(new_date, new_time)
        
        return result_date