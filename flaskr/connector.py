import json
import os

FILE_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/req')


class Connector:
    @classmethod
    def open_file_list(cls, file_name):
        with open(f'{FILE_ROOT}/{file_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    @classmethod
    def open_company(cls, file_name, pk):
        with open(f'{FILE_ROOT}/{file_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for i in data:
                if i['company_url'] == pk:
                    response = i
        return response

    @classmethod
    def open_person(cls, file_name, pk):
        with open(f'{FILE_ROOT}/{file_name}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for i in data:
                if i['profile_url'] == pk:
                    response = i
        return response
