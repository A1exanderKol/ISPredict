# patches.py
import collections.abc
import sys

# Исправление для совместимости с Python 3.10+
if sys.version_info >= (3, 10):
    collections.Mapping = collections.abc.Mapping
    collections.Sequence = collections.abc.Sequence
    collections.Iterable = collections.abc.Iterable