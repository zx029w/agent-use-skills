"""
该模块用于计算并返回当前周的时间范围（从上周日到下周六），
主要用于周报标题中日期范围的自动生成。
"""

import datetime


def weekly_range():
    today = datetime.datetime.now()

    # Calculate last Sunday
    days_since_sunday = today.weekday() + 1
    last_sunday = today - datetime.timedelta(days=days_since_sunday)

    # Calculate next Saturday
    days_until_saturday = 5 - today.weekday()
    if days_until_saturday < 0:
        days_until_saturday += 7
    next_saturday = today + datetime.timedelta(days=days_until_saturday)

    return {
        "start_date": last_sunday.strftime("%Y.%m.%d"),
        "end_date": next_saturday.strftime("%Y.%m.%d"),
    }


if __name__ == "__main__":
    result = weekly_range()
    print(result)
