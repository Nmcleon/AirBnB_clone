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
        "Review": Review,
        "User": User
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
        if class_name != obj.__class__.__name__:
            print("** no instance found **")
        else:
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
        all_objs = storage.all(class_name)
        obj_id = "{}.{}".format(class_name, obj_id)
        
        if obj_id not in all_objs:
            print("** no instance found **")
            return
        del all_objs[obj_id]
        storage.save()
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
        class_name = args.split()[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        result = [str(obj) for obj in all_objs.values() if obj.__class__.__name__ == class_name]
        print(result)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class"""
        count = 0
        for obj in storage.all().values():
            if arg[0] == obj.__class__.name__:
                count +=1
        print(count)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return

        args = args.split()
        class_name = args[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        self.update_instance(class_name, obj_id, args[2:])

            
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
