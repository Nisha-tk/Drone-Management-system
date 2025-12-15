from sqlalchemy.orm import Session
from src.models.users import Users
from src.schemas.user import UserCreate


class UserRepository:
    @staticmethod
    def get_by_email( db: Session, email: str)-> Users:
        return db.query(Users).filter(Users.email == email).first()
    

    @staticmethod
    def get_by_id( db: Session, user_id: int)-> Users:
        return db.query(Users).filter(Users.id == user_id).first()
    
    @staticmethod
    def create( db: Session, user)-> Users:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def list_Users( db: Session, skip: int = 0, limit: int = 10)-> list[Users]:
        return db.query(Users).offset(skip).limit(limit).all()

    @staticmethod
    def delete( db: Session, user: Users):
        db.delete(user)
        db.commit()
