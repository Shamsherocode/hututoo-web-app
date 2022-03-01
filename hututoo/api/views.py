import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth.models import User
# from rest_framework import authentication, permissions
# from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
from .models import *
from .serializers import *
from .email import sendOTP

# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS


class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                sendOTP(serializer.data['email'])
                # return Response({
                #     'status': 200,
                #     'message': 'Register successfully',
                #     'data': serializer.data
                # })
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            # return Response({
            #         'status': 400,
            #         'message': 'Something went wrong',
            #         'data': serializer.errors
            #     })
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)


class QuizOptionView(APIView):
    # permission_classes = [ReadOnly]
    def get(self, request):
        data = QuizOption.objects.all()
        serializer = QuizOptionSerializer(data, many=True)
        return Response({'status': 200, 'payload': serializer.data})


class QuizCategoryView(APIView):
    # permission_classes = [ReadOnly]
    def get(self, request):
        data = QuizCategory.objects.all()
        serializer = QuizCategorySerializer(data, many=True)
        return Response({'status': 200, 'payload': serializer.data})



# class RegisterUser(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data = request.data)
#         if not serializer.is_valid():
#             return Response({'status': 403, 'payload': serializer.errors, 'message': 'Something went wrong'})

#         serializer.save()
#         user = User.objects.get(username = serializer.data['username'])
#         token , _ = Token.objects.get_or_create(user=user)
#         return Response({'status': 200, 'payload': serializer.data, 'token': str(token), 'message': 'You have successfully Register.'})
        # serializer.save()
        # user = User.objects.get(username = serializer.data['username'])
        # user.is_active = False
        # otp = random.randint(100000, 999999)
        # User.objects.create(user = user)
        # msg = f'Hello Alien...\nYour OTP is {otp}'
        # send_mail(
        #     'Welcome to Hututoo',
        #     msg,
        #     settings.EMAIL_HOST_USER,
        #     [user.username],
        #     fail_silently = False
        # )
        # token , _ = Token.objects.get_or_create(user=user)
        # return Response({'status': 200, 'payload': serializer.data, 'token': str(token), 'message': 'You have successfully Register.'})

class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyUserOTPSerializer(data = data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email = email)
                if not user.exists():
                    return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': 'Invalid Email address'
                    })

                if user[0].otp != otp:
                    return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': 'Invalid OTP'
                    })

                user = user.first()
                user.is_verified = True
                user.save() 
                return Response({
                        'status': 200,
                        'message': 'Email Verification is done..',
                        'data': serializer.data
                    })
                # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': serializer.errors
                    })

        except Exception as e:
            print(e)



class QuizView(APIView):
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