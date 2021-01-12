#Create a Time Converter. Get the number of seconds from user and display in the form print(hours, "hr,", minutes, "min,", seconds, "sec")

time = float(input("Input time in seconds: "))
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print('hours "%d",minutes "%d",seconds "%d" '%(hour,minutes,seconds))
