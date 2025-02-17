from datetime import datetime, timedelta, time


def add_times_and_compare(time1_str, time2_str, compare_time_str):
    # 解析时间
    time1 = datetime.strptime(time1_str, "%H:%M:%S")
    time2 = datetime.strptime(time2_str, "%H:%M:%S")
    compare_time = datetime.strptime(compare_time_str, "%H:%M:%S").time()

    # 将时间转换为 timedelta
    delta1 = timedelta(hours=time1.hour, minutes=time1.minute, seconds=time1.second)
    delta2 = timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)

    # 相加时间
    total_delta = delta1 + delta2

    # 保证相加的结果不超过 24 小时
    total_seconds_in_a_day = 24 * 60 * 60
    total_delta_seconds = total_delta.total_seconds() % total_seconds_in_a_day
    result_time = (datetime.min + timedelta(seconds=total_delta_seconds)).time()

    print(f"相加后的时间是: {result_time}")

    # 比较相加后的时间和给定的 compare_time
    if result_time > compare_time:
        print(f"相加后的时间 {result_time} 在给定时间 {compare_time} 之后")
    elif result_time < compare_time:
        print(f"相加后的时间 {result_time} 在给定时间 {compare_time} 之前")
    else:
        print(f"相加后的时间 {result_time} 和给定时间 {compare_time} 相同")


if __name__ == '__main__':
    # 测试
    add_times_and_compare("12:30:15", "14:15:45", "03:00:00")

    time.strftime('12:00:00', "%HH:%MM:%SS")