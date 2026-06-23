from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializer import CarSerializers
from .models import Car
from rest_framework.views import APIView




class list_create_car(APIView):
    def post(self, request):
        serializer = CarSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': 'Car create',
            'status': status.HTTP_201_CREATED,
            'car': serializer.data
        })

    def get(self, request):
        car = Car.objects.all()
        serializer = CarSerializers(car, many=True)

        return Response({
            'msg': 'Car list',
            'count': car.count(),
            'status': status.HTTP_200_OK,
            'list': serializer.data
        })


class update_delete_detail_car(APIView):

    def get_object(self, pk):
        car = Car.objects.filter(pk=pk).first()
        if not car:
            raise ValidationError({'msg': "Car not found", "status": status.HTTP_204_NO_CONTENT})

        return car

    def get(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializers(car)

        return Response({
            'msg': "Car detial",
            "status": status.HTTP_200_OK,
            "car": serializer.data
        })

    def delete(self, request, pk):
        car = self.get_object(pk)
        car.delete()

        return Response({
            'msg': "Car delete",
            "status": status.HTTP_204_NO_CONTENT
        })

    def put(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializers(instance=car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "msg": "Car update put",
            "status": status.HTTP_200_OK,
            "car": serializer.data
        })

    def patch(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializers(instance=car, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "msg": "Car update patch",
            "status": status.HTTP_200_OK,
            "car": serializer.data
        })













