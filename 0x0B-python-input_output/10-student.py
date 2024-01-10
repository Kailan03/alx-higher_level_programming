#!/usr/bin/python3
"""
Defines a Student class with public instance attributes
and a to_json method.
"""


class Student:
    """
    Student class definition.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(self, attrs=None): Retrieves a dictionary representation
        of a Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
            attrs (list): A list of strings representing attribute names.
                         Only attributes in this list will be retrieved.
                         If None, all attributes will be retrieved.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
