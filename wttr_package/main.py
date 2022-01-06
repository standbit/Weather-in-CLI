import requests


URL_TEMPLATE = "http://wttr.in/{}"
LOCATIONS = [
    "Лондон?nTqm&lang=ru",
    "Шереметьево?nTqm&lang=ru",
    "Череповец?nTqm&lang=ru"]


def get_response():
    for item in LOCATIONS:
        url = URL_TEMPLATE.format(item)
        response = requests.get(url)
        print(response.text)


def main():
    get_response()


if __name__ == "__main__":
    main()
