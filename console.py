#!/usr/bin/env python3
"""HBNBCommand module"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print("")
        return True
    
    def default(self, arg):
        """Default behavior for cmd"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg[1])
            if match is not None:
                command = [arg[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

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
        class_name = args[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        
        obj_id = args[1]
        self.show_instance(class_name, obj_id)

    def show_instance(self, class_name, obj_id):
        all_objs = storage.all()
        obj_id = "{}.{}".format(class_name, obj_id)
        
        if obj_id not in all_objs:
            print("** no instance found **")
            return
        obj = all_objs[obj_id]
        print(obj)

    def do_destroy(self, args):
        """Deletes an instance based 
        on the class name and id
        """
        obj_dict = storage.all()
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        class_name = args[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        
        obj_id = args[1]
        self.destroy_instance(class_name, obj_id)

    def destroy_instance(self, class_name, obj_id):
        all_objs = storage.all()
        obj_id = "{}.{}".format(class_name, obj_id)
        
        if obj_id not in all_objs:
            print("** no instance found **")
            return

        obj_to_delete = all_objs[obj_id]
        del all_objs[obj_id]
        obj_to_delete.save()
        print()
        
        """
        #all_objs = storage.all()
        #obj_id = "{}.{}".format(args[0], args[1])
        if obj_id not in all_objs:
            print("** no instance found **")
            return
        del all_objs[obj_id]
        store.save()
        """

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
        result = [str(all_objs[obj])
                  for obj in all_objs if obj.startswith(args + '.')]
        print(result)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class"""
        count = 0
        for obj in storage.all().values():
            if arg[0] == obj.__class__.name__:
                count +=1
        print(count)

    def do_update(self, args):
        """Updates an instance based on the class name and id."""
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
        attribute_value = split_args[3]
        if attribute_value.startswith('"') and attribute_value.endswith('"'):
            attribute_value = attribute_value[1:-1]
        obj_to_update = all_objs[obj_id]
        if attribute_name in {'id', 'created_at', 'updated_at'}:
            print("** cannot update 'id', 'created_at', or 'updated_at' **")
            return

        try:
            attribute_value = int(attribute_value)
        except ValueError:
            try:
                attribute_value = float(attribute_value)
            except ValueError:
                pass
            
            setattr(obj_to_update, attribute_name, attribute_value)
            obj_to_update.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
