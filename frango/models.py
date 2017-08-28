# -*- coding: utf-8 -*-
## Exemplo tirado do pwall

import os
import importlib
import inspect
import peewee
from frango.conf import settings

def get_database():
    # Create file and dir if needed
    if not os.path.exists(settings.DB_FILE):
        os.makedirs ('../databases/var/db/', 0700)
        f = open (settings.DB_FILE, 'w+')
        f.close()
    db = peewee.SqliteDatabase(settings.DB_FILE)
    db.connect()
    return db

class Model(peewee.Model):
    class Meta:
        database = get_database()

    def data_from_dict (self, dictionary, fields=None):
        self, e = self.get_or_create (id=dictionary['id'])
        if (fields != None):
            for key in fields:
                if ( key in self._meta.fields.keys()) and ( key in dictionary.keys() ):
                    self.__dict__['_data'][key] = dictionary[key]
        else:        
            for key in dictionary.keys():
                if key in self._meta.fields.keys():
                    self.__dict__['_data'][key] = dictionary[key]
        return self

def create_tables():
    list_models = []
    for module_name in settings.INSTALLED_APPS:
        module = importlib.import_module(module_name+'.models')
        # get a class list
        class_list = dir(module)
        # this creates a list of Model names
        for class_name in class_list:
            my_class = getattr(module, class_name)
            if type(my_class) == peewee.BaseModel:
                parents = inspect.getmro(my_class)
                if Model in parents:
                    #list_models.append(class_name)
                    list_models.append(my_class)
    # Removes frango.models.Model from the list
    ModelClass = getattr(importlib.import_module('frango.models'), 'Model')
    list_models.remove(ModelClass)
    #Now take that list and create the tables
    db = get_database()
    db.create_tables(list_models, safe=True)
    
# TODO temp
def mosta_set():
    print settings.DB_FILE



        
