# REST API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Installation
After you cloned the repository, you can install all the required dependencies by running
```
pip install -r requirements.txt
```

## API Register & Login

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`user/login` | POST | READ | Get token for access API Product & Transaction
`user/register` | POST | READ | Create an user

## API Product

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/product` | GET | READ | Get all products
`api/product/:id` | GET | READ | Get a single product
`api/product`| POST | CREATE | Create a new product
`api/product/:id` | PUT | UPDATE | Update a product
`api/product/:id` | DELETE | DELETE | Delete a product

## API Transaction

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/transaction` | GET | READ | Get all transactions
`api/transaction/:id` | GET | READ | Get a single transaction
`api/transaction`| POST | CREATE | Create a new transaction
`api/transaction/:id` | PUT | UPDATE | Update a transaction
`api/transaction/:id` | DELETE | DELETE | Delete a transaction



## Use
We can test the API using [Postman](https://www.postman.com/)


First, we have to start up Django's development server.
```
python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
http  http://127.0.0.1:8000/api/product/
```
we get:
```
{
    "detail": "Authentication credentials were not provided."
}
```
Instead, if we try to access with credentials:
```
http http://127.0.0.1:8000/api/product/2 "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
```
we get the product with id = 2
```
{
    "id": 2,
    "name": "Triasse Paket MCU Basic",
    "testtype": "Basic",
    "code": "TPMB001",
    "price": "1000",
    "created": "2022-01-17T10:18:58.551797Z",
    "updated": "2022-01-18T02:33:22.733927Z"
}
```

## Create users and Tokens

First we need to create a user, so we can log in
```
http POST http://127.0.0.1:8000/user/register email="email@email.com" username="USERNAME" password="PASSWORD" password2="PASSWORD" first_name="FIRSTNAME" last_name="LASTNAME" role="admin/customer"
```

After we create an account we can use those credentials to get a token

To get a token first we need to request
```
http http://127.0.0.1:8000/user/login username="username" password="password"
```
after that, we get the token
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA2MjIxLCJqdGkiOiJjNTNlNThmYjE4N2Q0YWY2YTE5MGNiMzhlNjU5ZmI0NSIsInVzZXJfaWQiOjN9.Csz-SgXoItUbT3RgB3zXhjA2DAv77hpYjqlgEMNAHps"
}
```
We got two tokens, the access token will be used to authenticated all the requests we need to make, this access token will expire after some time.
We can use the refresh token to request a need access token.

requesting new access token
```
http http://127.0.0.1:8000/user/login/refresh refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA"
```
and we will get a new access token
```
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
}
```

## Commands
### API Product
```
Get all product
http http://127.0.0.1:8000/api/product "Authorization: Bearer {YOUR_TOKEN}" 
Get a single product
http GET http://127.0.0.1:8000/api/product/{id} "Authorization: Bearer {YOUR_TOKEN}" 
Create a new product
http POST http://127.0.0.1:8000/api/product "Authorization: Bearer {YOUR_TOKEN}" {name="Triasse Paket MCU Premium" code="TPMP001" price=765000 testtype="Premium"} 
Full update a product
http PUT http://127.0.0.1:8000/api/product/{id} "Authorization: Bearer {YOUR_TOKEN}" {name="Triasse Paket Basic" code="TPMP002" price=100000 testtype="Basic"}
Partial update a product
http PATCH http://127.0.0.1:8000/api/product/{id} "Authorization: Bearer {YOUR_TOKEN}" {name="Triasse Paket Basic"} 
Delete a product
http DELETE http://127.0.0.1:8000/api/product/{id} "Authorization: Bearer {YOUR_TOKEN}"
```
### API Transaction
```
Get all transaction
http http://127.0.0.1:8000/api/transaction "Authorization: Bearer {YOUR_TOKEN}" 
Get a single transaction
http GET http://127.0.0.1:8000/api/transaction/{id} "Authorization: Bearer {YOUR_TOKEN}" 
Create a new transaction
http POST http://127.0.0.1:8000/api/transaction "Authorization: Bearer {YOUR_TOKEN}" array({productid=2 orderquantity=10},{productid=3 orderquantity=5}) 
Full update a transaction
http PUT http://127.0.0.1:8000/api/transaction/{id} "Authorization: Bearer {YOUR_TOKEN}" {userid=1 totalprice=100000}
Partial update a transaction
http PATCH http://127.0.0.1:8000/api/transaction/{id} "Authorization: Bearer {YOUR_TOKEN}" {userid=1}
Delete a transaction
http DELETE http://127.0.0.1:8000/api/transaction/{id} "Authorization: Bearer {YOUR_TOKEN}"
```

