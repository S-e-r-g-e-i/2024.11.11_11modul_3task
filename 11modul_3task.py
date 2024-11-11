""" Домашнее задание по теме "Интроспекция" """
from pprint import pprint
import inspect


def introspection_info(obj):
    dict_info = {'1 Тип объекта:': type(obj),
                 '2 Атрибуты и методы объекта:': dir(obj),
                 '3 Модуль, к которому объект принадлежит:': inspect.getmodule(obj)}
    return dict_info


number_info = introspection_info(42)
pprint(number_info)

