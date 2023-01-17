#!/usr/bin/python3
""" Base Class """
import json
import os
import csv


class Base:
    """ Class Base Template """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base init method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return Json represenation of dict objects """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        dict_arr = [obj.to_dictionary() for obj in list_objs]

        filename = f"{cls.__name__}.json"
        with open(filename, "w") as json_file:
            json_file.write(cls.to_json_string(dict_arr))

    @staticmethod
    def from_json_string(json_string):
        """ Deserialize/decode a json object """
        if json_string is None or len(json_string) <= 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set: """
        # create a dummy instance of the class (Rectangle or Square ...)
        instance = cls(1, 1, 0, 0)
        # call the update method from the instance class
        instance.update(**dictionary)
        return (instance)

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a json file"""
        filename = f"{cls.__name__}.json"
        # check if file exist or is empty
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return ([])
        with open(filename, 'r') as read_file:
            json_content = read_file.read()
            # deserialize the json file
            decoded_content = cls.from_json_string(json_content)
            # call the create class method on each dict content
            result = [cls.create(**obj) for obj in decoded_content]
            return (result)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the csv representation/Serialize of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        # called the dictionary method b4 saving it in a csv file
        dict_arr = [obj.to_dictionary() for obj in list_objs]
        filename = f'{cls.__name__}.csv'
        with open(filename, 'w', newline="") as csv_file:
            if cls.__name__ == 'Rectangle':
                field_names = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                field_names = ['id', 'size', 'x', 'y']
            csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)

            csv_writer.writeheader()
            for obj in dict_arr:
                csv_writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls):
        """ Deserialize an csv file"""

        filename = f"{cls.__name__}.csv"
        # check if file exist or is empty
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return ([])
        with open(filename, 'r') as read_file:
            csv_reader = csv.DictReader(read_file)

            # convert dictionary values to int
            # csv stores and retrive values in str formats
            result = [dict([key, int(value)] for key, value in row.items())
                      for row in csv_reader]

            result = [cls.create(**obj) for obj in result]
            return (result)
