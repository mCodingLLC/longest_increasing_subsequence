"""Implementation of the longest increasing subsequence algorithm."""
from bisect import bisect_right, bisect_left
from typing import TypeVar, Optional, List, Any, Iterator, Sequence, Callable

T = TypeVar('T')


def longest_increasing_subsequence(seq: Sequence[T], strict=False, key: Callable = None) -> List[T]:
    """
    Returns the longest increasing subsequence of the given sequence.
    There may be other increasing subsequences of the same length.

    >>> longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    [0, 2, 6, 9, 11, 15]

    >>> longest_increasing_subsequence([0, 0, 1, 2, 3, 2, 1, 0, 0])
    [0, 0, 1, 2, 2]

    >>> longest_increasing_subsequence([0, 0, 1, 2, 3], strict=True)
    [0, 1, 2, 3]

    >>> longest_increasing_subsequence(['A', 'B', 'CC', 'D', 'EEE'], key=len)
    ['A', 'B', 'D', 'EEE']

    >>> "".join(longest_increasing_subsequence('aababbbdccddd'))
    'aaabbbccddd'

    :param seq: A sequence-like container of comparable objects.
    :param strict: Whether the subsequence must be strictly increasing.
    :param key: If not None, values in sequence are compared by comparing their keys.
    :return: The longest increasing subsequence in seq as a list.
    """
    return _longest_monotone_subsequence(seq, True, strict, key)


def longest_decreasing_subsequence(seq: Sequence[T], strict=False, key: Callable = None) -> List[T]:
    """
    Returns the longest decreasing subsequence of the given sequence.
    There may be other decreasing subsequences of the same length.

    >>> longest_decreasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    [12, 10, 9, 5, 3]

    >>> longest_decreasing_subsequence([0, 0, 1, 2, 3, 2, 1, 0, 0])
    [3, 2, 1, 0, 0]

    >>> longest_decreasing_subsequence([0, 0, 1, 2, 3, 2, 1, 0, 0], strict=True)
    [3, 2, 1, 0]

    :param seq: A sequence-like container of comparable objects.
    :param strict: Whether the subsequence must be strictly increasing.
    :param key: If not None, values in sequence are compared by comparing their keys.
    :return: The longest decreasing subsequence in seq as a list.
    """
    return _longest_monotone_subsequence(seq, False, strict, key)


def longest_increasing_subsequence_indices(seq: Sequence[T], strict=False, key: Callable = None) -> List[int]:
    """
    Returns the indices of the longest increasing subsequence of the given sequence.
    There may be other increasing subsequences of the same length.

    >>> longest_increasing_subsequence_indices([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    [0, 4, 6, 9, 13, 15]

    >>> longest_increasing_subsequence_indices([0, 0, 1, 2, 3, 2, 1, 0, 0])
    [0, 1, 2, 3, 5]

    >>> longest_increasing_subsequence_indices([0, 0, 1, 2, 3, 2, 1, 0, 0], strict=True)
    [0, 2, 3, 4]


    :param seq: A sequence-like container of comparable objects.
    :param strict: Whether the subsequence must be strictly increasing.
    :param key: If not None, values in sequence are compared by comparing their keys.
    :return: A list of indices of the longest increasing subsequence in seq.
    """
    return _longest_monotone_subsequence_indices(seq, True, strict, key)


def longest_decreasing_subsequence_indices(seq: Sequence[T], strict=False, key: Callable = None) -> List[int]:
    """
    Returns the indices of the longest decreasing subsequence of the given sequence.
    There may be other decreasing subsequences of the same length.

    >>> longest_decreasing_subsequence_indices([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    [3, 5, 9, 10, 12]

    >>> longest_decreasing_subsequence_indices([0, 0, 1, 2, 3, 2, 1, 0, 0])
    [4, 5, 6, 7, 8]

    >>> longest_decreasing_subsequence_indices([0, 0, 1, 2, 3, 2, 1, 0, 0], strict=True)
    [4, 5, 6, 7]

    :param seq: A sequence-like container of comparable objects.
    :param strict: Whether the subsequence must be strictly increasing.
    :param key: If not None, values in sequence are compared by comparing their keys.
    :return: A list of indices of the longest decreasing subsequence in seq.
    """
    return _longest_monotone_subsequence_indices(seq, False, strict, key)


def _longest_monotone_subsequence(seq: Sequence[T], increasing=True, strict=False, key: Callable = None) -> List[T]:
    """
    Returns the a list of the longest increasing (respectively decreasing) subsequence of the given sequence.
    There may be other increasing (respectively decreasing) subsequences of the same length.

    This is not a public function, use a longest_increasing_* or longest_decreasing_* function instead.

    :param seq: A sequence-like container of comparable objects.
    :param increasing: Whether the subsequence should be increasing or decreasing.
    :param strict: Whether the subsequence must be strictly monotone.
    :param key: If not None, values in sequence are compared by comparing their keys.
    :return: An iterator of indices of the longest monotone subsequence in seq.
    """
    return [seq[idx] for idx in _longest_monotone_subsequence_indices_iter(seq, increasing, strict, key)]


def _longest_monotone_subsequence_indices(seq: Sequence[T], increasing=True, strict=False, key: Callable = None) -> List[int]:
    """
    Gives a list of the indices of the longest increasing (respectively decreasing) subsequence of the given sequence.
    There may be other increasing (respectively decreasing) subsequences of the same length.

    This is not a public function, use a longest_increasing_* or longest_decreasing_* function instead.

    :param seq: A sequence-like container of comparable objects.
    :param increasing: Whether the subsequence should be increasing or decreasing.
    :param strict: Whether the subsequence must be strictly monotone.
    :param key: If not None, values in sequence are compared by comparing their keys.
    :return: An iterator of indices of the longest monotone subsequence in seq.
    """
    return list(_longest_monotone_subsequence_indices_iter(seq, increasing, strict, key))


def _longest_monotone_subsequence_indices_iter(seq: Sequence[T], increasing=True, strict=False, key: Callable = None) -> Iterator[int]:
    """
    Yields the indices of the longest increasing (respectively decreasing) subsequence of the given sequence.
    There may be other monotone subsequences of the same length.

    This is not a public function, use a longest_increasing_* or longest_decreasing_* function instead.

    :param seq: A sequence-like container of comparable objects.
    :param increasing: Whether the subsequence should be increasing or decreasing.
    :param strict: Whether the subsequence must be strictly monotone.
    :param key: If not None, values in sequence are compared by comparing their keys.
    :return: An iterator of indices of the longest monotone subsequence in seq.
    """
    if not seq:
        return (_ for _ in [])

    idx_prev_longest: List[Optional[int]] = []
    idx_min_of_len_plus1: List[int] = []  # the index of the smallest value ending a subsequence of a given length+1
    val_min_of_len_plus1: List[Any] = []  # the smallest value ending a subsequence of a given length+1

    bisect = bisect_right if not strict else bisect_left
    key_fn = _choose_key_function(key, increasing)
    keys = seq if key_fn is None else map(key_fn, seq)

    for i, curr_key in enumerate(keys):
        len_longest_extendable = bisect(val_min_of_len_plus1, curr_key)

        if len_longest_extendable == len(val_min_of_len_plus1):
            idx_min_of_len_plus1.append(i)
            val_min_of_len_plus1.append(curr_key)
        elif curr_key < val_min_of_len_plus1[len_longest_extendable]:
            idx_min_of_len_plus1[len_longest_extendable] = i
            val_min_of_len_plus1[len_longest_extendable] = curr_key

        idx_longest_extendable = idx_min_of_len_plus1[len_longest_extendable - 1] if len_longest_extendable else None
        idx_prev_longest.append(idx_longest_extendable)

    longest_subsequence_indices = _make_subsequence_indices(prev_indices=idx_prev_longest,
                                                            terminal_idx=idx_min_of_len_plus1[-1])
    return longest_subsequence_indices


class _OrderReversed:
    """
    A wrapper around any object that swaps its < and > operators (without touching the actual object).

    >>> _OrderReversed(0) > _OrderReversed(1)
    True
    """

    def __init__(self, o):
        self.obj = o

    def __lt__(self, other):
        return self.obj > other.obj

    def __gt__(self, other):
        return self.obj < other.obj

    def __repr__(self):
        return f'{self.__class__.__name__}({self.obj!r})'


def _choose_key_function(key: Optional[Callable], increasing: bool) -> Optional[Callable]:
    """
    Gives back the key function with its order optionally reversed. None represents the identity function.

    >>> _choose_key_function(None, True) is None
    True

    >>> fn = _choose_key_function(None, False)
    >>> fn(0) > fn(1)
    True

    >>> fn = _choose_key_function(len, True)
    >>> fn("X") < fn("AA")
    True

    >>> fn = _choose_key_function(len, False)
    >>> fn("AA") < fn("X")
    True
    """
    if key is None and increasing:
        key_fn = None
    elif key is None:
        def key_fn(v):
            return _OrderReversed(v)
    elif not increasing:
        orig_key = key

        def key_fn(v):
            return _OrderReversed(orig_key(v))
    else:
        key_fn = key
    return key_fn


def _make_reversed_subsequence_indices(prev_indices: List[Optional[int]], terminal_idx: int) -> Iterator[int]:
    """
    Given a list of indices representing pointers to parent, and given a terminal pointer, yields indices from the terminal to the root.

    >>> list(_make_reversed_subsequence_indices([None, 0, 0, 1, 2, 1], 5))
    [5, 1, 0]
    """
    idx: Optional[int] = terminal_idx
    while idx is not None:
        yield idx
        idx = prev_indices[idx]


def _make_subsequence_indices(prev_indices: List[Optional[int]], terminal_idx: int) -> Iterator[int]:
    """
    Given a list of indices representing pointers to parent, and given a terminal pointer, yields indices from the root to the terminal index.

    >>> list(_make_subsequence_indices([None, 0, 0, 1, 2, 1], 5))
    [0, 1, 5]
    """
    return reversed(list(_make_reversed_subsequence_indices(prev_indices, terminal_idx)))
