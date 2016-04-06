import random

def answer(x, y, z):
    numbers = [x, y, z]

    month = [number for number in numbers if number <= 12]
    if len(month) == 3:
        if numbers[1:] == numbers[:-1]:
            return str(x).zfill(2) + '/' + str(y).zfill(2) + '/' + str(z).zfill(2)
        else:
            return "Ambiguous:", x, y, z
    if len(month) == 2:
        if month[0] == month[-1]:
            year = [number for number in numbers if number not in month][0]
            month, day = month
            if month in [1,3,5,7,8,10,12]:
                if year > 31:
                    return str(month).zfill(2) + '/' + str(day).zfill(2) + '/' + str(year).zfill(2)
                else:
                    return "Ambiguous:", x, y, z
            if month in [4,6,9,11]:
                if year > 30:
                    return str(month).zfill(2) + '/' + str(day).zfill(2) + '/' + str(year).zfill(2)
                else:
                    return "Ambiguous:", x, y, z
            if month in [2]:
                if year > 28:
                    return str(month).zfill(2) + '/' + str(day).zfill(2) + '/' + str(year).zfill(2)
                else:
                    return "Ambiguous:", x, y, z
        else:
            return "Ambiguous:", x, y, z
    if len(month) == 1:
        month = month[0]
        numbers.remove(month)

        def one_month_value(numbers, max_days):
            day = [number for number in numbers if number <= max_days]
            if len(day) == 2:
                if day[0] == day[-1]:
                    day, year = day
                    return str(month).zfill(2) + '/' + str(day).zfill(2) + '/' + str(year).zfill(2)
                else:
                    return "Ambiguous:", x, y, z
            if len(day) == 1:
                day = day[0]
                numbers.remove(day)
                year = numbers[0]
                return str(month).zfill(2) + '/' + str(day).zfill(2) + '/' + str(year).zfill(2)

        if month in [1,3,5,7,8,10,12]:
            return one_month_value(numbers, 31)
        if month in [4,6,9,11]:
            return one_month_value(numbers, 30)
        if month in [2]:
            return one_month_value(numbers, 28)

def run(a, b, c):
    randlist = [a, b, c]
    random.shuffle(randlist)
    x, y, z = randlist
    print "input:", randlist
    print "output:", answer(x, y, z)

#covers all possible dates + some non-dates
run(random.randint(1,99), random.randint(1,12), random.randint(1,31))

#covers all possible dates with a distinct year
run(random.randint(32,99), random.randint(1,12), random.randint(1,31))

#covers all possible dates with non-distinct month/day
run(random.randint(32,99), random.randint(1,12), random.randint(1,12))

#covers all possible dates with duplicate month/day
month_day = random.randint(1,12)
run(random.randint(32,99), month_day, month_day)

#covers all possible dates with all three values equal
month_day_year = random.randint(1,12)
run(month_day_year, month_day_year, month_day_year)

#if year and month have the same number, it is ambiguous
run(12, 15, 12)

#if year and day have the same number,
run(12, 15, 15)

#february
run(random.randint(1,99), 2, random.randint(1,28))

#covers all possible dates with duplicate day/year in february
day_year = random.randint(1,28)
run(day_year, 2, day_year)

run(27,2,27)

run(9,62,5)
