import datetime

import sqlalchemy as sq
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, relationship

from config import DSN

engine = create_async_engine(DSN)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):

    @property
    def id_dict(self):
        return {"id": self.id}


class Advertisement(Base):

    __tablename__ = 'advertisement'
    _model = "Advertisement"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(128), nullable=False, index=True)
    description = sq.Column(sq.String(256), nullable=False, index=True)
    price = sq.Column(sq.Float, nullable=False)
    author = sq.Column(sq.ForeignKey("user.id"))
    create_date = sq.Column(sq.DateTime, default=datetime.date.today())

    user = relationship("User", lazy="joined", back_populates="advs")

    @property
    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'author': self.author,
            'create_date': int(self.create_date.timestamp()),
        }


class User(Base):

    __tablename__ = "user"
    _model = "User"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100), unique=True, nullable=False)
    password = sq.Column(sq.String(72), nullable=False)
    tokens = relationship("Token", lazy="joined", back_populates="user")
    advs = relationship("Advertisement", lazy="joined", back_populates="user")
    role = sq.Column(sq.String(16), nullable=False, default='user')

    @property
    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "advs": self.advs}


class Token(Base):

    __tablename__ = "token"
    _model = "Token"

    id = sq.Column(sq.Integer, primary_key=True)
    token = sq.Column(
        sq.UUID,
        server_default=sq.func.gen_random_uuid(),
        unique=True,
    )
    creation_time = sq.Column(
        sq.DateTime, server_default=sq.func.now()
    )
    user_id = sq.Column(sq.ForeignKey("user.id"))
    user = relationship("User", lazy="joined", back_populates="tokens")

    @property
    def dict(self):
        return {
            "id": self.id,
            "token": str(self.token),
            "user_id": self.user_id,
            "creation_time": self.creation_time.isoformat(),
        }


ORM_OBJECT = Advertisement | User | Token
ORM_CLS = type[Advertisement] | type[User] | type[Token]
