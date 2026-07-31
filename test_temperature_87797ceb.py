from temperature_87797ceb import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
