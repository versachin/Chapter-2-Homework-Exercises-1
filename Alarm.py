timenow = int(input("what is the time now? "))
hourswait = int(input("how many hours should we wait? "))
alarmtime = (hourswait % 24) + timenow
alarmtime = alarmtime % 24
alarmtime = alarmtime % 12
print(alarmtime)