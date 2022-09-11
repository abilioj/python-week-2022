import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database

#formatar o retornou em tabela
from rich.table import Table
from rich.console import Console

main = typer.Typer(help="Beer Management Application")

console = Console()

@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database"""
    if add_beer_to_database(
        name=name, style=style, flavor=flavor, image=image, cost=cost
    ):
        print("Beer Added to Database!")
    else:
        print("Error")


@main.command("list")
# não pode coloca o nome 'list' na fucao, pois 'list' é uma palavra reservada. por isso 'list_beers'
def list_beers(style: Optional[str] = None):
    """Lists beers in database"""
    beers = get_beers_from_database()
    # criando uma tabela
    table = Table(title="Beerlog :beer_mug:")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        # formatar a data
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)

