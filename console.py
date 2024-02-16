#!/usr/bin/python3
""" contains the entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    array_of_keys = ["BaseModel", "City", "User", "State",
                     "Review", "Place", "Amenity"]

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.array_of_keys:
            print("** class doesn't exist **")
            return
        else:
            class_name = args[0]
            my_instance = eval(class_name)()
            my_instance.save()
            print(my_instance.id)

    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.array_of_keys:
            print(args[0])
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        elif my_args[0] not in self.array_of_keys:
            print("** class doesn't exist **")
            return
        elif len(my_args) == 1:
            print("** instance id missing **")
            return
        for key in storage.all():
            if storage.all()[key].id == my_args[1]:
                del storage.all()[key]
                storage.save()
                return
        print("** no instance found **")

    def do_update(self, args):
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        elif my_args[0] not in self.array_of_keys:
            print("** class doesn't exist **")
            return
        elif len(my_args) == 1:
            print("** instance id missing **")
            return
        else:
            instance_id = my_args[1]
            attribute_name = str(my_args[2])
            attribute_value = str(my_args[3])

            for key in storage.all():
                if key.split('.')[1] == instance_id:
                    instance = storage.all()[key]
                    setattr(instance, attribute_name, attribute_value)
                    instance.save()
                    return

            print("** no instance found **")

    def do_command(self, arg):
        args = arg.split()
        if args:
            first_arg = args[0]
            print("First argument:", first_arg)

    def do_all(self, args):
        my_args = args.split()
        if len(my_args) == 0 or my_args[0] not in self.array_of_keys:
            print("** class doesn't exist **")
            return
        else:
            class_name = my_args[0]
            list_of_instances = []

            for key in storage.all():
                key_class = key.split('.')[0]
                if key_class == class_name:
                    instance_str = str(storage.all()[key])
                    list_of_instances.append(instance_str)
            print(list_of_instances)

    def default(self, args):
        my_args = args.split(".")
        if my_args[0] in self.array_of_keys:
            if my_args[1] == "all()":
                self.do_all(my_args[0])
                return
            if my_args[1] == "count()":
                counter = 0
                for keys in storage.all().keys():
                    key, value = keys.split(".")
                    if key == my_args[0]:
                        counter += 1
                print(counter)
                return
            Last_args = my_args[1].split('("')
            if Last_args[0] == "show":
                new_s = Last_args[1].replace('")', "")
                last = f"{my_args[0]}.{new_s}"
                if last in storage.all():
                    print(last)
                    print(storage.all()[last])
                    return
                print("** no instance found **")
            if Last_args[0] == "destroy":
                new_s = Last_args[1].replace('")', "")
                last = f"{my_args[0]}.{new_s}"
                if last in storage.all():
                    del storage.all()[last]
                    storage.save()
                    return
                print("** no instance found **")
            if Last_args[0] == "update":
                print(Last_args[1])
                return  # need to be fix to get a list of str withour a comma.
        print(f"*** Unknown syntax: {args}")

    def do_EOF(self, arg):
        """Exit the program by typing EOF """
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
