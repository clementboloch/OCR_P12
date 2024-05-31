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
    if response.status_code == 401:
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
    parameters = {k: v for k, v in parameters.items() if v}
    
    url = f'http://127.0.0.1:8000/crm/employee-modify/{id}/'

    make_authenticated_request(url=url, json = parameters, type=('patch'))


@app.command()
def employeelist():
    url = 'http://127.0.0.1:8000/crm/employee-list/'
    response = make_authenticated_request(url=url)
    print(response)

if __name__ == "__main__":
    app()
