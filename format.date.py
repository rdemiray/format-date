
import unittest
from enum import Enum

class DateFormat(Enum):
    MMDDYYYY = 1
    DDMMYYYY = 2
    YYYYMMDD = 3
    YYYYDDMM = 4
    DDYYYYMM = 5
    MMYYYYDD = 6


def format_date(date, separator, format_type):
    # Input date format: 07-05-2025(MM-DD-YYYY)

    print("\nInput date:", date)
    print("Separator:", separator)
    print("Requested format type:", format_type.name)

    splitDate = date.split("-")
    month = splitDate[0]
    day = splitDate[1]
    year = splitDate[2]

    formatted_date = ""

    if format_type == DateFormat.MMDDYYYY:
        formatted_date = f"{month}{separator}{day}{separator}{year}"
    elif format_type == DateFormat.DDMMYYYY:
        formatted_date = f"{day}{separator}{month}{separator}{year}"
    elif format_type == DateFormat.YYYYMMDD:
        formatted_date = f"{year}{separator}{month}{separator}{day}"
    elif format_type == DateFormat.YYYYDDMM:
        formatted_date = f"{year}{separator}{day}{separator}{month}"
    elif format_type == DateFormat.DDYYYYMM:
        formatted_date = f"{day}{separator}{year}{separator}{month}"
    elif format_type == DateFormat.MMYYYYDD:
        formatted_date = f"{month}{separator}{year}{separator}{day}"

    print("Formatted date:", formatted_date)
    return formatted_date


class TestClass(unittest.TestCase):

    test_data = [
        # Seperator tests
        (["07-05-2025", "/", DateFormat.YYYYMMDD], "2025/07/05"),
        (["07-05-2025", "-", DateFormat.YYYYMMDD], "2025-07-05"),
        (["07-05-2025", "#", DateFormat.YYYYMMDD], "2025#07#05"),

        # All combinations of date formats
        (["07-05-2025", "/", DateFormat.YYYYDDMM], "2025/05/07"),
        (["07-05-2025", "/", DateFormat.DDMMYYYY], "05/07/2025"),
        (["07-05-2025", "/", DateFormat.MMDDYYYY], "07/05/2025"),
        (["07-05-2025", "/", DateFormat.DDYYYYMM], "05/2025/07"),
        (["07-05-2025", "/", DateFormat.MMYYYYDD], "07/2025/05"),


    ]

    def test_method(self):
        for data in self.test_data:
            self.assertEqual(
                format_date(data[0][0], data[0][1], data[0][2]),
                data[1]
            )



if __name__ == "__main__":
    unittest.main()
    
            
