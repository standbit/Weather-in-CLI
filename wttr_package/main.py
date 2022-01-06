import requests


URL_TEMPLATE = "http://wttr.in/{}"

LOCATIONS = [
    "Лондон",
    "Шереметьево",
    "Череповец"]

PAYLOAD = {
    "nTqm": "",
    "lang": "ru"
}


def get_response():
    for item in LOCATIONS:
        url = URL_TEMPLATE.format(item)
        response = requests.get(url, params=PAYLOAD)
        print(response.text)


def main():
    get_response()


if __name__ == "__main__":
    main()
