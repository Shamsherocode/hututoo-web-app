from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
from .models import *
from .serializers import *
from .email import sendOTP
from functools import partial

import json
import threading
import hashlib

class EmailThread(threading.Thread):
    def __init__(self, sendOTP):
        self.sendOTP = sendOTP
        threading.Thread.__init__(self)

    def run(self):
        self.sendOTP()
       

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class MyPermission(permissions.BasePermission):
    def __init__(self, allowed_methods):
        super().__init__()
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        return request.method in self.allowed_methods


class UserRegister(APIView):
    # permission_classes = [ReadOnly]
    def post(self, request):
        try:
            data = request.data
            serializer = RegitserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                sendOTP(data['email'])
                return Response({
                    'status': 200,
                    'message': 'Verification code sent on the mail address. Please check',
                })
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)

class LoginUser(APIView):
    # permission_classes = (partial(MyPermission, ['GET', 'POST', 'HEAD']),)
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data)
            verify_user = RegisterUser.objects.filter(email = data['email'])
            if not verify_user:
                user = RegisterUser(email = data['email'])
                user.save()
            else:
                user = verify_user[0]
            sendOTP(user)
            return Response({
            'status': 200,
            'message': 'Verification code sent on the mail address. Please check',
            'data': serializer.data,
            })
        except: 
            return Response({
            'status': 400,
            'message': 'Please Type correct Email Address',
            })

class UserProfileView(APIView):
    # permission_classes = [ReadOnly]
    def get(self, request, user):
        try: 
            user_profile = UserProfile.objects.get(user__email=user)
            profile_serializer = UserProfileSerializer(user_profile)
            return Response({'status': 200, 'payload': profile_serializer.data})
        except:
            return Response({'status': 400, 'message': 'Unauthenticted User'})

class EventOptionView(APIView):
    # permission_classes = [ReadOnly]
    def get(self, request):
        data = QuizOption.objects.all()
        serializer = QuizOptionSerializer(data, many=True)
        return Response({'status': 200, 'payload': serializer.data})

class EventCategoryView(APIView):
    # permission_classes = [ReadOnly]
    def get(self, request):
        data = QuizCategory.objects.all()
        serializer = QuizCategorySerializer(data, many=True)
        return Response({'status': 200, 'payload': serializer.data})

class VerifyOTP(APIView):
    # permission_classes = (partial(MyPermission, ['GET', 'POST', 'HEAD']),)
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyUserOTPSerializer(data = data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                try:
                    user = RegisterUser.objects.get(email=email)
                    if user.otp != otp:
                        return Response({
                            'status': 400,
                            'message': 'Invalid OTP. Please enter corrent OTP',  
                        })
                    else:
                        if not user.is_verified:
                            user.is_verified = True

                            user.save()
                            privat_key_gen = hashlib.sha256(b'data.email + data.id')
                            key = privat_key_gen.hexdigest()
                            profile = UserProfile(user = user, private_key = key)
                            profile.save()
                            points = Transaction(user = user, user_points=10000, points_method=1, points_status=1)
                            points.save()
                        return Response({
                                'status': 200,
                                'message': 'Email Verification is done..',
                            })
                except:
                    return Response({
                        'status': 400,
                        'message': 'Email not found. Please enter corrent Email Address',
                        
                    })

            return Response({
                        'status': 400,
                        'payload': serializer.errors,
                        
                    })
        except:
            return Response({
                        'status': 400,
                        'message': 'Something Went Wrong',
                    })

class EventView(APIView):
    # permission_classes = [ReadOnly]
    def get(self, request):
        quizs = Quizs.objects.all()
        serializer = QuizSerializer(quizs, many=True)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self, request):
        serializer = QuizSerializer(data = request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'payload': serializer.errors, 'message': 'Something went wrong'})

        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'You have successfully Created Quiz.'})


    def put(self, request):
        try:
            quizs = Quizs.objects.get(id = request.data['id'])
            serializer = QuizSerializer(quizs, data = request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'payload': serializer.errors, 'message': 'Something went wrong'})

            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'You have successfully Created Quiz.'})

        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid ID'})

    def patch(self, request):
        try:
            quizs = Quizs.objects.get(id = request.data['id'])
            serializer = QuizSerializer(quizs, data = request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'payload': serializer.errors, 'message': 'Something went wrong'})

            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'You have successfully Created Quiz.'})

        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid ID'})


    def delete(self, request):
        try:
            id = request.GET.get('id')
            quizs = Quizs.objects.get(id=id)
            quizs.delete()
            return Response({'status': 200, 'message': 'Quiz Successfully deleted'})
        
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid ID'})

class TransactionView(APIView):
    def get(self, request, user):
        try: 
            transaction = Transaction.objects.get(user__email=user)
            transactions = TransactionSerializer(transaction)
            return Response({'status': 200, 'payload': transactions.data})
        except:
            return Response({'status': 400, 'message': 'Unauthenticted User'})