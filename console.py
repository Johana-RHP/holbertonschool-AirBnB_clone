#!/usr/bin/python3
""" Console to manage hbnb data """

import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand CLI, entry command interpreter """
    prompt = '(hbnb) '
    claxx = ["BaseModel", "State", "City", "User", "Place",
             "Amenity", "Review"]

    def emptyline(self):
        """ Method emptyline """
        pass

    def do_quit(self, arg):
        """func to do"""
        return True

    def do_EOF(self, line):
        """ Ctrl+D to exit the program """
        return True

    def do_create(self, arg):
        """functions to operate"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.claxx:
            print("** class doesn't exist **")
            return
        instance = eval(class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """functions to operate"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.claxx:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return
        print(instances[key])

    def do_destroy(self, arg):
        """functions to operate"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.claxx:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return
        del instances[key]
        storage.save()

    def do_all(self, arg):
        """functions to operate"""
        args = arg.split()
        instances = storage.all()
        if not args:
            print([str(instance) for instance in instances.values()])
        else:
            class_name = args[0]
            if class_name not in self.claxx:
                print("** class doesn't exist **")
                return
            filtered_instances = [
                    str(instance)
                    for instance in instances.values()
                    if instance.__class__.__name__ == class_name
            ]
            print(filtered_instances)

    def do_update(self, arg):
        """functions to operate"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.claxx:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        instance = instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()



    if __name__ == '__main__':
    HBNBCommand().cmdloop()
