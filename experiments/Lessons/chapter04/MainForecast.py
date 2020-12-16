from source import daily, weekly
# from forecasts import today
import forecasts

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")

forecasts.today()

for number, outlook in enumerate(weekly.forecast(), 1):
  print(number, outlook)