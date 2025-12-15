from passlib.context import CryptContext

class PasswordManager:

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hash_password(cls,password:str)->str:
   
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls,password:str,hashed_password:str)->bool:
       return cls.pwd_context.verify(password,hashed_password)
    


"""here we have used class methods using static
1. we dont have create object and call the function
2.using class methods we can acess class varaible . in case static we cannot we have write whole Class.func_name"""