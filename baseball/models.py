from django.db import models

# Create your models here.

class Stadiums(models.Model):
    city_name = models.CharField(max_length=200)
    timezone = models.IntegerField(default=0)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    city_id = models.IntegerField(default = 0)
    stadium_name =  models.CharField(max_length=200,primary_key=True)
    home_team = models.CharField(max_length=200)
    def __str__(self):
        return self.stadium_name

class Forecast(models.Model):
    city_id = models.CharField(max_length=200)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)    
    dt = models.IntegerField(default = 0)
    temp = models.FloatField(default = 0)
    feels_like = models.FloatField(default = 0)
    temp_min = models.FloatField(default=0)
    temp_max = models.FloatField(default=0)
    pressure = models.IntegerField(default=0)
    sea_level = models.IntegerField(default=0)
    grnd_level = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    temp_kf = models.FloatField(default=0)

    weather_id = models.IntegerField(default=0)
    weather_main = models.CharField(max_length = 200)
    weather_description = models.CharField(max_length = 200)
    clouds_all = models.IntegerField(default=0)

    wind_speed = models.FloatField(default=0)
    wind_deg = models.FloatField(default=0)
    wind_gust = models.FloatField(default=0)

    visibility = models.FloatField(default=0)

    df_txt = models.CharField(max_length = 200)

class GameSchedule(models.Model):
    game_id = models.CharField(max_length=200,primary_key=True)
    sport_key = models.CharField(max_length=200)
    sport_title = models.CharField(max_length=200)
    home_team = models.CharField(max_length=200)
    away_team = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    stadium_name=models.ForeignKey(Stadiums,on_delete=models.CASCADE)

class Odds(models.Model):
    game_id = models.ForeignKey(GameSchedule,on_delete=models.CASCADE)
    bookmaker = models.CharField(max_length=200)
    bookmaker_title = models.CharField(max_length=200)
    last_update = models.CharField(max_length=200)
    market_type= models.CharField(max_length=200)
    over_price = models.FloatField(default=0)
    over_point = models.FloatField(default=0)
    under_price= models.FloatField(default=0)
    under_point = models.FloatField(default=0)

    





