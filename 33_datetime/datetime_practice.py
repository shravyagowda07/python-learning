from datetime import datetime
now = datetime.now()

today = datetime.now().date()

current_time = datetime.now().time()
print(now)
print(today)
print(current_time)

from datetime import datetime
now = datetime.now()
formatted = now.strftime("%d-%m-%Y")
print(formatted)

#timedelta
from datetime import datetime, timedelta
today = datetime.now()
tommorow = today + timedelta(days=1)
print(tommorow)


from datetime import datetime, timedelta
print("=== DATE & TIME PRACTICE ===")
now = datetime.now()
print("Current Date & Time:", now)
print("Date:", now.date())
print("Time:", now.time())

print("\nFormatted Date:")
print(now.strftime("%d-%m-%Y"))

print("\nFormatted Time:")
print(now.strftime("%H:%M:%S"))

tommorow = now + timedelta(days=1)

print("\nTommorow:", tommorow.strftime("%d-%m-%Y"))

