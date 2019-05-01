# simple-weather
simple weather app based on Kivy (python gui)

## Installation
You will need
* Kivy
* PyOWM

the package versions are provided in the `requirements.txt` file just install them with `pip install -r requirements.txt`
Although `kivy` is based on pygame and SDL so you will need to install some system libs `libsdl1.2-dev` and `libfreetypes6-dev`, maybe others if they are not on your system yet. You may face problem installing pygame from source look online on how to get the prebuild packages as it is easier

## Run
You need to tweak two variables inside weatherapp.py
- API_KEY: free api key from 'open weather map', if you keep using mine we will lose it both :p
- CITY: change this to your city in the form 'CityName,Country_CODE'

then run `python weatherapp.py`
