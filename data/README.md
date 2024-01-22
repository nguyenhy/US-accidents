- [Source](#source)- [Source](#source)
- [Data dictionary](#data-dictionary)

## Source
- [US Accidents (2016 - 2023)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
- Visit paper: [A Countrywide Traffic Accident Dataset](https://arxiv.org/abs/1906.05409)
- [US State Abbreviation](https://www.bu.edu/brand/guidelines/editorial-style/us-state-abbreviations/)
- [COVID-19 Data Explorer](https://ourworldindata.org/explorers/coronavirus-data-explorer)

## Usage Policy and Legal Disclaimer
This dataset is being distributed solely for research purposes under the Creative Commons Attribution-Noncommercial-ShareAlike license (CC BY-NC-SA 4.0). By downloading the dataset, you agree to use it only for non-commercial, research, or academic applications. If you use this dataset, it is necessary to cite the papers mentioned above.

## Terminology
### Definition 3.1 (Traffic Event).
We define a traffic event e by `e =⟨lat,lng,time,type,desc⟩`, where
- lat and lng are GPS latitude and longitude
- type is the type of the event
- desc provides a natural language description of the event.
A traffic event is of one of the
following types: accident, broken-vehicle, congestion, construction, event, lane-blocked or flow-incident

### Definition 3.2 (Weather Observation Record). 
A weather observation w is defined by `w = ⟨lat, lng, time, temperature, humidity, pressure, visibility, wind−speed, precip, rain, snow, fog, hail⟩`. Here
- lat and lng represent the GPS coordinates of the weather station which reported w; 
- precip is the precipitation amount (if any)
- rain, snow, fog, and hail are binary indicators of these events.

### Definition 3.3 (Point-of-Interest).
A point-of-interest p is defined by `p = ⟨lat,lng,type⟩`. Here,
- lat and lng show the GPS latitude and longitude coordinates,
- available types for p are:
    - Amenity:
        Refers to particular places such as restaurant, library, college, bar, etc.
    - Bump:
        Refers to speed bump or hump to reduce the speed.
    - Crossing:
        Refers to any crossing across roads for pedestrians, cyclists, etc.
    - Give-way:
        A sign on road which shows priority of passing.
    - Junction:
        Refers to any highway ramp, exit, or entrance.
    - No-exit:
        Indicates there is no possibility to travel further by any transport mode along a formal path or route.
    - Railway:
        Indicates the presence of railways.
    - Roundabout:
        Refers to a circular road junction.
    - Station:
        Refers to public transportation station (bus, metro, etc.).
    - Stop:
        Refers to stop sign.
    - Traffic:
        Calming Refers to any means for slowing down traffic speed.
    - Traffic Signal:
        Refers to traffic signal on intersections.
    - Turning:
        Loop Indicates a widened area of a highway with a non-traversable island for turning around.
Table 1. Note that several of definitions in this table are adopted
from https://wiki.openstreetmap.org.

## Data dictionary

### ID
- Nullable: No
- Description: This is a unique identifier of the accident record.

### Severity
- Nullable: No
- Description: Shows the severity of the accident, a number between 1 and 4, where 1 indicates the least impact on traffic (i.e., short delay as a result of the accident) and 4 indicates a significant impact on traffic (i.e., long delay).

### Start_Time
- Nullable: No
- Description: Shows start time of the accident in local time zone.

### End_Time
- Nullable: No
- Description: Shows end time of the accident in local time zone. End time here refers to when the impact of accident on traffic flow was dismissed.

### Start_Lat
- Nullable: No
- Description: Shows latitude in GPS coordinate of the start point.

### Start_Lng
- Nullable: No
- Description: Shows longitude in GPS coordinate of the start point.

### End_Lat
- Nullable: Yes
- Description: Shows latitude in GPS coordinate of the end point.

### End_Lng
- Nullable: Yes
- Description: Shows longitude in GPS coordinate of the end point.

### Distance(mi)
- Nullable: No
- Description: The length of the road extent affected by the accident.

### Description
- Nullable: No
- Description: Shows natural language description of the accident.

### Number
- Nullable: Yes
- Description: Shows the street number in address field.

### Street
- Nullable: Yes
- Description: Shows the street name in address field.

### Side
- Nullable: Yes
- Description: Shows the relative side of the street (Right/Left) in address field.

### City
- Nullable: Yes
- Description: Shows the city in address field.

### County
- Nullable: Yes
- Description: Shows the county in address field.

### State
- Nullable: Yes
- Description: Shows the state in address field.

### Zipcode
- Nullable: Yes
- Description: Shows the zipcode in address field.

### Country
- Nullable: Yes
- Description: Shows the country in address field.

### Timezone
- Nullable: Yes
- Description: Shows timezone based on the location of the accident (eastern, central, etc.).

### Airport_Code
- Nullable: Yes
- Description: Denotes an airport-based weather station which is the closest one to location of the accident.

### Weather_Timestamp
- Nullable: Yes
- Description: Shows the time-stamp of weather observation record (in local time).

### Temperature(F)
- Nullable: Yes
- Description: Shows the temperature (in Fahrenheit).

### Wind_Chill(F)
- Nullable: Yes
- Description: Shows the wind chill (in Fahrenheit).

### Humidity(%)
- Nullable: Yes
- Description: Shows the humidity (in percentage).

### Pressure(in)
- Nullable: Yes
- Description: Shows the air pressure (in inches).

### Visibility(mi)
- Nullable: Yes
- Description: Shows visibility (in miles).

### Wind_Direction
- Nullable: Yes
- Description: Shows wind direction.

### Wind_Speed(mph)
- Nullable: Yes
- Description: Shows wind speed (in miles per hour).

### Precipitation(in)
- Nullable: Yes
- Description: Shows precipitation amount in inches, if there is any.

### Weather_Condition
- Nullable: Yes
- Description: Shows the weather condition (rain, snow, thunderstorm, fog, etc.)

### Amenity
- Nullable: No
- Description: A POI annotation which indicates presence of amenity in a nearby location.

### Bump
- Nullable: No
- Description: A POI annotation which indicates presence of speed bump or hump in a nearby location.

### Crossing
- Nullable: No
- Description: A POI annotation which indicates presence of crossing in a nearby location.

### Give_Way
- Nullable: No
- Description: A POI annotation which indicates presence of give_way in a nearby location.

### Junction
- Nullable: No
- Description: A POI annotation which indicates presence of junction in a nearby location.

### No_Exit
- Nullable: No
- Description: A POI annotation which indicates presence of no_exit in a nearby location.

### Railway
- Nullable: No
- Description: A POI annotation which indicates presence of railway in a nearby location.

### Roundabout
- Nullable: No
- Description: A POI annotation which indicates presence of roundabout in a nearby location.

### Station
- Nullable: No
- Description: A POI annotation which indicates presence of station in a nearby location.

### Stop
- Nullable: No
- Description: A POI annotation which indicates presence of stop in a nearby location.

### Traffic_Calming
- Nullable: No
- Description: A POI annotation which indicates presence of traffic_calming in a nearby location.

### Traffic_Signal
- Nullable: No
- Description: A POI annotation which indicates presence of traffic_signal in a nearby loction.

### Turning_Loop
- Nullable: No
- Description: A POI annotation which indicates presence of turning_loop in a nearby location.

### Sunrise_Sunset
- Nullable: Yes
- Description: Shows the period of day (i.e. day or night) based on sunrise/sunset.

### Civil_Twilight
- Nullable: Yes
- Description: Shows the period of day (i.e. day or night) based on civil twilight.

### Nautical_Twilight
- Nullable: Yes
- Description: Shows the period of day (i.e. day or night) based on nautical twilight.

### Astronomical_Twilight
- Nullable: Yes
- Description: Shows the period of day (i.e. day or night) based on astronomical twilight.

##
ID

Source, Description, Country

Severity, Distance(mi)

Start_Time, End_Time, Timezone,

Start_Lat, Start_Lng, End_Lat, End_Lng,  Street, City, County, State, Zipcode

Airport_Code, Weather_Timestamp, Temperature(F), Wind_Chill(F), Humidity(%), Pressure(in), Visibility(mi), Wind_Direction, Wind_Speed(mph), Precipitation(in), Weather_Condition,

Amenity, Bump, Crossing, Give_Way, Junction, No_Exit, Railway, Roundabout, Station, Stop, Traffic_Calming, Traffic_Signal, Turning_Loop,

Sunrise_Sunset, Civil_Twilight, Nautical_Twilight, Astronomical_Twilight,
