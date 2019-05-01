#_*_coding: utf-8_*_
import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


import pyowm

# Use your free API key from openweathermap
API_KEY = "72d1868964a13571511aad0ba972659c"
CITY    = "Paris,FR"
owm = pyowm.OWM(API_KEY)


# label with background pic WA
class LabelWithBackground(Label):
	pass

class WeatherScreen(BoxLayout):
	def reload(self):
		res = self.conditions()
		self.ids.wind.text = "Wind: {}".format(res.get("wind"))
		self.ids.hum.text = "Humidity: {}".format(res.get("hum"))
		self.ids.temp_min.text = "Min: {}°C".format(res.get("temp")[0])
		self.ids.temp_now.text = "Now: {}°C".format(res.get("temp")[1])
		self.ids.temp_max.text = "Max: {}°C".format(res.get("temp")[2])

	def conditions(self):
		# Change this to your city
		observation = owm.weather_at_place(CITY)
		w = observation.get_weather()
		tmp = w.get_temperature('celsius')
		wind = "{} miles/h".format(w.get_wind().get('speed'))
		hum = "{} %".format(w.get_humidity())
		temp = (
			tmp.get('temp_min'),
			tmp.get('temp'),
			tmp.get('temp_max')
			)
		return {"wind": wind, "hum": hum, "temp": temp}


class WeatherApp(App):
	def build(self):
		return WeatherScreen()


if __name__ == '__main__':
	WeatherApp().run()
