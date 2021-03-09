Sudoku solver
===============

|python|

This project is Python implementation of a sudoku solver using CSPs. It was made during our scholarship at UQAC.

Requirements
============

In order to run the code properly, some packages need to be installed. Fortunately, you can easily install
them by using pipenv.

- First, verify that pip is installed :

.. code-block:: console

    $ pip --version

if not, `install it <https://pip.pypa.io/en/stable/installing/>`_.

When it is done, let's continue the installation :

- install pipenv :

.. code-block:: console

    $ pip install --user pipenv

- once it is installed and well configured, run your environment :

.. code-block:: console

    $ pipenv shell

Run the code
============

Before you can have some fun solving some great Sudokus (at least try to solve them by yourself before using our amazing
algorithm), you should at least know how to run the code. So here are all the commands yet implemented :

- Run default (easy sudoku, the first one, with AC3 algorithm) :

.. code-block:: console

    $ python -m Sudoku

- Choose an other sudoku (between 1 and 6) :

.. code-block:: console

    $ python -m Sudoku -sn 3

- Change the difficulty (easy, hard and extreme are available) :

.. code-block:: console

    $ python -m Sudoku -d hard

- Run with or without AC3 algorithm :

.. code-block:: console

    $ python -m Sudoku -ac3 False

.. |python| image:: https://img.shields.io/github/pipenv/locked/python-version/camillebenoit/Sudoku_solver
    :target: https://www.python.org/downloads/release/python-386/
