#!/usr/bin/python3
"""module creating the console for project"""

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
