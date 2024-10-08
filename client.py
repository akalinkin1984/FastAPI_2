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
# response = requests.get("http://127.0.0.1:8080/user/2")


# изменение юзера
# response = requests.patch("http://127.0.0.1:8080/user/2",
#                           json={
#                               'name': 'Petya',
#                               'password': '1234567',
#                                 },
#                           headers={"x-token": '1ef7258f-8757-4290-8b53-9d408cf24e13'}
#                           )


# удаление юзера
# response = requests.delete(
#     "http://127.0.0.1:8080/user/3",
#     headers={"x-token": '31f8f81d-cba3-431f-8ea8-822eb676e52d'}
# )


# создание объявления
# response = requests.post(
#     "http://127.0.0.1:8080/advertisement",
#     json={
#         'title': 'TV',
#         'description': 'Samsung',
#         'price': 130,
#     },
#     headers={"x-token": '1ef7258f-8757-4290-8b53-9d408cf24e13'}
# )


# поиск объявления по id
# response = requests.get("http://127.0.0.1:8080/advertisement/1")


# поиск объявления по полям
# response = requests.get("http://127.0.0.1:8080/advertisement?qs_params=TV")


# изменение объявления
# response = requests.patch(
#     "http://127.0.0.1:8080/advertisement/2",
#     json={
#         "title": "New title",
#     },
#     headers={"x-token": '31f8f81d-cba3-431f-8ea8-822eb676e52d'},
# )


# удаление объявления
# response = requests.delete("http://127.0.0.1:8080/advertisement/1",
#                            headers={"x-token": '31f8f81d-cba3-431f-8ea8-822eb676e52d'})


print(response.status_code)
print(response.json())
