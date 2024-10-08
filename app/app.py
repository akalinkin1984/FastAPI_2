import fastapi
from sqlalchemy.future import select

import crud
import models
import schema
from constants import STATUS_SUCCESS_RESPONSE
from dependencies import SessionDependency, TokenDependency
from lifespan import lifespan
import auth


app = fastapi.FastAPI(
    title="Advertisement service",
    version="0.0.1",
    description="...",
    lifespan=lifespan
)


@app.get("/advertisement/{adv_id}", response_model=schema.GetAdvResponse)
async def get_adv(adv_id: int, session: SessionDependency):
    adv = await crud.get_item(session, models.Advertisement, adv_id)
    return adv.dict


@app.post("/advertisement", response_model=schema.CreateAdvResponse)
async def create_adv(adv_json: schema.CreateAdvRequest, session: SessionDependency, token: TokenDependency):
    adv = models.Advertisement(**adv_json.dict(), author=token.user_id)
    adv = await crud.add_item(session, adv)
    return adv.id_dict


@app.patch("/advertisement/{adv_id}", response_model=schema.UpdateAdvResponse)
async def update_adv(
        adv_id: int,
        adv_json: schema.UpdateAdvRequest,
        session: SessionDependency,
        token: TokenDependency):
    adv = await crud.get_item(session, models.Advertisement, adv_id)

    if token.user.role == 'admin' or token.user_id == adv.author:
        adv_patch = adv_json.dict(exclude_unset=True)

        for field, value in adv_patch.items():
            setattr(adv, field, value)
        await crud.add_item(session, adv)
        return adv.id_dict
    raise fastapi.HTTPException(403, 'Not enough rights')


@app.delete("/advertisement/{adv_id}", response_model=schema.DeleteAdvResponse)
async def delete_adv(adv_id: int, session: SessionDependency, token: TokenDependency):
    adv = await crud.get_item(session, models.Advertisement, adv_id)
    if token.user.role == 'admin' or token.user_id == adv.author:
        await crud.delete_item(session, models.Advertisement, adv_id)
        return STATUS_SUCCESS_RESPONSE
    raise fastapi.HTTPException(403, 'Not enough rights')


@app.get("/advertisement", response_model=schema.SearchAdvResponse)
async def search_adv(qs_params: str, session: SessionDependency):
    query = (select(models.Advertisement).
             filter(models.Advertisement.title.contains(qs_params) |
                    models.Advertisement.description.contains(qs_params)))
    data = await session.execute(query)
    res = data.unique().scalars().all()

    return {'result': res}


@app.post("/login", response_model=schema.LoginResponse)
async def login(login_data: schema.LoginRequest, session: SessionDependency):
    query = select(models.User).where(models.User.name == login_data.name)
    user = await session.scalar(query)
    if user is None:
        raise fastapi.HTTPException(401, "User or password is incorrect")
    if not auth.check_password(login_data.password, user.password):
        raise fastapi.HTTPException(401, "User or password is incorrect")

    token = models.Token(user_id=user.id)
    token = await crud.add_item(session, token)
    return {"token": token.token}


@app.post("/user", response_model=schema.CreateUserResponse)
async def create_user(user_data: schema.CreateUserRequest, session: SessionDependency):
    user = models.User(**user_data.dict())
    user.password = auth.hash_password(user_data.password)
    await crud.add_item(session, user)

    return user.id_dict


@app.get("/user/{user_id}", response_model=schema.GetUserResponse)
async def get_user(user_id: int, session: SessionDependency):
    user = await crud.get_item(session, models.User, user_id)
    return user.dict


@app.patch("/user/{user_id}", response_model=schema.UpdateUserResponse)
async def update_user(
        user_id: int,
        user_json: schema.UpdateUserRequest,
        session: SessionDependency,
        token: TokenDependency):
    if token.user.role == 'admin' or token.user_id == user_id:
        user = await crud.get_item(session, models.User, user_id)
        user_patch = user_json.dict(exclude_unset=True)

        if 'password' in user_patch:
            user_patch['password'] = auth.hash_password(user_patch['password'])

        for field, value in user_patch.items():
            setattr(user, field, value)

        await crud.add_item(session, user)
        return user.id_dict
    raise fastapi.HTTPException(403, 'Not enough rights')


@app.delete("/user/{user_id}", response_model=schema.DeleteUserResponse)
async def delete_user(user_id: int, session: SessionDependency, token: TokenDependency):
    if token.user.role == 'admin' or token.user_id == user_id:
        await crud.delete_item(session, models.User, user_id)
        return STATUS_SUCCESS_RESPONSE
    raise fastapi.HTTPException(403, 'Not enough rights')
