import requests


# response = requests.post(
#     "http://127.0.0.1:8080/advertisement",
#     json={
#         'title': 'Telephone',
#         'description': 'Samsung',
#         'price': 128.75,
#         'author': 'Ivan'
#     }
# )

# response = requests.get("http://127.0.0.1:8080/advertisement/3")

# response = requests.patch("http://127.0.0.1:8080/advertisement/3",
#                           json={
#                               'description': 'Iphone New Model',
#                               'price': 135.0,
#                                 }
#                           )

# response = requests.delete("http://127.0.0.1:8080/advertisement/1")

# response = requests.get("http://127.0.0.1:8080/advertisement?qs_params=Sam")

# print(response.status_code)
# print(response.json())

#____________________________________________________________________________

#создание юзера
# response = requests.post(
#     "http://127.0.0.1:8080/user",
#     json={
#         "name": "user_1",
#         "password": "12345",
#     },
# )
# print(response.status_code)
# print(response.json())


# получение токена
# response = requests.post(
#     "http://127.0.0.1:8080/login",
#     json={
#         "name": "user_1",
#         "password": "12345",
#     },
# )
# print(response.status_code)
# response_data = response.json()
# print(response_data)
# token = response_data["token"]


# создание объявления
response = requests.post(
    "http://127.0.0.1:8080/advertisement",
    json={
        'title': 'Telephone',
        'description': 'Samsung',
        'price': 128.75,
    },
    headers={"x-token": 'd1e090c6-2484-4d79-850d-9ccb325ffa32'}
)
print(response.status_code)
print(response.json())

# response = requests.patch(
#     "http://127.0.0.1:8080/advertisement/1",
#     json={
#         "title": "New title",
#     },
#     headers={"x-token": token},
# )

# print(response.json())
#
# response = requests.post(
#     "http://127.0.0.1:8080/advertisement",
#     json={
#         "title": "Title",
#         "description": "descr",
#     },
#     headers={"x-token": token}
# )

# print(response.json())


# response = requests.get(
#     "http://127.0.0.1:8080/advertisement/1",
#     json={
#         "title": "Title",
#         "description": "descr",
#     },
#     headers={"x-token": token}
# )

# print(response.json())

