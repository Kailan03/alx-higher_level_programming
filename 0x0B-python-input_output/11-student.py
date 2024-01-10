#!/usr/bin/python3
"""
Defines a Student class with public instance attributes,
and methods to retrieve a dictionary representation and
reload attributes from a dictionary.
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
        reload_from_json(self, json): Replaces all attributes of the
        Student instance with those from a given dictionary.
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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with those from a dictionary.

        Parameters:
            json (dict): A dictionary where keys are attribute names and
                         values are the corresponding attribute values.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
