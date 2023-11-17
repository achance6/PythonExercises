class SpaceAge:
    SEC_IN_MIN = 60
    MIN_IN_HOUR = 60
    HOUR_IN_DAY = 24
    DAY_IN_EARTH_YEAR = 365.25
    planets_orbital_period = {'Mercury': 0.2408467, 'Venus': 0.61519726,
                              'Earth': 1.0, 'Mars': 1.8808158, 
                              'Jupiter': 11.862615, 'Saturn': 29.447498, 
                              'Uranus': 84.016846, 'Neptune': 164.79132}

    def __init__(self, seconds):
        self.age_seconds = seconds

    def on_mercury(self):
        return round(SpaceAge.seconds_to_earth_years(self.age_seconds) / 
                SpaceAge.planets_orbital_period['Mercury'], 2)
    
    def on_venus(self):
        return round(SpaceAge.seconds_to_earth_years(self.age_seconds) / 
                SpaceAge.planets_orbital_period['Venus'], 2)

    def on_earth(self):
        return round(SpaceAge.seconds_to_earth_years(self.age_seconds) / 
                SpaceAge.planets_orbital_period['Earth'], 2)
    
    def on_mars(self):
        return round(SpaceAge.seconds_to_earth_years(self.age_seconds) / 
                SpaceAge.planets_orbital_period['Mars'], 2)
    
    def on_jupiter(self):
        return round(SpaceAge.seconds_to_earth_years(self.age_seconds) / 
                SpaceAge.planets_orbital_period['Jupiter'], 2)
    
    def on_saturn(self):
        return round(SpaceAge.seconds_to_earth_years(self.age_seconds) / 
                SpaceAge.planets_orbital_period['Saturn'], 2)
    
    def on_uranus(self):
        return round(SpaceAge.seconds_to_earth_years(self.age_seconds) / 
                SpaceAge.planets_orbital_period['Uranus'], 2)
    
    def on_neptune(self):
        return round(SpaceAge.seconds_to_earth_years(self.age_seconds) / 
                SpaceAge.planets_orbital_period['Neptune'], 2)

    @staticmethod
    def seconds_to_earth_years(seconds: int) -> float:
        return (seconds / 
                SpaceAge.SEC_IN_MIN / 
                SpaceAge.MIN_IN_HOUR / 
                SpaceAge.HOUR_IN_DAY / 
                SpaceAge.DAY_IN_EARTH_YEAR)

space = SpaceAge(31557600)
print(space.on_mercury())

