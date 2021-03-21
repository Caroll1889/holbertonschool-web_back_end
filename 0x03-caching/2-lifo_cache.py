#!/usr/bin/env python3
""" FIFO caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class LifoCache"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.line = []

    def put(self, key, item):
        """ Add an item in the cache with LIFO algorithm """

        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            erase = self.line.pop()
            del self.cache_data[erase]
            print('DISCARD: {}'.format(erase))

        if key not in self.line:
            self.line.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
