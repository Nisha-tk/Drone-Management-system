from sqlalchemy.orm import DeclarativeBase , declared_attr 
from sqlalchemy import Column , Integer , DateTime , func , UUID
import uuid



class Base(DeclarativeBase):
    
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(UUID(as_uuid= True), primary_key=True, index=True, default= uuid.uuid4)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())







