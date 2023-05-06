from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from User.permissions import IsAdminOrReadOnly, UserAutentication
from Loan.serializers import LoanSerializer
from Loan.models import Loan


class CreateLoanView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = LoanSerializer


class UpdateLoanView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    lookup_url_kwarg = "loan_id"
