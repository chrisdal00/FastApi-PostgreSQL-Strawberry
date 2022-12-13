# FastApi + PostgresSQL + Strawberry GraphQL
This is a simple application that shows how to do crud operations with both api rest and graphql controller.
The PostgresSQL database is wrapped into a docker container.

## Installation (Quick Start)
Install requirements
```
pip install -r /path/to/requirements.txt
```

## Getting started
Run Docker containers
```
cd .docker/
docker compose up -d
```
Run the application
```
cd .src/
uvicorn app:app --port 8000 --reload
```
or run as python file
```
cd .src/
python app.py
```


## Test
To use the REST Apis open Swagger
```
http://localhost:8000/docs
```

To use GraphQL open
```
http://localhost:8000/graphql
```

## Test GraphQL Queries
Here some examples of queries:
1) Get all users
```
query GetUsers {
  getUsers(limit: 10, skip: 10) {
    id
    email
    name
  }
}
```
2) Get user by email
```
query GetUserByEmail {
  getUserByEmail(email: "my_email@domain.com") {
    id
    name
  }
}
```
3) Get user by id
```
query GetUserById {
  getUserById(userId: 1) {
    id
    email
  }
}
```

## Test GraphQL Mutations
Here some examples of mutations:
1) Add user (if not exists)
```
mutation AddUser{
  addUser(
    name: "name", 
    email: "email@domain.com", 
    password: "super_secret"
  )
  {
    id
  }
}
```
2) Update user (if exists)
```
mutation UpdateUser{
  updateUser(
    userId: 1,
    name: "new name", 
    email: "new email", 
    password: "new super_secret"
  )
  {
    id
  }
}
```
3) Delete user (if exists)
```
mutation DeleteUser{
  deleteUser(
    userId: 20
  ){
    id
  }
}
```

## Teardown
Stop python application and docker containers
```
docker compose down
```
