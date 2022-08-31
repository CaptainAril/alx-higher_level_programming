#!/usr/bin/python3
"""This module defines a Student class."""


class Student:
    """Represents a class Student."""
    def __init__(self, first_name, last_name, age):
        """Instantiates a Student instance.

        Args:
            first_name (str): First name of student instance.
            last_name (str): Last name of Student instance.
            age (int): age of Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of class instance"""
        return self.__dict__
