# get-temperature-from-cep
Returns local temperature with the CEP as input.

## Libraries used
- Requests (To access the API's URL)
- Pycep_correios (Getting the CEP's city name)

## Used APIs
- OpenWeather (Getting local temperature and climate description. https://openweathermap.org/)

## How to use

Dont forget to get your own key on the given link and change API_KEY's value

Example of function calling:
```
get_temperature("25961-025")
```

