#!/usr/bin/env python3
"""
This is a function named index_range that takes two integer
arguments page and page_size
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start
    index and an end index

    Args:
        page (int): The page number
        page_size (int): The number of items per page

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
