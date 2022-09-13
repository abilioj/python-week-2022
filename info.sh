

ipython

python -i beerlog\models.py

beerlog

dir(Beer)
brewdog

from select import select

print(select(Beer))
print(select(Beer).where(Beer.name == "Brewdog"))

beerlog add "SuperBock" "Lager" --flavor=6 --image=3 --cost=8
beerlog add "shchoo" "beer" --flavor=6 --image=3 --cost=8
beerlog add "Letra" "Sour" --flavor=8 --image=5 --cost=5
beerlog add "Lagunitas" "IPA" --flavor=7 --image=6 --cost=8
-----------------------------------------------------------
-- sql
	insert into Beer (name, style, flavor, image, cost, rate, date)
	 values ("Brewdog", "NEIPA", 6, 5, 8, 6,"2022-09-09 9:23:50.219259");

-----------------------------------------------------------

    # valida campo de 1 a 10
    @validator("flavor","image","cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    # valida a pontuação da bebida,
    @validator("rate",always=True)
    def calculete_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)

	try:
	    brewdog = Beer(name="Brewdog", style="NEIPA", flavor=60, image=8, cost=8)
	except RuntimeError:
	    print("zika de mais")
	----------------------------------------
	# função do cli
	import sys
	from .config import settings

	def main():
		print("Hello from", settings.NAME)
		print(sys.argv[1:])

	----------------------------------------

-----------------------------------------------------------
	# -- CODE test ipython

	from sqlmodel import Session, select
	from beerlog.models import Beer
	from beerlog.database import engine

	with Session(engine) as session:
		sql = select(Beer)
		results = session.exec(sql)
		for beer in results:
			print(beer.name)

	with Session(engine) as session:
		beer = Beer(name="two chefs", style="QPA", flavor=5, image=6, cost=6)
		session.add(beer)
		session.commit()
		results = session.exec(select(Beer))
		for beer in results:
			print(beer.name)
-----------------------------------------------------------
- formata o codigo
black -l 79 beerlog

flake8 beerlog
################################################################################################################
# api
	# libs framework FastAPI
	from fastapi import FastAPI

	api = FastAPI(title="beerlog")

	# Para executar precisamos de um servidor ASGI e para isso usaremos o uvicorn
	poetry add uvicorn

	# Agora podemos executar a api com
	uvicorn beerlog.api:api --reload

	# Ao acessar https://localhost:8000/docs veremos a página de docs da api, e também temos a página /redoc