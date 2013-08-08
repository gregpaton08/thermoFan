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
        return -99.0

def getWeather():
    forecast = Forecastio("b8d1abd0c7da6a6c878e64015e78a8ee")
    result = forecast.load_forecast(39.960278, -74.978889,
                                   time=datetime.datetime.now(), units="si")
    
    if result['success'] is True:
        temp = (forecast.get_currently().temperature * 9.0 / 5.0) + 32
        return forecast.get_currently().summary
    else:
        return "FAIL"


def main():
    print(getWeather())
    print(getTemp())

if __name__ == "__main__":
    main()
