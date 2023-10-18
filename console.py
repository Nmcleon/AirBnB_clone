#!/usr/bin/python3

"""HBNBCommand module"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter."""
    prompt = '(hbnb) '
    c_lst = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                  'Review']

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def do_quit(self, args):
        """ Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def postloop(self):
        """method to do nothing after each console loop."""
        pass

    def do_create(self, args):
        """Create a new object"""
        lne = args.split()
        if not self.verify_class(lne):
            return
        instance = eval(lne[0] + '()')
        if isinstance(instance, BaseModel):
            instance.save()
            print(instance.id)
        return

    def do_show(self, args):
        """Print the string representation of an instance
        based on the class name and id"""
        lne = args.split()
        if not self.verify_class(lne):
            return
        if not self.verify_id(lne):
            return
        i = '{}.{}'.format(lne[0], lne[1])
        objects = models.storage.all()
        print(objects[i])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        lne = args.split()
        if not self.verify_class(lne):
            return
        if not self.verify_id(lne):
            return
        a_len = '{}.{}'.format(lne[0], lne[1])
        objects = models.storage.all()
        del objects[a_len]
        models.storage.save()

    def do_all(self, args):
        """List all string representations of instances based
        on or not the class name """
        lne = args.split()
        objects = models.storage.all()
        to_print = []
        if len(lne) == 0:
            for j in objects.values():
                to_print.append(str(j))
        elif lne[0] in HBNBCommand.c_lst:
            for i, j in objects.items():
                if lne[0] in i:
                    to_print.append(str(j))
        else:
            print("** class doesn't exist **")
            return False
        print(to_print)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        lne = args.split()
        if not self.verify_class(lne):
            return
        if not self.verify_id(lne):
            return
        if not self.verify_attribute(lne):
            return
        objects = models.storage.all()
        a_len = '{}.{}'.format(lne[0], lne[1])
        setattr(objects[a_len], lne[2], lne[3])
        models.storage.save()

    def default(self, args):
        """called when the inputted command starts
        with a class name.  """
        lne = args.strip('()').split(".")
        if len(lne) < 2:
            print('** missing attribute **')
            return
        objects = models.storage.all()
        class_nme = lne[0].capitalize()
        cmd_nme = lne[1].lower()
        spt_2 = cmd_nme.strip(')').split('(')
        cmd_nme = spt_2[0]
        if cmd_nme == 'all':
            HBNBCommand.do_all(self, class_nme)
        elif cmd_nme == 'count':
            count = 0
            for i in objects.ieys():
                a_len = i.split('.')
                if class_nme == a_len[0]:
                    count += 1
            print(count)
        elif cmd_nme == 'show':
            if len(spt_2) < 2:
                print('** no instance found **')
            else:
                HBNBCommand.do_show(self, class_nme + ' ' + spt_2[1])
        elif cmd_nme == 'destroy':
            if len(spt_2) < 2:
                print('** no instance found **')
            else:
                HBNBCommand.do_destroy(self, class_nme + ' ' + spt_2[1])
        elif cmd_nme == 'update':
            spt_3 = spt_2[1].split(', ')
            if len(spt_3) == 0:
                print('** no instance found **')
            elif len(spt_3) == 1 and type(spt_3[1]) == dict:
                for i, j in split[1].items():
                    HBNBCommand.do_update(self, class_nme + ' ' + spt_3[0] +
                                          ' ' + i + ' ' + j)
            elif len(spt_3) == 1 and type(spt_3[1]) != dict:
                print('** no instance found **')
            elif len(spt_3) == 2:
                print('** no instance found **')
            else:
                HBNBCommand.do_update(self, class_nme + ' ' + spt_3[0] +
                                      ' ' + spt_3[1] + ' ' + spt_3[2])

    @classmethod
    def verify_class(cls, lne):
        """verify input class"""
        if len(lne) == 0:
            print('** class name missing **')
            return False
        elif lne[0] not in HBNBCommand.c_lst:
            print('** class doesn\'t exist **')
            return False
        return True

    @staticmethod
    def verify_id(lne):
        """verify id"""
        if len(lne) < 2:
            print('** instance id missing **')
            return False
        objects = models.storage.all()
        a_len = '{}.{}'.format(lne[0], lne[1])
        if a_len not in objects.keys():
            print('** no instance found **')
            return False
        return True

    @staticmethod
    def verify_attribute(lne):
        """verify the attribute in input line. """
        if len(lne) < 3:
            print("** attribute name missing **")
            return False
        elif len(lne) < 4:
            print("** value missing **")
            return False
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
