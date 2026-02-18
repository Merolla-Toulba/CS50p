months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

date = input("Date: ").strip()

try:
    month, day, year = date.split("/")
    year = int(year)
    day = int(day)
    month = int(month)

    if month > 12:
        raise ValueError
    elif day > 31:
        raise ValueError

except Exception:

    try:
        initial = date.split(", ")
        month, day = initial[0].split(" ")
        year = initial[1]
        for i, mnth in enumerate(months):
            if mnth == month:
                number = i + 1
        month = number

        year = int(year)
        day = int(day)
        month = int(month)

        if day > 31:
            raise ValueError

    except Exception:
        date = input("Date: ").strip()


print(f"{year}-{month:02}-{day:02}")
