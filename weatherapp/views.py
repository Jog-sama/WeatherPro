from django.shortcuts import render
import requests
import datetime

def ConvertKtoC(K):

    # Convert the Fahrenheit into Celsius

    C = K - 273.15

    # Return the conversion value

    return round(C,2)

def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Mumbai'

    appid = '83ffbaaf71971f621175fb43360393bf'
    URL_CORD = 'http://api.openweathermap.org/geo/1.0/direct'
    PARAMS_CORD = {'q':city,'appid':appid}
    r_CORD = requests.get(url=URL_CORD,params=PARAMS_CORD)
    res_CORD = r_CORD.json()
    city_lat = res_CORD[0]['lat']
    city_lon = res_CORD[0]['lon']

    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'lat':city_lat, 'lon':city_lon,'appid':appid}
    r = requests.get(url=URL,params=PARAMS)
    res = r.json()

    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp_k = res['main']['temp']
    temp = ConvertKtoC(temp_k)

    day = datetime.date.today()


    return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})