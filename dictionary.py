
'''
Convert "Jan" -> "January";
'''

monthConversions = {
    1: "January",
    2: "February",
    "Mar": 3,
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
str = monthConversions.get(2, "Not a valid key")
print(str)