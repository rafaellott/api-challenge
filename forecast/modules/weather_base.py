from abc import abstractmethod


class BaseWeather(object):

    @abstractmethod
    def get_today_forecast(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_forecast_for_period(self, *args, **kwargs):
        pass
