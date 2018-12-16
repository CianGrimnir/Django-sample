#### Prerequisite:
Django

#### Running the application
python3 manage.py runserver 0.0.0.0

##### APIs
GET /emapi/employees   --> Get all the employees

GET /emapi/employee/<id> --> Get informaton of specific id

PUT /emapi/addemployee --> Put data for an employee with below json format

```
{
"employee": {
"employee_id" : "22",
"first_name": "Foo1",
"last_name": "Bar2",
"department": "Central2 Tech"
        }
}
```
