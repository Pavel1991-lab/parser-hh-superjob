import requests


class HH():
    def __init__(self):
        self.__count = 500

    def get_request(self):
        pages = int(self.__count / 100)
        params = {
            "page": 0,
            "per_page": 100
        }
        response = []
        for page in range(pages):
            params.update({"page": page})
            data = requests.get(f"https://api.hh.ru/vacancies", params=params)
            try:
                items = data.json()['items']
                for item in items:
                    if item['employer']['name'] in ['Барса', 'Яндекс', '7 этажей', 'МУЛЯВКА К.В', 'ПроТекст', 'Extent', 'Альбатрос', 'Семак С.А', 'Смарт Конекшн', 'MindSet']:
                        response.append(item)
            except KeyError:
                print("Ключ 'items' отсутствует в JSON-ответе")
        return response

a = HH()
print(a.get_request())


