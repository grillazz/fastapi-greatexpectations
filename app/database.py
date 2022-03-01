from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url = "postgresql://user:secret@db:5432/gxshakezz"

engine = create_engine(url, echo=True)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
