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
        try:
            response.raise_for_status()
            if "error" in response.text:
                raise requests.exceptions.HTTPError(response.text["error"])
            print(response.text)
        except Exception as e:
            print('Ошибка при загрузке страницы: ' + str(e))


def main():
    get_response()


if __name__ == "__main__":
    main()
