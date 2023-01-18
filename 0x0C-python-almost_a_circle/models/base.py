#!/usr/bin/python3
"""Defines a base class."""
import json


class Base:
    """Model the base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """takes a dictioanry as argument and returns the JSON string
        representation."""

        if (list_dictionaries is None) or (list_dictionaries == "[]"):
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list of instances to a file.

        Args:
            list_objs - list of instances that inherit from Base.
        """

        if list_objs is None:
            pass

        filename = "{}.json".format(cls.__name__)
        dict_lists = []

        if (list_objs) is not None:
            for obj in list_objs:
                dict_lists.append(obj.to_dictionary())

        j_string = cls.to_json_string(dict_lists)
        with open(filename, "w") as f:
            f.write(j_string)

    @staticmethod
    def from_json_string(json_string):
        """returns a list of JSON string representation of json_string"""
        if (json_string is None) or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionaries):
        """Returns an instance with all attributes set.

        Description: 'dictionaries' is a key value pair
        that will be used to set
        the attributes of an instance of Rectangle or Square.
        """
        if cls.__name__ == "Rectangle":
            new_inst = cls(1, 1)
        else:
            new_inst = cls(1)
        new_inst.update(**dictionaries)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """Load a file and return the list of instances based on the
        dictionaries in the file."""

        filename = "{}.json".format(cls.__name__)
        inst_list = []

        try:
            with open(filename, "r") as f:
                lists = Base.from_json_string(f.read())
        except FileNotFoundError:
            return []

        for inst in lists:
            inst_list.append(cls.create(**inst))

        return (inst_list)
