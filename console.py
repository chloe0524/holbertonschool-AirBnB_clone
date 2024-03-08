#!/usr/bin/python3
"""
This script creates a simple interactive console
for the HBNB application.
Users can enter commands to interact with the application.
Available commands include 'quit' to exit, 'help' to display help,
and 'EOF' to exit (typically triggered by Ctrl-D).

To use the console, run the script, and then enter commands at the
'(hbnb)' prompt.
"""
import cmd

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

storage = FileStorage()


class HBNBCommand(cmd.Cmd):
    """
    Class representing the custom command interpreter for HBNB.
    Use 'help' to see the available commands.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Handles an empty command (ignored)"""
        pass

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program (Ctrl-D)"""
        return True

    def do_create(self, arg):
        """
        Create a new instance.
        Syntax: create ClassName
        """
        if not arg:
            print("** class name missing **")
            return

        if arg not in globals():
            print("** class doesn't exist **")
            return

        class_mapping = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

        class_instance = class_mapping[arg]()
        class_instance.save()
        print(class_instance.id)

    def do_show(self, arg):
        """
        Display the details of an instance.
        Syntax: show ClassName ID
        """
        if not arg:
            print("** class name missing **")
            return

        frag = arg.split()

        if frag[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(frag) != 2:
            print("** instance id missing **")
            return

        instance = f"{frag[0]}.{frag[1]}"

        if instance not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[instance])

    def do_destroy(self, arg):
        """
        Delete an instance and save the JSON file.
        Syntax: destroy ClassName ID
        """
        if not arg:
            print("** class name missing **")
            return

        frag = arg.split()

        if frag[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(frag) != 2:
            print("** instance id missing **")
            return

        instance = f"{frag[0]}.{frag[1]}"
        if instance not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[instance]
        storage.save()

    def do_all(self, arg):
        """
        Print all instances in string representation.

        Syntax:
        - all BaseModel
        - all
        """
        if not arg:
            print([str(storage.all()[id]) for id in storage.all()])
            return

        if arg not in globals():
            print("** class doesn't exist **")
            return

        instances = []

        for instance in storage.all():
            if arg in instance:
                instances.append(str(storage.all()[instance]))

        print(instances)

    def do_update(self, arg):
        """
        Update an instance attribute by ID and ClassName.

        Syntax:
        - update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return

        frag = arg.split()

        if frag[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(frag) < 2:
            print("** instance id missing **")
            return

        instance = f"{frag[0]}.{frag[1]}"

        if instance not in storage.all():
            print("** no instance found **")
            return

        if len(frag) < 3:
            print("** attribute name missing **")
            return

        if len(frag) < 4:
            print("** value missing **")
            return

        setattr(storage.all()[instance], frag[2], frag[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
