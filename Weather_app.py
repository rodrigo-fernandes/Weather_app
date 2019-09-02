import requests
import json
import pprint

accuweatherAPIKey = 'npDVYLXnPFAZDyGOv3JghrMyBiyWu9bc'

r = requests.get('http://www.geoplugin.net/json.gp')

if (r.status_code != 200):
    print('Nao foi possível obter a localização')
else:
    localizacao = json.loads(r.text)
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']
    locationAPUUrl = "http://dataservice.accuweather.com/locations/v1/cities/" \
    + "geoposition/search?apikey=" + accuweatherAPIKey \
    + "&q=" + lat +"%2C" + long + "&language=pt-br"

    r2 = requests.get(locationAPUUrl)
    if(r.status_code != 200):
        print('Não foi possível obter o código do local')
    else:
        locationResponse = json.loads(r2.text)
        nomeLocal = locationResponse['LocalizedName'] + ", " \
                    + locationResponse['AdministrativeArea']['LocalizedName'] + "." \
                    + locationResponse['Country']['LocalizedName']
        codigoLocal = locationResponse['Key']
        print("Obtendo clima do local: ", nomeLocal)

        CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" \
                                  + codigoLocal + "?apikey=" + accuweatherAPIKey \
                                  + "&language=pt-br"
        r3 = requests.get(CurrentConditionsAPIUrl)
        if(r3.status_code != 200):
            print('Não foi possível obter o código do local')
        else:
            CurrentConditionsResponse = json.loads(r3.text)
            textoClima = CurrentConditionsResponse[0]['WeatherText']
            temperatura = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
            print('Clima no momento: ', textoClima)
            print('Temperatura: ' + str(temperatura) + 'graus Celsius')
        
