from django.shortcuts import render
import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def get_book(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj, many = True)
    return Response({'status':'200', 'payload': serializer.data})


from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'message': 'not a valid token'})
    
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response
        ({
         'status': 200,
         'payload': serializer.data, 
         'refresh': str(refresh),
         'access': str(refresh.access_token),
         'message': 'created'
        })

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication ]
    permission_classes = [IsAuthenticated]


    def get(self, request):

        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many = True)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self, request):

            data = request.data
            serializer = StudentSerializer(data = request.data)
            if not serializer.is_valid():
                return Response({'status': 403, 'message': 'not a valid serializer'})
            serializer.save()
            return Response({'status':200, 'payload': serializer.data})

    def put(self, request): 

        student_obj = Student.objects.get(id = request.data['id'])
        serializer = StudentSerializer(student_obj, data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'message': 'not a valid serializer'})
        serializer.save()
        return Response({'status':200, 'payload': serializer.data})

    def patch(self, request):
        student_obj = Student.objects.get(id = request.data['id'])
        serializer = StudentSerializer(student_obj, data = request.data, partial = True)
        if not serializer.is_valid():
            return Response({'status':403, 'message': 'not valid data'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data})

    def delete(self, request):
        id = request.GET.get('id')
        student_obj = Student.objects.get(id = id)
        student_obj.delete()
        return Response({'status': 200, 'message' : 'deleted'})

#?id=10 for deletion of data

from rest_framework import generics

class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentGenericUpdate(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'


































# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many = True)

#     return Response({'status': 200, 'payload': serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data = request.data)

#     if not serializer.is_valid():
#         return Response({'status' : 403, 'message' : 'something went wrong'})

#     serializer.save()
#     #print(data)
#     return Response({'status' : 200, 'payload' : data, 'message' : 'you sent'})

# @api_view(['PATCH'])
# def update_student(request, id):
    
#         student_obj = Student.objects.get(id = id)
#         serializer = StudentSerializer(student_obj, data = request.data, partial = True)

#         if not serializer.is_valid():
#             return Response({'status': 403, 'message': 'enter valid data'})

#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'meassage': 'can continue'})


#@api_view(['PUT'])
#def update_student(request, id):
    #student_obj = Student.objects.get(id = id)
    #serializer = StudentSerializer(student_obj, data = request.data)

    #if not serializer.is_valid():
            #return Response({'status': 403, 'message': 'enter valid data'})

    #serializer.save()
    #return Response({'status': 200, 'payload': serializer.data, 'meassage': 'can continue'})
        
#In case of put we have to input the whole packet of input only one elemnt cannot be updated but in case of patch we can update the single input also

# @api_view(['DELETE'])
# def delete_student(request, id):
#     id = request.GET.get('id')
#     student_obj = Student.objects.get(id = id)
#     student_obj.delete()
#     return Response({'status': 200, 'message':'deleted'})

