#!/usr/bin/env python3
"""HBNBCommand module"""

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
	__classes = {
        "BaseModel"
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, args):
        """Create a new object"""
        # Parse the 'args' to get class name and create the object

    def do_show(self, args):
        """Show the specified object"""
        # Parse the 'args' to get class name and object ID
        # Retrieve and print the object

    def do_destroy(self, args):
        """Destroy the specified object"""
        # Parse the 'args' to get class name and object ID
        # Delete the object

    def do_all(self, args):
        """List all objects or specific objects"""
        # Parse the 'args' to get class name (optional)
        # List all objects or filter objects by class name

if __name__ == '__main__':
    HBNBCommand().cmdloop()
