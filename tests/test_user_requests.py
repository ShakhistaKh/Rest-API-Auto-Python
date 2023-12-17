import httpx
from jsonschema import validate

def test_list_users():
    response = httpx.get('https://reqres.in/api/users?page=2')
    assert response.status_code == 200

    json_response = response.json()
    # print(json_response['data'][0]) - вывод данных из блока data, 0

