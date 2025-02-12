from getData import DataGetter
from dataConverter import DataConverter, NEED_START
import datetime

class CalCursor:

    def __init__(self):
        DataGetter.auth()
        self.time=datetime.datetime(
            *datetime.datetime.now().timetuple()[:5]
        )
    
    @classmethod
    def from_datetime(cls, point: datetime.datetime):
        result = cls()
        result.time = point
        return result

    def alter_day(self, number: int) -> bool:
        try:
            self.time = self.time + datetime.timedelta(days=number)
            return True
        except:
            return False

    def alter_week(self, number: int) -> bool:
        try:
            self.time += datetime.timedelta(days=7*number)
            return True
        except:
            return False
    

    def alter_month(self, number: int) -> bool:
        try:
            self.time = DataConverter.get_x_next_month(self.time, number)
            return True
        except:
            return False
    

    def get_data_for_week(self) -> list:
        return DataGetter.get_for_week(self.time)

    def get_data_for_day(self) -> list:
        return DataGetter.get_for_day(self.time)
    
    def get_data_for_month(self) -> list:
        return DataGetter.get_for_month(self.time)

    def get_data_for_interval(self, start_time: datetime.datetime, end_time: datetime.datetime) -> list:
        return DataGetter.get_by_time(start_time, end_time)
    
    def _get_cursor_time(self) -> datetime.datetime:
        return self.time


    def __str__(self):
        return str(self.time)
    

    def __repr__(self):
        return str(self.time)