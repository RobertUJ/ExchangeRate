# Exhange Rate

This is a API that provide Exhange Rate from Dollar USD to Mexican Pesos.

### How works
This api runs a background task that updates currencies every hour. 


## Installation

This app uses docker.

To start the project, execute the next commands.

```bash
# To build docker containers
docker-compose build

# To start containers
docker-compose up -d
```

#### Run this command to create a user and fallow the instructions.
```bash
docker exec -ti exchangerate_django_1 python manage.py createsuperuser
```

## Usage

```bash
# Step 1
# To get token.

# Note: Change the email and password entered in the previous step.
# and take the item access
 
 curl \
 http://localhost:8000/api/v1/token/ \
 -d "email=rob@gmail.com&password=root"


# Step 2
# To get Exchange rates 

 curl \
 http://localhost:8000/api/v1/foreign_exchange/ \
 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI1NTI3MjI0LCJqdGkiOiJlODZiYmFhODQ0NjE0MzUyYTQ2NDVmOWEyNDNjNmRhMiIsInVzZXJfaWQiOjF9.hiI__ADRu2NO6OeGDsMZ8xrGLr0-GWy-IC4DaSu1gjw"

# Note: Replace the token with the one obtained above.

```

## Finally

You can see the next format:

```json
[
  {
    "provider": "Diario oficial de la federación",
    "value": "20.0368",
    "created": "2021-07-05T05:54:16.815907-05:00"
  },
  {
    "provider": "Fixer",
    "value": "19.7996",
    "created": "2021-07-05T05:54:16.689327-05:00"
  },
  {
    "provider": "Banxico",
    "value": "19.8817",
    "created": "2021-07-05T05:54:16.797277-05:00"
  }
]
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
