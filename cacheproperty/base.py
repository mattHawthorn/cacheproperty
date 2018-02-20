# -*- coding: utf-8 -*-
"""A subclass of python's builtin property class that removes boilerplate by implementing the h_hidden_attribute pattern with a single decorator call. Also afacilitates invalidation of the cached hidden attribute with a `@cacheproperty.invalidate`
decorator on any other methods or properties in a class."""

from functools import wraps


class CacheProperty(property):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None, attr=None):
        helper = _CachePropertyHelper(fget=fget, fset=fset, fdel=fdel, attr=attr)
        super().__init__(fget=helper._fget, fset=helper._fset, fdel=helper._fdel)
        self.__doc__ = doc or (fget.__doc__ if fget is not None else None)
        self.helper = helper

    def invalidate(self, method):
        """Allows use of the `@mycacheproperty.invalidate` form of registering invalidators"""
        return self.helper.register_invalidator(method)


class _CachePropertyHelper:
    # this essentially acts like a mixin for CacheProperty, but we avoid pitfalls of
    # subclassing builtins by separating it into its own class
    def __init__(self, fget=None, fset=None, fdel=None, attr=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.attr = attr or '_' + fget.__name__

    def _fget(self, obj):
        """Getter for cached property attribute; gets the associated hidden attribute.
        If a getter is specified, optionally returns the result of the call to the getter
        after checking for the hidden attribute, and sets the hidden attribute to the
        result of the call before """
        if self.fget is None:
            return getattr(obj, self.attr)
        else:
            try:
                attr = getattr(obj, self.attr)
            except AttributeError:
                attr = self.fget(obj)
                setattr(obj, self.attr, attr)
        return attr

    def _fdel(self, obj):
        """Deleter for cached property attribute; removes the associated hidden attribute"""
        if self.fdel is None:
            delattr(obj, self.attr)
        else:
            self.fdel(obj)
            delattr(obj, self.attr)

    def _fset(self, obj, val):
        """Setter for cached property attribute; sets the associated hidden attribute,
        optionally to the return value of the wrapped function"""
        if self.fset is None:
            setattr(obj, self.attr, val)
        else:
            val_ = self.fset(obj, val)
            setattr(obj, self.attr, val_)

    def register_invalidator(self, f):
        inv = invalidate(self.attr)(f)
        return inv


def invalidate(*attrs):
    """Allows for registering multiple invalidators simultaneously by name"""
    def decorator(f):
        @wraps(f)
        def dec(self, *a, **kw):
            result = f(self, *a, **kw)
            for attr in attrs:
                if hasattr(self, attr):
                    delattr(self, attr)
            return result
        return dec
    return decorator


def cacheproperty(arg):
    if callable(arg):
        return CacheProperty(fget=arg)
    else:
        def dec(f):
            return CacheProperty(fget=f, attr=arg)
        return dec
