
from .models import Emp
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json

class empl_details(APIView):
    """ 
    APIs for CRUD - employ table
    """

    #empl_details/
    # {"name":"Jayanth","age":20,"email":"jayanth@gmail.com"}     
    def post(self, request):     
        """ post method - for creating user entry in employee table"""
        try:
            data=json.loads(request.body.decode('utf-8'))   #create new class
        except Exception as e:
            return JsonResponse({'status':400,'message':f'{e}'})

        try:
            """ input parameters """
            name = data['name']
            age= data['age']
            email = data['email']
        except KeyError as key_e:
            return JsonResponse({'status':400,'message':f'Error in key: {key_e}'})


        if Emp.objects.filter(name=name):       #filter from name
            return JsonResponse({'status':409,'message':'User already exist'})

        Emp.objects.create(name=name,age=age,email=email)  #create user
        resp=Emp.objects.all().values('id','name','age','email')
        return JsonResponse({'status':200,'message':'Successfully created','Employes':list(resp)})

    #empl_details/
    #{"id":1}
    def get(self, request): 
        """ get method - for reading user entry in employee table"""
        try:
            data=json.loads(request.body.decode('utf-8'))   #create new class
        except Exception as e:
            return JsonResponse({'status':400,'message':f'{e}'})

        try:
            id = data['id']         #get id
        except KeyError as key_e:
            return JsonResponse({'status':400,'message':f'Error in key: {key_e}'})

        emp_details=Emp.objects.filter(pk=id).first()       #filter for id
        if not emp_details:
            return JsonResponse({'status':204,'message':'No data'})
        result={'name':emp_details.name, \
            'age':emp_details.age, \
            'email':emp_details.email}

        return JsonResponse({'status':200,'result':result})

    #empl_details/
    #{"id":1,"name":"Jayanth chnged","age":20,"email":"jayanth@gmail.com"}  
    def put(self, request):
        """ put method - for updating user entry in employee table"""
        try:
            data=json.loads(request.body.decode('utf-8'))  

        except Exception as e:
            return JsonResponse({'status':400,'message':f'{e}'})
       
        try:
            """ get parameters for update """
            id = data['id']
            name= data['name']
            age = data['age']
            email = data['email']
        except KeyError as key_e:
            return JsonResponse({'status':400,'message':f'Error in key: {key_e}'})

        try:
            Emp.objects.filter(pk=id).update(
                    name=name,
                    age=age,
                    email=email)
 
        except KeyError as key_e:
            return JsonResponse({'status':400,'message':f'Error in key: {key_e}'})
        except Exception as e:
            return JsonResponse({'status':400,'message':f'{e}'})

        Emp.objects.create(name=name,age=age,email=email)
        resp=Emp.objects.all().values('id','name','age','email')
        return JsonResponse({'status':200,'message':'Successfully created','Employes':list(resp)})

    #empl_details/
    #{"id":1}
    def delete(self, request):   
        """ delete method - for deleting user entry in employee table"""
        try:
            data=json.loads(request.body.decode('utf-8'))  

        except Exception as e:
            return JsonResponse({'status':400,'message':f'{e}'})
       
        try:
            id_ = data['id']
        except KeyError as key_e:
            return JsonResponse({'status':400,'message':f'Error in key: {key_e}'})

          
        Emp.objects.filter(pk=id_).delete()         #deletes

        resp=Emp.objects.all().values('id','name','age','email')
        return JsonResponse({'status':200,'message':'Successfully created','Employes':list(resp)})