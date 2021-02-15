#!/usr/bin/env python

"""Tests for `longest_increasing_subsequence` package."""

import pytest

from longest_increasing_subsequence import longest_increasing_subsequence, longest_decreasing_subsequence


@pytest.mark.parametrize('test_input,expected', [
    ([], []),
    ("", []),
    (tuple(), []),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 0, 3], [1, 2, 3]),
    ([10, 9, 2, 5, 3, 7, 101, 18], [2, 3, 7, 18]),
    ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], [0, 2, 6, 9, 11, 15]),
    ((0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15), [0, 2, 6, 9, 11, 15]),
    ([5], [5]),
    ([5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5]),
    ([5, 5, 5, 5, 5, 5, 4, 3, 2, 1], [5, 5, 5, 5, 5, 5]),
    ('aababbbdccddd', ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd', 'd']),
])
def test_longest_increasing_subsequence(test_input, expected):
    assert longest_increasing_subsequence(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ([], []),
    ("", []),
    (tuple(), []),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 0, 3], [1, 2, 3]),
    ([10, 9, 2, 5, 3, 7, 101, 18], [2, 3, 7, 18]),
    ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], [0, 2, 6, 9, 11, 15]),
    ((0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15), [0, 2, 6, 9, 11, 15]),
    ([5], [5]),
    ([5, 5, 5, 5, 5, 5], [5]),
    ([5, 5, 5, 5, 5, 5, 4, 3, 2, 1], [1]),
    ('aababbbdccddd', ['a', 'b', 'c', 'd']),
    ([0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0], [0, 1]),

])
def test_longest_increasing_subsequence_strict(test_input, expected):
    assert longest_increasing_subsequence(test_input, strict=True) == expected


@pytest.mark.parametrize('test_input,key,expected', [
    ([], lambda x: x, []),
    ("", lambda x: x, []),
    (tuple(), lambda x: x, []),
    ([1, 2, 3], lambda x: x * x, [1, 2, 3]),
    ([1, 2, 0, 3], lambda x: x * x, [1, 2, 3]),
    ([10, 9, 2, 5, 3, 7, 101, 18], lambda x: x * x, [2, 3, 7, 18]),
    ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], lambda x: x * x, [0, 2, 6, 9, 11, 15]),
    ((0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15), lambda x: x * x, [0, 2, 6, 9, 11, 15]),
    ([5], lambda x: x * x, [5]),
    ([5, 5, 5, 5, 5, 5], lambda x: x * x, [5, 5, 5, 5, 5, 5]),
    ([5, 5, 5, 5, 5, 5, 4, 3, 2, 1], lambda x: x * x, [5, 5, 5, 5, 5, 5]),
    ('aababbbdccddd', lambda x: x, ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd', 'd']),
    ([0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0], lambda x: x, [0, 0, 0, 0, 0, 0, 1, 1]),
])
def test_longest_increasing_subsequence_with_key(test_input, key, expected):
    assert longest_increasing_subsequence(test_input, key=key) == expected


@pytest.mark.parametrize('test_input,key,expected', [
    ([], lambda x: x, []),
    ("", lambda x: x, []),
    (tuple(), lambda x: x, []),
    ([1, 2, 3], lambda x: x * x, [1, 2, 3]),
    ([1, 2, 0, 3], lambda x: -x * x, [2, 0]),
    ([10, 9, 2, 5, 3, 7, 101, 18], lambda x: x * x, [2, 3, 7, 18]),
    ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], lambda x: x * x, [0, 2, 6, 9, 11, 15]),
    ((0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15), lambda x: x * x, [0, 2, 6, 9, 11, 15]),
    ([5], lambda x: x * x, [5]),
    ([5, 5, 5, 5, 5, 5], lambda x: x * x, [5]),
    ([5, 5, 5, 5, 5, 5, 4, 3, 2, 1], lambda x: x * x, [1]),
    ('aababbbdccddd', lambda x: x, ['a', 'b', 'c', 'd']),
    ([0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0], lambda x: -x, [1, 0]),
])
def test_longest_increasing_subsequences_strict_with_key(test_input, key, expected):
    assert longest_increasing_subsequence(test_input, strict=True, key=key) == expected


@pytest.mark.parametrize('test_input,expected', [
    ([0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]),
])
def test_longest_decreasing_subsequence(test_input, expected):
    assert longest_decreasing_subsequence(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ([0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 0]),
])
def test_longest_decreasing_subsequence_strict(test_input, expected):
    assert longest_decreasing_subsequence(test_input, strict=True) == expected


@pytest.mark.parametrize('test_input,key,expected', [
    ([0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0], lambda x: -x, [0, 1]),
])
def test_longest_decreasing_subsequence_strict_with_key(test_input, key, expected):
    assert longest_decreasing_subsequence(test_input, strict=True, key=key) == expected
