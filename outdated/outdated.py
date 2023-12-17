'''
In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order,
formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
Date: 9/8/1636
1636-09-08
$ python outdated.py
Date: 8 September 1636
Date: September 8, 1636
1636-09-08
[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
'''
def main():
    month, day, year = getDate()
    print(f"{year}-{month:02}-{day:02}")

def getDate():
    months = ["January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"]
    while True:
        old_date = input("Date: ")
        if (old_date.find("/") != -1):
            month, day, year = old_date.split("/")
            try:
                month = int(month)
                day = int(day)
                year = int(year)
            except:
                pass
            else:
                if(1 <= month <= 12 and 1 <= day <= 31):
                    break
        elif (old_date.find(" ") != -1):
            try:
                split_date = old_date.split(" ")
                month = months.index(split_date[0].strip()) + 1
                day = int(split_date[1][:-1])
                year = int(split_date[2])
            except:
                pass
            else:
                if(1 <= month <= 12 and 1 <= day <= 31):
                    break

    return month, day, year

main()
