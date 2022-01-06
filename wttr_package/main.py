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


def get_response(url):
    response = requests.get(url, params=PAYLOAD)
    return response


def check_response(response):
    try:
        response.raise_for_status()
        if "error" in response.text:
            raise requests.exceptions.HTTPError(response.text["error"])
        return response.text
    except Exception as e:
        return "Ошибка при загрузке страницы: " + str(e)


def main():
    for item in LOCATIONS:
        url = URL_TEMPLATE.format(item)
        print(check_response(get_response(url)))


if __name__ == "__main__":
    main()
