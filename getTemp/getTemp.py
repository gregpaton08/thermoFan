from forecastio import Forecastio
import datetime


def getTemp():
    forecast = Forecastio("b8d1abd0c7da6a6c878e64015e78a8ee")
    result = forecast.load_forecast(39.960278, -74.978889,
                                   time=datetime.datetime.now(), units="si")
    
    if result['success'] is True:
        temp = (forecast.get_currently().temperature * 9.0 / 5.0) + 32
        return temp
    else:
        print(result['response'])

def getWeather():
    forecast = Forecastio("b8d1abd0c7da6a6c878e64015e78a8ee")
    result = forecast.load_forecast(39.960278, -74.978889,
                                   time=datetime.datetime.now(), units="si")
    
    if result['success'] is True:
        temp = (forecast.get_currently().temperature * 9.0 / 5.0) + 32
        print(forecast.get_currently().summary)
        print(temp)
    else:
        print("FAIL")
        print(result['response'])


def main():
    forecast = Forecastio("b8d1abd0c7da6a6c878e64015e78a8ee")
    result = forecast.load_forecast(39.960278, -74.978889,
                                   time=datetime.datetime.now(), units="si")
    
    if result['success'] is True:
        temp = (forecast.get_currently().temperature * 9.0 / 5.0) + 32
        print(forecast.get_currently().summary)
        print(temp)
    else:
        print("FAIL")
        print(result['response'])

if __name__ == "__main__":
    main()
