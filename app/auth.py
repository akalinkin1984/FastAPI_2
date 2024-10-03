import bcrypt


def hash_password(password: str) -> str:
    password = password.encode()
    return bcrypt.hashpw(password, bcrypt.gensalt()).decode()


def check_password(password: str, hashed_password: str) -> bool:
    password = password.encode()
    hashed_password = hashed_password.encode()
    return bcrypt.checkpw(password, hashed_password)