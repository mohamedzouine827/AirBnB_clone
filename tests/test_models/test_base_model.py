import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_attribute(self):
        """
        test the basic attributes are initilazed
        """
        instance_1 = BaseModel()
        v = getattr(instance_1, "id", 0)
        self.assertTrue(instance_1.id == v)
        v = getattr(instance_1, "created_at", 0)
        self.assertTrue(instance_1.created_at == v)
        v = getattr(instance_1, "updated_at", 0)
        self.assertTrue(instance_1.updated_at == v)

    def test_type(self):
        """
        test basic attributes types
        """
        instance_1 = BaseModel()
        a = datetime.now()
        self.assertTrue(type(instance_1.id) == str)
        self.assertTrue(type(instance_1.created_at) == type(a))
        self.assertTrue(type(instance_1.updated_at) == type(a))

    def test_unique_id(self):
        """
        test two ids are the equals
        """
        instance_1 = BaseModel()
        inctance_2 = BaseModel()
        self.assertNotEqual(instance_1.id, inctance_2.id)

    def test_str(self):
        """
        test magic method
        """
        instance_1 = BaseModel()
        strr = ("[{}] ({}) {}".format(instance_1.__class__.__name__,
                instance_1.id, instance_1.__dict__))
        self.assertEqual(str(instance_1), strr)

    def test_save_method(self):
        """
        test save method
        """
        instance_1 = BaseModel()
        update = instance_1.updated_at
        instance_1.save()
        self.assertNotEqual(update, instance_1.updated_at)

    def test_to_dict(self):
        """
        test to_dict() method
        """
        instance_1 = BaseModel()
        instance_1.name = "Aadel"
        dic = instance_1.to_dict()
        self.assertEqual(type(dic), dict)
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(dic["name"], "Aadel")
        self.assertEqual(type(dic["created_at"]), str)

    def test_kwargs(self):
        """
        test passing kwargs to BaseModel()
        """
        instance_1 = BaseModel()
        instance_1.name = "houda"
        dic = instance_1.to_dict()
        instance_2 = BaseModel(**dic)
        self.assertNotEqual(instance_1, instance_2)
        self.assertEqual(instance_1.id, instance_2.id)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(self.base_model.to_dict(), dict)

    def test_to_dict_contains_class_name(self):
        self.assertEqual(self.base_model.to_dict()["__class__"], "BaseModel")

    def test_to_dict_contains_created_at(self):
        self.assertIn("created_at", self.base_model.to_dict())

    def test_to_dict_contains_updated_at(self):
        self.assertIn("updated_at", self.base_model.to_dict())


if __name__ == '__main__':
    unittest.main()
