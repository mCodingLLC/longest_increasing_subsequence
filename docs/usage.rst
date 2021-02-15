=====
Usage
=====

To use Longest Increasing Subsequence in a project::

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
