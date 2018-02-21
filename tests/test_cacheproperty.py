#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cacheproperty` package."""

import pytest
from cacheproperty import cacheproperty, invalidate
from cacheproperty.base import CacheProperty


class Foo:
    @cacheproperty("foo_attr")
    def foo(self):
        """foo doc"""
        return 1

    @foo.invalidate
    def bar(self):
        """bar doc"""
        return "bar"

    @invalidate("foo")
    def bam(self):
        """bam doc"""
        return "bam"

    @property
    @invalidate("foo")
    def baz(self):
        """baz doc"""
        return "baz"


@pytest.fixture(scope="module")
def instance():
    return Foo()


def test_getter(instance):
    assert instance.foo == 1


def test_setter(instance):
    instance.foo = 2
    assert instance.foo == 2
    assert isinstance(instance.__class__.foo, CacheProperty)


def test_deleter(instance):
    instance.foo = 2
    del instance.foo
    assert instance.foo == 1


def test_cacheproperty_invalidate(instance):
    instance.foo = 2
    instance.bar()
    assert instance.foo == 1


def test_invalidate(instance):
    instance.foo = 2
    instance.bam()
    assert instance.foo == 1


def test_invalidating_property(instance):
    instance.foo = 2
    baz = instance.baz
    assert instance.foo == 1


def test_cacheproperty_doc(instance):
    assert instance.__class__.foo.__doc__ == "foo doc"


def test_cacheproperty_invalidate_doc(instance):
    assert instance.bar.__doc__ == "bar doc"


def test_invalidate_doc(instance):
    assert instance.bam.__doc__ == "bam doc"


def test_invalidating_property_doc(instance):
    assert instance.__class__.baz.__doc__ == "baz doc"
