# expense-manager

This is an Expense Manger application, built using Django on top of Python.

-   Django Version: 4.1.7
-   Python Version: 3.9.6
-   PostgreSQL Version: 15

---

## Project Setup

### 1. Clone the repository

### 2. Dependencies

Install the dependencies by creating a virtual environment, followed by installation using the `requirements.txt` file

1. Virtual Environment

    ```Python
    python -m venv <name>
    source <name>/bin/activate
    ```

2. Requirements

    ```Python
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

### 3. Database

-   Create a database `expensemanage`
-   Owner/User : `postgres`
-   Password: `password`
-   Host: `localhost`
-   Port: `5432`

    In order to change the DB configurations, update the DATABASE configuration section in `settings.py` file

    ```Python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'expensemanager',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

-   In order to connect and apply the DB Schema, run the following command(s)

    ```Python
    python manage.py makemigrations
    python manage.py migrate
    ```

### 4. Creating Superuser

-   username: `<username>`
-   password: `<password>`

```python
python mange.py createsuperuser
```

### 5. Running the application

-   For Development Environment

    ```Python
    python manage.py runserver
    ```

-   For Production Environment(using gunicorn)

    ```Python
    gunicorn expense_manager.wsgi
    ```

---

## Running the Project

#### 1. Create superuser

#### 2. Generate Token using `/login` endpoint using superuser credentials

```Python
import requests
import json

url = "http://localhost:8000/login/"

payload = json.dumps({
  "username": "admin",
  "password": "admin"
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```

-   The token received in the above step can be used to as a Authorization Header.

-   For other users, use the `/api/v1/user` endpoint to perform CRUD operation(s)

-   To create an Expense category, use the `api/v1/expense_category` endpoint

-   To add an Expense, use the `/api/v1/expense` endpoint

-   To apply filters, keywords can be passed in the <b>params</b> section

-   For more details, click the [here](https://api.postman.com/collections/14667962-2a238661-79bf-442b-b0a3-a2ecb0ce03bb?access_key=PMAT-01GT1XWBPAH5E5TYE8XEN6YD1F) for the Postman Collection
