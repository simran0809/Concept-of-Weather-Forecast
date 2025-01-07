import random
                       #####  Weather Forecasting 

def winter_forecast():
 days = ['day1' , 'day2' , 'day3 ']
 forecast = {day : random.choice(["Snow","Rainy","Winter"])for day in days}
 return forecast
  
print(winter_forecast())