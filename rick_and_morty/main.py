import requests
import json


def parse():
    result = []
    a = {}
    b = {}
    r = requests.get(f'https://rickandmortyapi.com/api/character/?page=2')

    jsonData = r.json()['results']
    for person in jsonData[5:9]:
        result.append(person)
    for i in range(len(result)):
        b[result[i]['name']] = {
            "https://rickandmortyapi.com/api/character/" + str(result[i]['id']): result[i]['created']}
        a[result[i]['id']] = str(b).split(",")[i][1:]
    return a


if __name__ == '__main__':
    with open('when_created.json', 'w') as file:
        json.dump(parse(), file)
    file.close()
