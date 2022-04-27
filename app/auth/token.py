from datetime import datetime, timedelta
from jose import JWTError, jwt

from auth import schemas, models

# openssl rand -hex 32
SECRET_KEY = "6a9fd437411d75c6a5f9accf8fc49cd169c7e66eb764ee4e37027ccd876b3c38"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10 * 24 * 60


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# verify and send current user id, email
def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        id: int = payload.get("id")
        if (email, id) is None:
            raise credentials_exception
        token_data = schemas.User(id=id, email=email)
        return token_data
    except JWTError:
        raise credentials_exception
