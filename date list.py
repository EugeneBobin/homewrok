from datetime import date, timedelta


def get_date_list(from_date: str, to_date: str) -> list[str]:
    start_date = date.fromisoformat(from_date)
    end_date = date.fromisoformat(to_date)

    if start_date <= end_date:
        delta = timedelta(days=1)
        date_list = [start_date.isoformat()]
        while start_date < end_date:
            start_date += delta
            date_list.append(start_date.isoformat())
        return date_list
    else:
        delta = timedelta(days=-1)
        date_list = [start_date.isoformat()]
        while start_date > end_date:
            start_date += delta
            date_list.append(start_date.isoformat())
        return date_list


print(get_date_list("2023-06-04", "2023-09-10"))
