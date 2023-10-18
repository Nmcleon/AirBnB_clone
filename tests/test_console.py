import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    # Test do_EOF
    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        console = HBNBCommand()
        self.assertTrue(console.do_EOF(''))
        self.assertEqual(mock_stdout.getvalue(), '')

    # Test do_quit
    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        console = HBNBCommand()
        self.assertTrue(console.do_quit(''))
        self.assertEqual(mock_stdout.getvalue(), '')

    # Test emptyline
    def test_emptyline(self):
        console = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO):
            console.emptyline()

    # Test verify_class
    @patch('sys.stdout', new_callable=StringIO)
    def test_verify_class(self, mock_stdout):
        console = HBNBCommand()
        self.assertTrue(console.verify_class(['BaseModel']))
        self.assertTrue(console.verify_class(['User']))
        self.assertTrue(console.verify_class(['State']))
        self.assertTrue(console.verify_class(['City']))
        self.assertTrue(console.verify_class(['Amenity']))
        self.assertTrue(console.verify_class(['Place']))
        self.assertTrue(console.verify_class(['Review']))
        self.assertFalse(console.verify_class([]))
        self.assertFalse(console.verify_class(['InvalidClass']))
        self.assertEqual(mock_stdout.getvalue(), '')

    # Test verify_id
    @patch('sys.stdout', new_callable=StringIO)
    def test_verify_id(self, mock_stdout):
        console = HBNBCommand()
        with patch('models.storage.all') as mock_all:
            mock_all.return_value = {'BaseModel.1': 'obj1', 'User.2': 'obj2'}
            self.assertTrue(console.verify_id(['BaseModel', '1']))
            self.assertTrue(console.verify_id(['User', '2']))
            self.assertFalse(console.verify_id([]))
            self.assertFalse(console.verify_id(['BaseModel']))
            self.assertFalse(console.verify_id(['BaseModel', '3']))
            self.assertEqual(mock_stdout.getvalue(), '')

    # Test verify_attribute
    @patch('sys.stdout', new_callable=StringIO)
    def test_verify_attribute(self, mock_stdout):
        console = HBNBCommand()
        self.assertTrue(console.verify_attribute(['BaseModel', '1', 'name', 'obj1']))
        self.assertTrue(console.verify_attribute(['User', '2', 'email', 'user@example.com']))
        self.assertFalse(console.verify_attribute([]))
        self.assertFalse(console.verify_attribute(['BaseModel', '1']))
        self.assertFalse(console.verify_attribute(['BaseModel', '2', 'name']))
        self.assertEqual(mock_stdout.getvalue(), '')

if __name__ == '__main__':
    unittest.main()

