import requests
import json
import os
import os.path
import hassapi as hass

class Get_Accu_ForeCast(hass.Hass):

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'en-US',
        'Host': 'dataservice.accuweather.com'
    }
        
    url_base = "https://dataservice.accuweather.com"
    url_forecast = '/forecasts/v1/daily/1day/298009?apikey=aYGshNEXSZFZtHAjAhWZGfGI56XsrHcT&language=en-us&details=true&metric=true'  

    def request(self):
        url = self.url_base + self.url_forecast
        response = requests.request("GET", url, headers = self.headers)
        return response.text

    def request_cached(self, date):
        path = './' + date + '.json'
        check_file = os.path.isfile(path)

        if check_file:
            f = open(path, "r")
            text = f.read() 
            return json.loads(text)
        else:
            text = self.request()
            f = open(path, "w")
            f.write(text)
            return json.loads(text)
        
    def load_sensor(self):
        path = './sensor.acc_day_rain_prob.txt'
        check_file = os.path.isfile(path)

        if check_file:
            f = open(path, "r")
            val = text = f.read()
            f.close()
            self.set_state("sensor.acc_day_rain_prob", state=int(val), replace=True, attributes={"friendly_name": "AccuWeather Day Rain Probability"})
        else:
            f = open(path, "a")
            f.write('0')
            f.close()
            self.set_state("sensor.acc_day_rain_prob", state=0, attributes={"friendly_name": "AccuWeather Day Rain Probability"})

    def set_sensor(self, val):
        path = './sensor.acc_day_rain_prob.txt'
        check_file = os.path.isfile(path)

        if check_file:
            os.remove(path)

        f = open(path, "a")
        f.write(str(val))
        f.close()

        self.set_state("sensor.acc_day_rain_prob", state=int(val), attributes={"friendly_name": "AccuWeather Day Rain Probability"})
   
    def initialize(self):
        
        result = self.request_cached('20231015')
        day = result['DailyForecasts'][0]['Day']
        prob = day['PrecipitationProbability']
        self.set_sensor(prob)

# print('HasPrecipitation:' + str(day['HasPrecipitation']))
# print('PrecipitationIntensity:' + str(day['PrecipitationIntensity']))
# print('PrecipitationProbability:' + str(day['PrecipitationProbability']))
# print('RainProbability:' + str(day['RainProbability']))
# print('TotalLiquid:' + str(day['TotalLiquid']))
# print('HoursOfPrecipitation:' + str(day['HoursOfPrecipitation']))

# night = result['DailyForecasts'][0]['Night']
# print('HasPrecipitation:' + str(night['HasPrecipitation']))
# print('PrecipitationIntensity:' + str(night['PrecipitationIntensity']))
# print('PrecipitationProbability:' + str(night['PrecipitationProbability']))
# print('RainProbability:' + str(night['RainProbability']))
# print('TotalLiquid:' + str(night['TotalLiquid']))
# print('HoursOfPrecipitation:' + str(night['HoursOfPrecipitation']))