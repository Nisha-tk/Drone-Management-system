from  sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from src.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo = False)

sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    try:
        db = sessionlocal()
        yield db 
    finally:
        db.close()
        
            