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
                    if item['employer']['name'] in ['Барса', 'АРТИТЕРА']:
                        response.append(item)
            except KeyError:
                print("Ключ 'items' отсутствует в JSON-ответе")
        return response

    def get_name_employer(self):
        employer_names = [vacancy['employer']['name'] for vacancy in self.get_request()]
        return employer_names

    def get_adress_name_employer(self):
        employer_addresses = []
        for vacancy in self.get_request():
            employer = vacancy['employer']
            employer_name = employer['name']
            employer_address = vacancy['address']
            if employer_address is not None:
                employer_address = employer_address['raw']
            else:
                employer_address = None
            employer_info = {'employer_name': employer_name, 'employer_address': employer_address}
            employer_addresses.append(employer_info)

        return employer_addresses

        # for employer_info in employer_addresses:
        #     print('Работодатель:', employer_info['employer_name'])
        #     print('Адрес:', employer_info['employer_address'])
        #     print()


employers = HH()
name_adress = employers.get_adress_name_employer()
print(name_adress)


