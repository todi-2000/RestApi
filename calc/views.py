from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.serializers import Serializer
from .models import Calculator
from .serializers import CalculatorSerializer
# Create your views here.

class Calc(APIView):
    authentication_classes = []
    permission_classes = []


    def get(self,request,*args,**kwargs):
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['value1', 'value2','operation']
        value1=self.request.GET.get('value1')
        value2=self.request.GET.get('value2')
        operation=self.request.GET.get('operation')
        # print(operation)
        val=0
        if operation==" ":
            val=int(value1)+int(value2)
        elif operation=='-':
            val=int(value1)-int(value2)
        elif operation=='*':
            val=int(value1)*int(value2)
        ans=Calculator.objects.create(output=val)
        data=CalculatorSerializer(ans)
        return Response(data.data)

    def post(self,request,*args,**kwargs):
        val=0
        operation=self.request.query_params.get('operation')
        value1=self.request.query_params.get('value1')
        value2=self.request.query_params.get('value2')
        if operation==' ':
            val=int(value1)+int(value2)
        elif operation=='-':
            val=int(value1)-int(value2)
        elif operation=='*':
            val=int(value1)*int(value2)
        ans=Calculator.objects.create(output=val)
        serializer=CalculatorSerializer(ans)
        return Response(serializer.data)

     

