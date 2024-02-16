import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):    # fix this to be matched with the console.py file
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(fake_out.getvalue(), "")

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel")
            self.assertIn("** instance id missing **", fake_out.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy BaseModel")
            self.assertIn("** instance id missing **", fake_out.getvalue())

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all BaseModel")
            self.assertIn("[]", fake_out.getvalue())

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(fake_out.getvalue(), "")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            self.assertIn("** instance id missing **", fake_out.getvalue())

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("update BaseModel instance_id")
            self.assertIn("** instance id missing **", fake_out.getvalue())

    def test_command(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("command BaseModel")
            self.assertIn(fake_out.getvalue(), "** instance id missing **")

    def test_default(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.default("BaseModel")
            self.assertEqual(fake_out.getvalue(), "** instance id missing **")

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("emptyline"))
            self.assertEqual(fake_out.getvalue(), "\n")


if __name__ == '__main__':
    unittest.main()
