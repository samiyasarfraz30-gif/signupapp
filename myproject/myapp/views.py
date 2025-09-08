from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.
class SignupAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        
        if not username or not email:
            return Response({"Error": "You not add username or password"}, status=400)
        if User.objects.filter(username=username):
            return Response({"Error": "Already username exist."}, status=200)
        if User.objects.filter(email=email):
            return Response({"Error": "Already email exist."}, status=200)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        
        return Response({"Message": "User created successfully "}, status=201) 
    
    
    