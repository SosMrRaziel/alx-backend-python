#!/usr/bin/env python3
""" element length """


from typing import Sequence, Tuple, List


def element_length(lst: Sequence[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return tuple of sequence and int """
    return [(i, len(i)) for i in lst]
