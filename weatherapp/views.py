from django.contrib import messages
from django.shortcuts import render
import requests
import datetime
# Create your views here.

def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'pune'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid='
    PARAMS = {'units':'metric' }

    API_KEY = ''

    SEARCH_ENGINE_ID=''

    query= city + "1920x1080"
    page=1
    start= (page-1)*10 +1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']

    
    
    try:
        data=requests.get(url,params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()


        return render(request,'weather/index.html',{'description': description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occurred':False,'image_url': image_url})
    
    except:
        exception_occurred=True
        messages.error(request,'Entered data is not available to API')
        day=datetime.date.today()
        return render(request,'weather/index.html',{'description': 'Clear Sky','icon':'01d','temp':22,'day':day,'city':'pune','exception_occurred':exception_occurred})
