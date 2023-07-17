import requests

API_KEY = "b064dcc24f254d870121408d152c7f14"
def get_data(place, days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    print(get_data(place="Tokyo"))
