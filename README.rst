==============================
Longest Increasing Subsequence
==============================


.. image:: https://img.shields.io/pypi/v/longest_increasing_subsequence.svg
        :target: https://pypi.python.org/pypi/longest_increasing_subsequence

.. image:: https://travis-ci.com/mCodingLLC/longest_increasing_subsequence.svg?branch=master
        :target: https://travis-ci.com/mCodingLLC/longest_increasing_subsequence

.. image:: https://readthedocs.org/projects/longest-increasing-subsequence/badge/?version=latest
        :target: https://longest-increasing-subsequence.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Find the longest increasing or decreasing subsequence of a sequence.

Install with:

.. code-block:: console

    pip install longest-increasing-subsequence

Usage:

.. code-block:: python3

    from longest_increasing_subsequence import (longest_increasing_subsequence,
                                                longest_decreasing_subsequence,
                                                longest_increasing_subsequence_indices)

    longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    # [0, 2, 6, 9, 11, 15]

    longest_increasing_subsequence([0, 0, 1, 2, 3, 2, 1, 0, 0])
    # [0, 0, 1, 2, 2]

    longest_decreasing_subsequence([0, 0, 1, 2, 3, 2, 1, 0, 0])
    # [3, 2, 1, 0, 0]

    longest_increasing_subsequence([0, 0, 1, 2, 3], strict=True)
    # [0, 1, 2, 3]

    longest_increasing_subsequence(['A', 'B', 'CC', 'D', 'EEE'], key=len)
    # ['A', 'B', 'D', 'EEE']

    "".join(longest_increasing_subsequence('aababbbdccddd'))
    # 'aaabbbccddd'

    longest_increasing_subsequence_indices([0, 0, 1, 2, 3, 2, 1, 0, 0])
    # [0, 1, 2, 3, 5]


* Free software: MIT license
* Documentation: https://longest-increasing-subsequence.readthedocs.io.


Features
--------

* Works with arbitrary sequence types (list, tuple, str, numpy array, pandas series, etc.)
* Works with arbitrary comparable elements (anything that has < and >).
* Can compute increasing or decreasing subsequences.
* Can compute strictly increasing or strictly decreasing subsequences.
* Can compare elements by an optional key function (e.g. compare strings by length).
* Can return the subsequence or the indices of the subsequence.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
