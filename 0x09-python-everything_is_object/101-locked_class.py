#!/usr/bin/python3
"""Defines a locked class"""
class LockedClass:
    """An empty Class LockedClass,
    that prevents the dynamic creation of new instance attributes,
    except if the new instance attribute is called 'first_name'."""
    __slots__ = ['first_name']
