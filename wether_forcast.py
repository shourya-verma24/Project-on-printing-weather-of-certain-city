import requests
input_city = input("Enter Any City in Inida,:")
URL = f"http://api.openweathermap.org/data/2.5/weather?q={input_city},IND&APPID=cee4064bda0a8a3712b2f8bbbdf2cf1a"
response= requests.get(URL)
print(response.status_code)
data = response.json()
Country = data["sys"]  
City = data["name"]
Actual_temp_Kelvin = data["main"]["temp"]
Actual_temp_celsius = Actual_temp_Kelvin - 273.15
print(Actual_temp_celsius,"Degree celsius")
print(Actual_temp_Kelvin,"in Kelvin")