import unittest
import datetime

import dataConverter as dt
import calCursor as cc

class TestStringMethods(unittest.TestCase):

    def test_week_bound(self):
        self.assertEqual(
            dt.DataConverter.get_week_bounds(datetime.datetime(2025, 2, 11)),
            (datetime.datetime(2025, 2, 10), datetime.datetime(2025, 2, 17))
        )

        self.assertEqual(
            dt.DataConverter.get_week_bounds(datetime.datetime(2025, 2, 2)),
            (datetime.datetime(2025, 1, 27), datetime.datetime(2025, 2, 3))
        )

        self.assertEqual(
            dt.DataConverter.get_week_bounds(datetime.datetime(2025, 2, 28)),
            (datetime.datetime(2025, 2, 24), datetime.datetime(2025, 3, 3))
        )

        self.assertEqual(
            dt.DataConverter.get_week_bounds(datetime.datetime(2025, 1, 1)),
            (datetime.datetime(2024, 12, 30), datetime.datetime(2025, 1, 6))
        )

    
    def test_plus_x_next_month(self):
        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 2, 11, 4, 55, 34), 3),
            datetime.datetime(2025, 5, 11, 4, 55, 34)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 1, 31, 4, 55, 34), 1),
            datetime.datetime(2025, 2, 28, 4, 55, 34)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 1, 31, 5, 55, 34), 5, dt.NEED_START),
            datetime.datetime(2025, 6, 1)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 1, 31, 4, 55, 34), 12),
            datetime.datetime(2026, 1, 31, 4, 55, 34)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 1, 31, 4, 55, 34), 13),
            datetime.datetime(2026, 2, 28, 4, 55, 34)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 1, 31, 4, 55, 34), 15, dt.NEED_START),
            datetime.datetime(2026, 4, 1)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 9, 30, 4, 55, 34), 16, dt.NEED_START),
            datetime.datetime(2027, 1, 1)
        )

    
    def test_negative_x_next_month(self):
        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 5, 11, 4, 55, 34), -3),
            datetime.datetime(2025, 2, 11, 4, 55, 34)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 3, 31, 4, 55, 34), -1),
            datetime.datetime(2025, 2, 28, 4, 55, 34)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 6, 30, 5, 55, 34), -5, dt.NEED_START),
            datetime.datetime(2025, 1, 1)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 1, 31, 4, 55, 34), -12),
            datetime.datetime(2024, 1, 31, 4, 55, 34)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 1, 31, 4, 55, 34), -24),
            datetime.datetime(2023, 1, 31, 4, 55, 34)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 1, 31, 4, 55, 34), -36),
            datetime.datetime(2022, 1, 31, 4, 55, 34)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 1, 31, 4, 55, 34), -13),
            datetime.datetime(2023, 12, 31, 4, 55, 34)
        )

        self.assertEqual(
            dt.DataConverter.get_x_next_month(datetime.datetime(2025, 4, 30, 4, 55, 34), -15, dt.NEED_START),
            datetime.datetime(2024, 1, 1)
        )
    

    def test_cal_cursor(self):
        testing_cursor = cc.calCursor()
        testing_cursor2 = cc.calCursor.from_datetime(datetime.datetime(
                *datetime.datetime.now().timetuple()[:5]
        ))
        self.assertEqual(testing_cursor._get_cursor_time(), testing_cursor2._get_cursor_time())


        testing_cursor = cc.calCursor.from_datetime(
            datetime.datetime(2025, 1, 1)
        )
        testing_cursor.alter_week(7)
        self.assertEqual(testing_cursor._get_cursor_time(), 
            datetime.datetime(2025, 2, 19)
        )

        testing_cursor.alter_week(-7)
        self.assertEqual(testing_cursor._get_cursor_time(),
            datetime.datetime(2025, 1, 1)
        )

        testing_cursor.alter_month(6)
        self.assertEqual(testing_cursor._get_cursor_time(),
            datetime.datetime(2025, 7, 1)
        )
        
        testing_cursor.alter_month(-10)
        self.assertEqual(testing_cursor._get_cursor_time(),
            datetime.datetime(2024, 9, 1)
        )


if __name__ == '__main__':
    unittest.main()