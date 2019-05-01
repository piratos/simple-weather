import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


import pyowm

API_KEY = "72d1868964a13571511aad0ba972659c"
owm = pyowm.OWM(API_KEY)


# label with background pic WA
class LabelWithBackground(Label):
	pass

class WeatherScreen(BoxLayout):
	def reload(self):
		res = self.conditions()
		self.ids.wind.text = res.get("wind")
		self.ids.hum.text = res.get("hum")
		self.ids.temp.text = res.get("temp")

	def conditions(self):
		observation = owm.weather_at_place('London,GB')
		w = observation.get_weather()
		tmp = w.get_temperature('celsius')
		wind = "{} miles/h".format(w.get_wind().get('speed'))
		hum = "{} %".format(w.get_humidity())
		temp = "Min: {}°C \nNow: {}°C \nMax: {}°C".format(
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