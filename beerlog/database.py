from sqlmodel import create_engine
from beerlog.config import settings

# impotar o model beer
from beerlog import models

engine = create_engine(settings.database.url)

# gerar a table no banco da model Beer
models.SQLModel.metadata.create_all(engine)
