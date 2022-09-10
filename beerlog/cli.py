# import sys
# from .config import settings

# def main():
# print("Hello from", settings.NAME)
# print(sys.argv[1:])

import typer

main = typer.Typer(help="Beer Management Application")


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database"""
    print(name, style)


@main.command("list")
def list_(style: str):
    """Lists beers in database"""
    print(style)
