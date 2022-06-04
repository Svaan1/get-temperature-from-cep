from pycep_correios import get_address_from_cep, WebService
import requests

def get_city_from_cep(cep): # Usa a biblioteca dos correios e pega o endereço baseado no CEP.
    return get_address_from_cep(cep, webservice=WebService.VIACEP)['cidade']

def get_api_link(city):  # Forma o link da API com a cidade adquirida e a chave do usuário.
    API_KEY = "d1b815f1193a472142a2d79adcadb484" # Minha key da API "OpenWeather", https://openweathermap.org/.
    api_link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"

    return api_link

def get_api_request(link): # Faz o request da API com o link já completo.
    request_dictionary = requests.get(link).json()

    descricao = request_dictionary['weather'][0]['description'].capitalize()
    temperatura = request_dictionary['main']['temp'] - 273.15

    return f"{descricao} {temperatura:.2}ºC"

def get_temperature(cep): # Função principal, pega o CEP como input e retorna a temperatura e o clima local;
    city = get_city_from_cep(cep)
    api_link = get_api_link(city)
    temperature = get_api_request(api_link)
    return f"{city}: {temperature}"

def main():
    pass

if __name__ == "__main__":
    main()