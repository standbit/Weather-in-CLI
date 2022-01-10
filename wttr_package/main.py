import requests


def get_response(url):
    payload = {
        "nTqm": "",
        "lang": "ru"
        }
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
        if "error" in response.text:
            raise requests.exceptions.HTTPError(response.text["error"])
    except requests.exceptions.HTTPError as err:
        print("General Error")
        print(str(err))
    except requests.ConnectionError as err:
        print("Connection Error. Make sure you are connected to Internet.\n")
        print(str(err))
    return response.text


def main():
    locations = [
        "Лондон",
        "Шереметьево",
        "Череповец"
        ]
    for location in locations:
        url = "http://wttr.in/{}".format(location)
        print(get_response(url))


if __name__ == "__main__":
    main()
