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
        if args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        new_obj = HBNBCommand.__classes[args]()
        new_obj.save()
        print(new_obj.id)
    
    def do_show(self, args):
        """Print the string representation of an instance
        based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        split_args = args.splir()
        if split_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(split_args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        obj_id = "{}.{}".format(split_args[0], split_args[1])
        if obj_id not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[obj_id])
        
    def do_destroy(self, args):
        """Deletes an instance based 
        on the class name and id
        """
        # Delete the object
        if not args:
            print("** class name missing **")
            return
        split_args = args.split()
        if split_args[0] nnot in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(split_args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        obj_id = "{}.{}".format(split_args[0], split_args[1])
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
        """  Update an instance based 
        on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        split_args = args.split()
        if split_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(split_args) < 2:
            print("** instance id missing **")
            return
        obj_id = "{}.{}".format(split_args[0], split_args[1])
        all_objs = storage.all()
        if obj_id not in all_objs:
            print("** no instance found **")
            return
        if len(split_args) < 3:
            print("** attribute name missing **")
            return
        if len(split_args) < 4:
            print("** value missing **")
            return

        attribute_name = split_args[2]
        # Get attribute value
        attribute_value = split_args[3]
        if attribute_value.startswitch('"') and attribute_value.endswitch('"'):
            attribute_value = attribute_value[1:-1]
        obj_to_update = all_objs[obj_id]
        if attribute_name != 'id' and attribute_name != 'created_at' and attribute_name != 'updated_at':
            try:
                attribute_value = int(attribute_value)
            except ValueError:
                try:
                    attribute_value = float(attribute_value)
                except ValueError:
                    pass
                #update obj's attribute
                setattr(obj_to_update, attribute_name, attribute_value)
                obj_to_update.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
