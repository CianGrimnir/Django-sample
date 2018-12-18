from django.test import TestCase
from django.test.client import RequestFactory
from emapi.views import index, post, list
import json

class YourTestClass(TestCase):
    
    employee_id=22
    employee_id_test=44
    body={
            "22": {
                "employee_id" : 22,
                "first_name": "Foo1",
                "last_name": "Bar2",
                "department": "Central2 Tech"
                        }
            }
    body_neg={
            "-22": {
                "employee_id" : -22,
                "first_name": "Foo1",
                "last_name": "Bar2",
                "department": "Central2 Tech"
                        }
            }

    post_error={ 'status code': 404,
                  'body': 'INVALID POST/WRONG DATA',
                  }
                                  
    list_error={ 'status code': 404,
                'body': 'Employee id: '+str(employee_id_test)+' not found',
                }

    body_reorder={
            "22": {
                "first_name": "Foo1",
                "employee_id" : 22,
                "last_name": "Bar2",
                "department": "Central2 Tech"
                        }
            }


    body_empty={}

    post_duplicate_resp={"status code": 404, "body": "DUPLICATE DATA"}


    @classmethod
    def setUp(self) :
        # Every test needs access to the request factory.
        self.factory = RequestFactory ( )

    def test_put(self):
        request=self.factory.put('/emapi/addemployee/',self.body,content_type='application/json')
        putresponse=post(request)
        resultresponse=json.loads(putresponse.content.decode('ascii'))
        self.assertDictEqual(resultresponse, self.body)

    def test_duplicate_put(self):
        request=self.factory.put('/emapi/addemployee/',self.body,content_type='application/json')
        putresponse=post(request)
        request=self.factory.put('/emapi/addemployee/',self.body,content_type='application/json')
        putresponse=post(request)
        resultresponse=json.loads(putresponse.content.decode('ascii'))
        self.assertDictEqual(resultresponse, self.post_duplicate_resp)

    def test_neg_put(self):
        request=self.factory.put('/emapi/addemployee/',self.body_neg,content_type='application/json')
        putresponse=post(request)
        resultresponse=json.loads(putresponse.content.decode('ascii'))
        self.assertDictEqual(resultresponse, self.post_error)

    def test_empty_put(self):
        request=self.factory.put('/emapi/addemployee/',self.body_empty,content_type='application/json')
        putresponse=post(request)
        resultresponse=json.loads(putresponse.content.decode('ascii'))
        self.assertDictEqual(resultresponse, self.post_error)

    def test_index(self) :
        putrequest=self.factory.put('/emapi/addemployee/',self.body_reorder,content_type='application/json')
        putresponse=post(putrequest)
        request = self.factory.get ( '/emapi/employees' )
        response = index ( request )
        self.assertEqual ( response.status_code, 200)
        resultresponse=json.loads(response.content.decode('ascii'))
        putresultresponse=json.loads(response.content.decode('ascii'))
        self.assertDictEqual(resultresponse, putresultresponse)

    def test_list(self):
        putrequest=self.factory.put('/emapi/addemployee/',self.body,content_type='application/json')
        putresponse=post(putrequest)
        request = self.factory.get ( 'employee/<int:employee_id>/' )
        response = list ( request,self.employee_id )
        self.assertEqual ( response.status_code, 200)
        resultresponse=json.loads(response.content.decode('ascii'))
        self.assertDictEqual(resultresponse, self.body)

    def test_list_error(self):
        putrequest=self.factory.put('/emapi/addemployee/',self.body,content_type='application/json')
        putresponse=post(putrequest)
        request = self.factory.get ( 'employee/<int:employee_id>/' )
        response = list ( request,self.employee_id_test )
        self.assertEqual ( response.status_code, 404)
        resultresponse=json.loads(response.content.decode('ascii'))
        self.assertDictEqual(resultresponse, self.list_error)
        
