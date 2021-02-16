"""Top-level package for Longest Increasing Subsequence."""

__author__ = """James Murphy"""
__email__ = 'james@mcoding.io'
__version__ = '0.1.4'

from .implementation import (longest_increasing_subsequence,
                             longest_decreasing_subsequence,
                             longest_increasing_subsequence_indices,
                             longest_decreasing_subsequence_indices, )

__all__ = ['longest_increasing_subsequence',
           'longest_decreasing_subsequence',
           'longest_increasing_subsequence_indices',
           'longest_decreasing_subsequence_indices', ]
