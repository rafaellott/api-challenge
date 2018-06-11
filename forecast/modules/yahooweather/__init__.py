from forecast.modules.weather_base import BaseWeather
from weather import Weather, Unit


class YahooWeather(BaseWeather):

    def __init__(self, city, *args, **kwargs):
        self.weather = Weather(unit=Unit.CELSIUS)
        self.location = self.weather.lookup_by_location(city)
        super(YahooWeather, self).__init__(*args, **kwargs)

    def get_today_forecast(self):
        today = self.location.forecast[0]
        return today.text

    def get_forecast_for_period(self, start_time, end_time):
        pass
