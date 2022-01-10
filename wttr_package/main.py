import requests


def get_response(url):
    payload = {
        "nTqm": "",
        "lang": "ru"
        }
    response = requests.get(url, params=payload)
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
    locations = [
    "Лондон",
    "Шереметьево",
    "Череповец"]
    for location in locations:
        url = "http://wttr.in/{}".format(location)
        print(check_response(get_response(url)))


if __name__ == "__main__":
    main()
