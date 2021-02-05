# This file is part of AndroidRepo (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

from tortoise import fields
from tortoise import Tortoise
from tortoise.models import Model
    
    
class Modules(Model):
    id = fields.IntField(pk=True)
    url = fields.TextField()
    name = fields.TextField()
    version = fields.IntField()
    last_update = fields.IntField()
    

class Requests(Model):
    id = fields.IntField(pk=True)
    user = fields.IntField()
    time = fields.IntField()
    ignore = fields.IntField()
    request = fields.TextField()
    attempts = fields.IntField()


async def connect_database():
    await Tortoise.init(
        {
            "connections": {
                "bot_db": os.getenv("DATABASE_URL", "sqlite://bot/database/database.sqlite")
            },
            "apps": {"bot": {"models": [__name__], "default_connection": "bot_db"}},
        }
    )
    # Generate the schema
    await Tortoise.generate_schemas()
