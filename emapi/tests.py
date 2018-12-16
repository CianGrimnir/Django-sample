from django.test import TestCase
from django.test.client import RequestFactory
from emapi.views import index, post

# Create your tests here
class YourTestClass(TestCase):
    '''def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
        '''
#    body={"Employee ID": 5, "First Name": "rahul", "last name": "nair", "Department": "Sr.Devops"}
    body={
            "employee": {
                "employee_id" : "22",
                "first_name": "Foo1",
                "last_name": "Bar2",
                "department": "Central2 Tech"
                        }
            }
    @classmethod
    def setUp(self) :
        # Every test needs access to the request factory.
        self.factory = RequestFactory ( )

    def test_put(self):
        request=self.factory.put('/emapi/addemployee/',self.body,content_type='application/json')

    def test_index(self) :
        putrequest=self.factory.put('/emapi/addemployee/',self.body,content_type='application/json')
        putresponse=post(putrequest)
        request = self.factory.get ( '/emapi/employees' )
        response = index ( request )
        self.assertEqual ( response.status_code, 200)
        print("Response ")
        print(response.content)
        self.assertEqual(putresponse.content, self.body)
