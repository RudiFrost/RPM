import requests
import numpy as np
import gimme


def get_average_age(url):
    data = requests.get(url).json()
    list_year = []
    for i in data["response"]["items"]:
        try:
            data = i["bdate"]
            if len(data) > 2:
                list_year.append(int(data[-4:]))
                average = np.mean(list_year)
        except:
            pass

    return 2022 - average


print("Средний возраст друзей:", round(get_average_age(gimme.gimme_url_token()), 2))
