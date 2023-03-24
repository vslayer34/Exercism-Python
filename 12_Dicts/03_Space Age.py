from helper import display_task_name, display_example
'''
Exersice: Space Age
URL: https://exercism.org/tracks/python/exercises/space-age

Instructions

Given an age in seconds, calculate how old someone would be on:

    Mercury: orbital period 0.2408467 Earth years
    Venus: orbital period 0.61519726 Earth years
    Earth: orbital period 1.0 Earth years, 365.25 Earth days, or 31557600 seconds
    Mars: orbital period 1.8808158 Earth years
    Jupiter: orbital period 11.862615 Earth years
    Saturn: orbital period 29.447498 Earth years
    Uranus: orbital period 84.016846 Earth years
    Neptune: orbital period 164.79132 Earth years

So if you were told someone were 1,000,000,000 seconds old, you should be able to say that they're 31.69 Earth-years old.

If you're wondering why Pluto didn't make the cut, go watch this YouTube video.

Note: The actual length of one complete orbit of the Earth around the sun is closer to 365.256 days (1 sidereal year). The Gregorian calendar has, on average, 365.2425 days. While not entirely accurate, 365.25 is the value used in this exercise. See Year on Wikipedia for more ways to measure a year.
'''

orbital_period = {
    'Mercury': 0.2408467,
    'Venus': 0.61519726,
    'Earth': 1.0,
    'Mars': 1.8808158,
    'Jupiter': 11.862615,
    'Saturn': 29.447498,
    'Uranus': 84.016846,
    'Neptune': 164.79132
}

EARTH_DAYS = (365.25, 31557600)


class SpaceAge:
    
    def __init__(self, seconds):
        self.seconds = seconds

    def seconds_per_year(planet_name: str):
        earth_seconds = EARTH_DAYS[1]
        orbital_period_to_earth = orbital_period[planet_name]
        
        return earth_seconds * orbital_period_to_earth


    def on_earth(self):
        return round(self.seconds / SpaceAge.seconds_per_year('Earth'), 2)
    
    def on_mercury(self):
        return round(self.seconds / SpaceAge.seconds_per_year('Mercury'), 2)
    
    def on_venus(self):
        return round(self.seconds / SpaceAge.seconds_per_year('Venus'), 2)
    
    def on_mars(self):
        return round(self.seconds / SpaceAge.seconds_per_year('Mars'), 2)
    
    def on_jupiter(self):
        return round(self.seconds / SpaceAge.seconds_per_year('Jupiter'), 2)
    
    def on_saturn(self):
        return round(self.seconds / SpaceAge.seconds_per_year('Saturn'), 2)
    
    def on_uranus(self):
        return round(self.seconds / SpaceAge.seconds_per_year('Uranus'), 2)
    
    def on_neptune(self):
        return round(self.seconds / SpaceAge.seconds_per_year('Neptune'), 2)
    
    
        


# Test 1
display_task_name("I", "SpaceAge > age on earth")
display_example('SpaceAge(1000000000).on_earth()', 31.69)
print(SpaceAge(1000000000).on_earth(), '\n')




# Test 2
display_task_name("II", "SpaceAge > age on mercury")
display_example('SpaceAge(2134835688).on_mercury()', 280.88)
print(SpaceAge(2134835688).on_mercury(), '\n')



# Test 3
display_task_name("III", "SpaceAge > age on venus")
display_example('SpaceAge(189839836).on_venus()', 9.78)
print(SpaceAge(189839836).on_venus(), '\n')



# Test 4
display_task_name("IV", "SpaceAge > age on mars")
display_example('SpaceAge(2129871239).on_mars()', 35.88)
print(SpaceAge(2129871239).on_mars(), '\n')



# Test 5
display_task_name("V", "SpaceAge > age on jupiter")
display_example('SpaceAge(901876382).on_jupiter()', 2.41)
print(SpaceAge(901876382).on_jupiter(), '\n')



# Test 6
display_task_name("VI", "SpaceAge > age on saturn")
display_example('SpaceAge(2000000000).on_saturn()', 2.15)
print(SpaceAge(2000000000).on_saturn(), '\n')



# Test 7
display_task_name("VII", "SpaceAge > age on uranus")
display_example('SpaceAge(1210123456).on_uranus()', 0.46)
print(SpaceAge(1210123456).on_uranus(), '\n')



# Test 8
display_task_name("VIII", "SpaceAge > age on neptune")
display_example('SpaceAge(1821023456).on_neptune()', 0.35)
print(SpaceAge(1821023456).on_neptune(), '\n')