import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA
import allure

BASE_URL = 'https://reqres.in/api/users'
EMAIL_ENDS = 'reqres.in'


@allure.suite('Проверка запросов с данными пользователей')
@allure.title('Метод проверящий список пользователей')
def test_list_users():
    with allure.step('Выполняем GET запрос'):
        response = httpx.get(BASE_URL + '?page=2')

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    users_data = response.json()['data']
    for item in users_data:
        with allure.step('Сверяем ответ с контрактом'):
            validate(item, USER_DATA_SCHEMA)

        with allure.step(f'Проверяем, что оканчивается на {EMAIL_ENDS}'):
            assert item['email'].endswith(EMAIL_ENDS)

    # print(item['email'])
    # print(item['first_name'])

    # json_response = response.json()
    # print(json_response['data'][0]) - вывод данных из блока data, 0

@allure.suite('Проверка запросов с данными пользователей')
@allure.title('Метод проверящий поддержку пользователей')
def test_support_users():
    with allure.step('Выполняем GET запрос'):
        response = httpx.get(BASE_URL + '/2')
    single_support_data = response.json()['support']