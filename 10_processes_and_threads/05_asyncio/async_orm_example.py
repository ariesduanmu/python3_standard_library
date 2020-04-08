# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-03 14:36:47
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-03 16:08:35
import asyncio
import orm
import sqlalchemy
import databases
import uvicorn
import string
from random import choice

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from starlette.routing import Route


database = databases.Database("sqlite:///db.sqlite")
engine = sqlalchemy.create_engine(str(database.url))
metadata = sqlalchemy.MetaData(bind=engine)


USER_TABLENAME = "user"
GROUP_TABLENAME = "group"
USER_GROUP_TABLENAME = "user_group"

class User(orm.Model):
    __tablename__ = USER_TABLENAME
    __database__ = database
    __metadata__ = metadata
    
    id = orm.Integer(primary_key=True, allow_null=False)
    name = orm.String(max_length=50, allow_null=False) 
        
class Group(orm.Model):
    __tablename__ = GROUP_TABLENAME
    __database__ = database
    __metadata__ = metadata
    
    id = orm.Integer(primary_key=True, allow_null=False)
    name = orm.String(max_length=50, unique=True, allow_null=False)

class UserGroup(orm.Model):
    __tablename__ = USER_GROUP_TABLENAME
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True, allow_null=False)
    user = orm.ForeignKey(User)
    group = orm.ForeignKey(Group)

# metadata.create_all(engine)


async def create_user(name):
    user = await User.objects.create(name=name)
    return user

async def create_group(name):
    group = await Group.objects.create(name=name)
    return group.name

async def create_user_group(user, group):
    await UserGroup.objects.create(user=user, group=group)

async def random_name(i):
    name = f"{i}: "+"".join([choice(string.ascii_lowercase) for _ in range(8)])
    # await asyncio.sleep(5 - (0.1*i))

    return name

async def main(n):
    print('starting main')
            
    for i in range(n):
        await create_group(await random_name(i))
        
    print('finish main')


event_loop = asyncio.get_event_loop()
# try:
event_loop.run_until_complete(main(50))
# except:
#     event_loop.close()
# finally:
#     event_loop.close()



# async def create(request):




# async def homepage(request):
#     return JSONResponse({'hello':'world'})

# routes = [
#     Route("/", endpoint=homepage)
# ]

# app = Starlette(debug=True, routes=routes)

# if __name__ == "__main__":
#     uvicorn.run("starlette_example1:app", host="127.0.0.1", port=8000, log_level="info")