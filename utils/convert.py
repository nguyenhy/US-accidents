def miles_to_meters(miles):
    return miles * 1609.34

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def inches_to_centimeters(inches):
    return inches * 2.54

def mph_to_kmh(mph):
    """
    - mph - miles per hour
    - kpm - kilometers per hour
    """
    return mph * 1.60934

def weekday_index_to_name(weekday_index):
    """
    Refers to pandas [weekday](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.weekday.html#pandas-datetimeindex-weekday)
    """

    return ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][weekday_index]
