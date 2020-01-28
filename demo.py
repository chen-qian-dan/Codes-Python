
total = 1 + \
        2 + \
        3

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

print(days)





import datetime



def braces(values):
    '''
    :param values: an array of strings
    :return:
    '''
    no = "NO"
    yes = "YES"
    ret = []
    for s in values:
        while "()" in s or "[]" in s or "{}" in s:
            if "()" in s:
                s = s.replace("()", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            elif "{}" in s:
                s = s.replace("{}", "")
        if s:
            ret.append(no)
        else:
            ret.append(yes)

    return ret


dateIn = input()
year = int(dateIn[-4:])
month = int(dateIn[3:5])
day = dateIn[0:2]

day = 1

nextMeeting = datetime.date(year, month, day)

print(nextMeeting)

while nextMeeting.weekday() != 1:
    nextMeeting += datetime.timedelta(days = 1)


ret = "Tue-" + str(day) + "-" + str(month) + str(year) + ":("
#print(ret)

#print(nextMonth.weekday())






