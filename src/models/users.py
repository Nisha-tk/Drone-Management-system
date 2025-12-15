from sqlalchemy import Column, String , Enum
from sqlalchemy.orm import relationship
from src.db.base import Base
from src.enums.user_role import UserRole


class Users(Base):
    name = Column(String(100),nullable= False)
    email = Column(String,unique=True,nullable=False, index = True)
    password = Column(String,nullable= False)
    role = Column(Enum(UserRole), default = UserRole.VIEWER)

    missions = relationship("Missions", back_populates="operator")




    
    