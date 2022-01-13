import requests


def get_response(url):
    payload = {
        "nTqm": "",
        "lang": "ru"
        }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    if "error" in response.text:
        raise requests.exceptions.HTTPError(response.text)
    return response.text


def main():
    locations = [
        "Лондон",
        "Шереметьево",
        "Череповец"
        ]
    for location in locations:
        try:
            url = "http://wttr.in/{}".format(location)
            print(get_response(url))
        except requests.exceptions.HTTPError as err:
            print("General Error\n", str(err))
        except requests.ConnectionError as err:
            print("Connection Error. Check Internet connection.\n", str(err))


if __name__ == "__main__":
    main()
