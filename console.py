#!/usr/bin/python3
"""module creating the console"""

import cmd

class HBNBCommand(cmd.Cmd):
    """class with cmd methods"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """End of File to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when it's an empty line"""
        pass

    # def create(self, arg):
    #    """ 3 """
    #    if not arg:
    #        print ('** class name missing **')

    #    if arg not in globals():
    #        print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()