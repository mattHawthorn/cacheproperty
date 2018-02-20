=============
cacheproperty
=============


.. image:: https://img.shields.io/pypi/v/cacheproperty.svg
        :target: https://pypi.python.org/pypi/cacheproperty

.. image:: https://img.shields.io/travis/mattHawthorn/cacheproperty.svg
        :target: https://travis-ci.org/mattHawthorn/cacheproperty

.. image:: https://readthedocs.org/projects/cacheproperty/badge/?version=latest
        :target: https://cacheproperty.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/mattHawthorn/cacheproperty/shield.svg
     :target: https://pyup.io/repos/github/mattHawthorn/cacheproperty/
     :alt: Updates



A subclass of python's builtin property class that removes boilerplate by implementing the h_hidden_attribute pattern with a single decorator call. Also afacilitates invalidation of the cached hidden attribute with a @cacheproperty.invalidate decorator on any other methods or properties in a class.


* Free software: GNU General Public License v3
* Documentation: https://cacheproperty.readthedocs.io.


Features
--------



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
