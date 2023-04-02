
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def bcrpt(password: str):
        hashedPassword = pwd_cxt.hash(password)
        return hashedPassword

    def verify(hashedPass,plainPassword):
        return pwd_cxt.verify(plainPassword,hashedPass)
