import inspect

import split_pool_mod_schema
from split_pool_mod_schema import Database

for name, obj in inspect.getmembers(split_pool_mod_schema):
    if inspect.isclass(obj):
        print(name)

x = Database(id="example:processes_db1")
