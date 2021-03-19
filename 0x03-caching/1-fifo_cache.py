#!/usr/bin/env python3
""" FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    
    def __init__(self):
        super().__init__()
        self.line = []

    def put(self, key, item):
        """ Add an item in the cache with FIFO algorithm """

        if key not in self.line:
            self.line.append(key)
        
        if key is not None or item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            erase = self.line.pop(0)
            del self.cache_data[erase]
            print('DISCARD: {}'.format(erase))

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
 