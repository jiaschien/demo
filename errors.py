#!/usr/bin/env python
# -3- coding: utf-8 -3-
from __future__ import print_function

import sys

thismodule = sys.modules[__name__]


class BPUGBaseException(Exception):
    CODE = None

    def generate_message(self, **kwargs):
        raise NotImplementedError

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.message = self.generate_message(**kwargs)


class ErrorCodeDescriptor(object):
    """ A Descriptor to return A BPUGBaseException Subclass"""

    def __init__(self, code, func):
        self.code = code
        self.f = func

    def __get__(self, instance, base_class):
        if not base_class:
            base_class = type(instance)

        klass_name = ''.join([base_class.__name__, self.f.__name__])

        klass = getattr(thismodule, klass_name, None)
        if not klass:
            klass = type(klass_name, (base_class,), {'CODE': self.code, 'generate_message': self.f})
            setattr(thismodule, klass_name, klass)

        return klass


class error_code(object):
    def __init__(self, code):
        self.code = code

    def __call__(self, func):
        return ErrorCodeDescriptor(self.code, func)


# Namespaces are one honking great idea -- let's do more of those!
class Pythonista(BPUGBaseException):

    @error_code(10000)
    def NotFound(_, **kwargs):
        return kwargs

    @error_code(10001)
    def Blocked(_, **kwargs):
        return kwargs

    @error_code(100003)
    def Ugly(_, **kwargs):
        kwargs['reason'] = 'Uglyyyyyyyyyyyyyyyyyy'
        return kwargs


if __name__ == '__main__':
    # More Readable Raise & Catch
    # import errors
    # try:
    #   raise errors.Pythonista.NotFound(nickname='Adam Wen', mail='adam#zhihu.com', blog='www.darkof.com')
    # except errors.Pythonista.NotFound as e:
    #   print e.message['nickname']
    # except errors.Pythonista.Blocked:
    #   1 / 0

    def raise_some_error():
        raise Pythonista.NotFound(foo='bar', tip="member id invalid")

    # Readable Controll Flow
    try:
        raise_some_error()
    except Pythonista.NotFound:
        print('Member NotFound')
    except Pythonista.Blocked:
        print('Member Blocked')
    except Pythonista.Ugly:
        print('Internal Error')

    # Errors Tree
    try:
        raise_some_error()
    except Pythonista.NotFound as e:
        print(isinstance(e, Pythonista.NotFound))  # True
        print(isinstance(e, Pythonista))  # True
        print(isinstance(e, BPUGBaseException))  # True
        print(issubclass(Pythonista.NotFound, Pythonista))  # True
        print(issubclass(Pythonista.NotFound, BPUGBaseException))  # True

    # Exception with message and context
    try:
        raise_some_error()
    except Pythonista.NotFound as e:
        print(e.CODE == Pythonista.NotFound.CODE)  # True
        print(e.message)

    # Overwrite message generation
    try:
        raise Pythonista.Ugly
    except Pythonista.Ugly as e:
        print(e.message)
