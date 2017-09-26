# Chapter-2-Homework-Exercises-1
word1 = "All"
word2 = "work"
word3 = "and"
word4 = "no"
word5 = "play"
word6 = "makes"
word7 = "Jack"
word8 = "a"
word9 = "dull"
Sachin = "boy."
print(word1, word2, word3, word4, word5,
word6, word7, word8, word9, Sachin)




p=10000
n=12
r=.08
t=1
p * ((1 + r / n) ** (n * t))


total_secs = int(input("how many seconds, are left in the hour?"))
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
# minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60
print("Hrs=", hours, " mins=", minutes,
"secs=", secs_finally_remaining)

It doesnt let you run this twice




n = int(input("Enter the number of hours: "))
days = n // 24
timeafter = n % 24
if (timeafter > 10):
days = days + 1
hours = timeafter - 10
else:
hours = timeafter + 14
print("End time is in: ", days, " days, at ", hours, ":00 hours")
