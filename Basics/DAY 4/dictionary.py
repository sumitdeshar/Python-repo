#key
monthCoversions = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthCoversions["Nov"] )
#print(monthCoversions["Maz"] ) not a valid key
print(monthCoversions.get("Maz","not a valid keys")) #but valid