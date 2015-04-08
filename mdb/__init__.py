# Copyright (c) 2015

# author: plasmashadow.
#  company: StrawHatPirates.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software
"""
  MongoDB Models are just like ndb models where the user can persist
  the records with extending it with mdb.Model class.

  class Person(mdb.Model):
       name = mdb.StringProperty()
       age  = mdb.IntegerProperty()
       person_id = mdb.StringProperty(key = True)

  Note: that the primary key is set to custom key
"""
from Connection import *
from Property import *
from Document import *

class EngineException(Exception):
    pass


def create_engine(host=None, username=None, password=None, port=27017, database=None, create_new = False):
    """

    :type create_new: Used to denote whether the library can reuse
                      the existing session or not.
    """
    try:
        mongo_connection = AbstractConnection(host=host, username=username, password=password, port=port, database=database)
        _engine_connection = mongo_connection._connect(create_new)
        return getattr(_engine_connection, database)
    except Exception as e:
        raise EngineException("Unable to connect to mongodb")


