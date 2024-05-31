import typer
from enum import Enum
import requests
from typing_extensions import Annotated

from datetime import datetime, date
import os
from pathlib import Path


class Department(str, Enum):
    c = 'Commercial'
    s = 'Support'
    m = 'Management'
    n = ''

app = typer.Typer()

TOKEN_URL = "http://127.0.0.1:8000/auth/login/"
TOKEN_FILE = Path("user_token.txt")

def get_token(
        email: str,
        password: str,
        ):
    response = requests.post(
        TOKEN_URL,
        data={"email": email,
              "password": password
              })
    response.raise_for_status()
    return response.json().get("access", "")


def save_token(token: str):
    with open(TOKEN_FILE, 'w') as file:
        file.write(token)

def read_token():
    if TOKEN_FILE.exists():
        with open(TOKEN_FILE, 'r') as file:
            return file.read().strip()
    return

@app.command()
def login(
    email: Annotated[str, typer.Option(prompt=True)],
    password: Annotated[str, typer.Option(prompt=True, hide_input=True)],
):
    try:
        token = get_token(email, password)
        save_token(token)
    except requests.HTTPError as e:
        typer.echo(f"Failed to log in: {e.response.text}", err=True)

def make_authenticated_request(
        url: str,
        json: dict = {},
        type: str = 'get',
        ):
    token = read_token()
    if not token:
        typer.echo("No authentication token found. Please log in first.", err=True)
        raise typer.Exit(code=1)
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    if type == 'get':
        r = requests.get
    elif type == 'post':
        r = requests.post
    elif type == 'patch':
        r = requests.patch
    else:
        return

    response = r(
        url,
        headers=headers,
        json=json,
        )
    if response.status_code in [401, 403]:
        typer.echo("You are not authorized or authentication token expired. Try to reconnect with 'login' command.", err=True)
    else:
        response.raise_for_status()
    return response.json()


@app.command()
def employeecreate(
    email:Annotated[str, typer.Option(prompt=True)],
    first_name:Annotated[str, typer.Option(prompt=True)],
    last_name:Annotated[str, typer.Option(prompt=True)],
    birthdate:Annotated[str, typer.Option(prompt=True)],
    group_name:Annotated[Department, typer.Option(prompt=True)],
    ):
    
    url = 'http://127.0.0.1:8000/auth/register/'
    parameters = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'birthdate': birthdate,
        'group_name': group_name.value,
    }

    r = make_authenticated_request(url=url, json = parameters, type='post')
    typer.echo(r)


@app.command()
def employeemodification(
    id:Annotated[int, typer.Option(prompt=True)],
    email:Annotated[str, typer.Option(prompt=True)] = "",
    first_name:Annotated[str, typer.Option(prompt=True)] = "",
    last_name:Annotated[str, typer.Option(prompt=True)] = "",
    birthdate:Annotated[str, typer.Option(prompt=True)] = "",
    group_name:Annotated[Department, typer.Option(prompt=True)] = Department.n,
    ):

    parameters = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'birthdate': birthdate,
        'group_name': group_name.value,
    }
    parameters = {k: v for k, v in parameters.items() if v not in ['', -1]}
    
    url = f'http://127.0.0.1:8000/crm/employee-modify/{id}/'

    r = make_authenticated_request(url=url, json = parameters, type='patch')
    typer.echo(r)


@app.command()
def passwordreset(
    email:Annotated[str, typer.Option(prompt=True)],
    token:Annotated[str, typer.Option(prompt=True)],
    new_password: Annotated[str, typer.Option(prompt=True, confirmation_prompt=True, hide_input=True)]
):
    parameters = {
        'email': email,
        'token': token,
        'new_password': new_password,
    }

    url = 'http://127.0.0.1:8000/auth/reset-password/'

    r = make_authenticated_request(url=url, json = parameters, type='post')
    typer.echo(r)


@app.command()
def employeelist():
    url = 'http://127.0.0.1:8000/crm/employee-list/'
    r = make_authenticated_request(url=url)
    typer.echo(r)


@app.command()
def clientlist():
    url = 'http://127.0.0.1:8000/crm/client-list/'
    r = make_authenticated_request(url=url)
    typer.echo(r)


@app.command()
def clientcreate(
    name:Annotated[str, typer.Option(prompt=True)],
    email:Annotated[str, typer.Option(prompt=True)] = '',
    phone:Annotated[str, typer.Option(prompt=True)] = '',
    company:Annotated[str, typer.Option(prompt=True)] = '',
    ):
    
    url = 'http://127.0.0.1:8000/crm/client-create/'
    parameters = {
        'name': name,
        'email': email,
        'phone': phone,
        'company': company,
    }

    parameters = {k: v for k, v in parameters.items() if v not in ['', -1]}

    r = make_authenticated_request(url=url, json = parameters, type='post')
    typer.echo(r)


@app.command()
def clientmodification(
    id:Annotated[int, typer.Option(prompt=True)],
    name:Annotated[str, typer.Option(prompt=True)] = '',
    email:Annotated[str, typer.Option(prompt=True)] = '',
    phone:Annotated[str, typer.Option(prompt=True)] = '',
    company:Annotated[str, typer.Option(prompt=True)] = '',
    ):

    parameters = {
        'name': name,
        'email': email,
        'phone': phone,
        'company': company,
    }
    parameters = {k: v for k, v in parameters.items() if v not in ['', -1]}
    
    url = f'http://127.0.0.1:8000/crm/client-modify/{id}/'

    r = make_authenticated_request(url=url, json = parameters, type='patch')
    typer.echo(r)


@app.command()
def contractlist():
    url = 'http://127.0.0.1:8000/crm/contract-list/'
    r = make_authenticated_request(url=url)
    typer.echo(r)


@app.command()
def contractcreate(
    client:Annotated[int, typer.Option(prompt=True)],
    amount:Annotated[float, typer.Option(prompt=True)] = -1,
    outstanding_amount:Annotated[float, typer.Option(prompt=True)] = -1,
    is_signed:Annotated[bool, typer.Option(prompt=True)] = False,
    ):

    url = 'http://127.0.0.1:8000/crm/contract-create/'
    parameters = {
        'client': client,
        'amount': amount,
        'outstanding_amount': outstanding_amount,
        'is_signed': is_signed,
    }

    parameters = {k: v for k, v in parameters.items() if v not in ['', -1]}

    r = make_authenticated_request(url=url, json = parameters, type='post')
    typer.echo(r)


@app.command()
def contractmodification(
    id:Annotated[int, typer.Option(prompt=True)],
    client:Annotated[int, typer.Option(prompt=True)] = -1,
    amount:Annotated[float, typer.Option(prompt=True)] = -1,
    outstanding_amount:Annotated[float, typer.Option(prompt=True)] = -1,
    is_signed:Annotated[bool, typer.Option(prompt=True)] = False,
    ):

    parameters = {
    'client': client,
    'amount': amount,
    'outstanding_amount': outstanding_amount,
    'is_signed': is_signed,
    }

    parameters = {k: v for k, v in parameters.items() if v not in ['', -1]}

    url = f'http://127.0.0.1:8000/crm/contract-modify/{id}/'

    r = make_authenticated_request(url=url, json = parameters, type='patch')
    typer.echo(r)


@app.command()
def eventlist():
    url = 'http://127.0.0.1:8000/crm/event-list/'
    r = make_authenticated_request(url=url)
    typer.echo(r)


@app.command()
def contractaddevent(
    contract:Annotated[int, typer.Option(prompt=True)],
    start_date:Annotated[str, typer.Option(prompt=True)] = '',
    end_date:Annotated[str, typer.Option(prompt=True)] = '',
    location:Annotated[str, typer.Option(prompt=True)] = '',
    attendees:Annotated[int, typer.Option(prompt=True)] = -1,
    notes:Annotated[str, typer.Option(prompt=True)] = '',
    support_contact:Annotated[int, typer.Option(prompt=True)] = -1,
    ):

    url = f'http://127.0.0.1:8000/crm/contract-add-event/{contract}/'
    parameters = {
        'start_date': start_date,
        'end_date': end_date,
        'location': location,
        'attendees': attendees,
        'notes': notes,
        'support_contact': support_contact,
    }

    parameters = {k: v for k, v in parameters.items() if v not in ['', -1]}

    r = make_authenticated_request(url=url, json = parameters, type='post')
    typer.echo(r)


@app.command()
def eventmodification(
    id:Annotated[int, typer.Option(prompt=True)],
    contract:Annotated[int, typer.Option(prompt=True)] = -1,
    start_date:Annotated[str, typer.Option(prompt=True)] = '',
    end_date:Annotated[str, typer.Option(prompt=True)] = '',
    location:Annotated[str, typer.Option(prompt=True)] = '',
    attendees:Annotated[int, typer.Option(prompt=True)] = -1,
    notes:Annotated[str, typer.Option(prompt=True)] = '',
    support_contact:Annotated[int, typer.Option(prompt=True)] = -1,
    ):

    parameters = {
        'contract': contract,
        'start_date': start_date,
        'end_date': end_date,
        'location': location,
        'attendees': attendees,
        'notes': notes,
        'support_contact': support_contact,
    }

    parameters = {k: v for k, v in parameters.items() if v not in ['', -1]}

    url = f'http://127.0.0.1:8000/crm/event-modify/{id}/'

    r = make_authenticated_request(url=url, json = parameters, type='patch')
    typer.echo(r)

if __name__ == "__main__":
    app()
