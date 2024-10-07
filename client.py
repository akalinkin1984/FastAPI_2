import requests


# создание админа
response = requests.post(
    "http://127.0.0.1:8080/user",
    json={
        "name": "admin",
        "password": "admin",
        "role": "admin"
    },
)


# создание юзера
# response = requests.post(
#     "http://127.0.0.1:8080/user",
#     json={
#         "name": "user_3",
#         "password": "12345",
#     },
# )


# получение токена
# response = requests.post(
#     "http://127.0.0.1:8080/login",
#     json={
#         "name": "user_3",
#         "password": "12345",
#     },
# )


# получение юзера по id
# response = requests.get("http://127.0.0.1:8080/user/1")


# изменение юзера
# response = requests.patch("http://127.0.0.1:8080/user/2",
#                           json={
#                               'name': 'Sasha',
#                               'password': '12345',
#                                 },
#                           headers={"x-token": 'bfcff199-31f4-4949-9878-323c328f5c33'}
#                           )


# удаление юзера
# response = requests.delete(
#     "http://127.0.0.1:8080/user/5",
#     headers={"x-token": 'bfcff199-31f4-4949-9878-323c328f5c33'}
# )


# создание объявления
# response = requests.post(
#     "http://127.0.0.1:8080/advertisement",
#     json={
#         'title': 'Telephone',
#         'description': 'Samsung',
#         'price': 128.75,
#     },
#     headers={"x-token": 'bfcff199-31f4-4949-9878-323c328f5c33'}
# )


# поиск объявления по id
# response = requests.get("http://127.0.0.1:8080/advertisement/1")


# поиск объявления по полям
# response = requests.get("http://127.0.0.1:8080/advertisement?qs_params=Sam")


# изменение объявления
# response = requests.patch(
#     "http://127.0.0.1:8080/advertisement/2",
#     json={
#         "title": "New title2",
#     },
#     headers={"x-token": 'f327a2ad-97f0-42b4-abf6-2f138ec3c14b'},
# )


# удаление объявления
# response = requests.delete("http://127.0.0.1:8080/advertisement/2",
#                            headers={"x-token": '73661ec2-886f-43fe-937b-b8397abfc308'})


print(response.status_code)
print(response.json())
