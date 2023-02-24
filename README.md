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
