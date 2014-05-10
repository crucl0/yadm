from unittest import TestCase

from yadm.documents import Document
from yadm import fields


class DocumentsTest(TestCase):

    def setUp(self):
        class TestDoc(Document):
            i = fields.IntegerField
            b = fields.SetField(fields.IntegerField())

        self.TestDoc = TestDoc

    def test__db(self):
        td = self.TestDoc()
        self.assertIs(td.__db__, None)

    def test_fields(self):
        self.assertEqual(set(self.TestDoc.__fields__), {'_id', 'i', 'b'})

    def test_inheritance_fields(self):
        class InhTestDoc(self.TestDoc):
            pass
