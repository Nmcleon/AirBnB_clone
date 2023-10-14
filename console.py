#!/usr/bin/env python3
"""HBNBCommand module"""

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        #print("")
        return True

    def do_help(self, line):
        """Get help on commands"""
        cmd.Cmd.do_help(self, line)
        
    def help_EOF(self):
        print("Ctrl+D command to exit the program\n")

    def emptyline(self):
        """Do nothing on an empty line"""
        pass
	
    def do_create(self, args):
        """Create a new object"""
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]

        if class_name not in HBNBCommand.__classes:
            print("** class name missing **")
            return

        new_obj = HBNBCommand.__classes[class_name]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, args):
        """Print the string representation of an instance
        based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        obj_id = "{}.{}".format(args[0], args[1])
        if obj_id not in all_objs:
            print("** no instance found **")
            return
        obj = all_objs[obj_id]
        print(obj)
        
    def do_destroy(self, args):
        """Deletes an instance based 
        on the class name and id
        """
        # Delete the object
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        obj_id = "{}.{}".format(args[0], args[1])
        if obj_id not in all_objs:
            print("** no instance found **")
            return
        del all_objs[obj_id]
        store.save()
        
    def do_all(self, args):
        """List all string representation of all instances based
        or not on the class name
        """
        all_objs = storage.all()
        if not args:
            result = [str(all_objs[obj]) for obj in all_objs]
            print(result)
            return
        if args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        result = [str(all_objs[obj]) for obj in all_objs if obj.startswith(args + '.')]
        print(result)

    def do_update(self, args):
        """Updates an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return

    split_args = args.split()
    class_name = split_args[0]

    if class_name not in HBNBCommand.__classes:
        print("** class doesn't exist **")
        return

    if len(split_args) < 2:
        print("** instance id missing **")
        return

    obj_id = split_args[1]
    all_objs = storage.all()
    obj_key = "{}.{}".format(class_name, obj_id)

    if obj_key not in all_objs:
        print("** no instance found **")
        return

    if len(split_args) < 3:
        print("** attribute name missing **")
        return

    attribute_name = split_args[2]

    if len(split_args) < 4:
        print("** value missing **")
        return

    # Join the attribute value parts into a single string, stripping double quotes
    attribute_value = " ".join(split_args[3:])[1:-1]

    obj = all_objs[obj_key]

    # Check if the attribute name is valid and not 'id', 'created_at', or 'updated_at'
    if hasattr(obj, attribute_name) and attribute_name not in ["id", "created_at", "updated_at"]:
        # Cast attribute value to the appropriate type based on the attribute's type
        attr_type = type(getattr(obj, attribute_name))
        try:
            if attr_type is str:
                attribute_value = str(attribute_value)
            elif attr_type is int:
                attribute_value = int(attribute_value)
            elif attr_type is float:
                attribute_value = float(attribute_value)
        except (ValueError, TypeError):
            print("** invalid value **")
            return

        setattr(obj, attribute_name, attribute_value)
        obj.save()
    else:
        print("** attribute doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

