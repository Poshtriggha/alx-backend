#!/usr/bin/env python3
"""Implements a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10"""

import csv
import math
from typing import List, Tuple

from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): The page number
        page_size (int): The number of items per page

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a list of lists containing the data for the specified page.

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of lists containing the data for the specified page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data = self.dataset()

        indices = index_range(page, page_size)
        start = indices[0]
        end = indices[1]

        try:
            return data[start:end]
        except IndexError:
            return []

if __name__ == "__main__":
    server = Server()

    res = server.get_page(1, 7)
    print(type(res))
    print(res)

    res = server.get_page(page=3, page_size=15)
    print(type(res))
    print(res)
