#!/usr/bin/env python
# encoding: utf-8

"""
    File name: book.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask.ext.restful import reqparse


# ------------ book add parser ------------
book_post_parser = reqparse.RequestParser()
book_post_parser.add_argument(
    'name', dest='name',
    type=unicode, location='form',
    required=True, help='The book\'s name',
)

book_post_parser.add_argument(
    'price', dest='price',
    type=float, location='form',
    required=True, help='The book\'s price',
)

book_post_parser.add_argument(
    'count', dest='count',
    type=int, location='form',
    required=True, help='The book\'s count',
)

book_post_parser.add_argument(
    'des', dest='des',
    type=unicode, location='form',
    required=False, help='The book\'s description',
)

# ------------ book update parser ------------
book_put_parser = reqparse.RequestParser()
book_put_parser.add_argument(
    'delta', dest='delta',
    type=int, location='form',
    required=True, help='The book\'s deviation',
)

book_put_parser.add_argument(
    'price', dest='price',
    type=float, location='form',
    required=True, help='The book\'s new price',
)

book_put_parser.add_argument(
    'des', dest='des',
    type=unicode, location='form',
    required=False, help='The book\'s new description',
)

book_put_parser.add_argument(
    'type_id', dest='type_ids', action='append',
    type=str, location='form',
    required=False, help='The book\'s new list of type id',
)
