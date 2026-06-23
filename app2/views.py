from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializer import CarSerializers
from .models import Car
from rest_framework.decorators import api_view




@api_view(['POST', "GET"])
def list_create_car(request):
    if request.method == 'POST':
        serializer = CarSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response({
                'msg': 'Created',
                'status': status.HTTP_201_CREATED,
                'data': serializer.data
            })
            
        raise ValidationError({
                'error': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST
                }) 
    elif request.method == 'GET':
        car = Car.objects.all()
        serializer = CarSerializers(car, many=True)
        
        return Response({
            'count': car.count(),
            'msg': 'list',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

@api_view(['PUT', 'PATCH',  "DELETE", 'GET'])
def update_delete_detail_car(request, pk):
    
    def get_object():
        car = Car.objects.filter(pk=pk).first()
    
        if not car:
            raise ValidationError({'msg': 'car not found', 'status': status.HTTP_400_BAD_REQUEST})
        return car
        
    
    if request.method == 'GET':
        car = get_object()
        serialzier = CarSerializers(car)
        return Response({
            'msg': 'detail',
            'status': status.HTTP_200_OK,
            'data': serialzier.data
        })
        
    elif request.method == 'DELETE':
        car = get_object()
        car.delete()
        return Response({
            'msg': 'deleted',
            'status': status.HTTP_204_NO_CONTENT,
        }) 
        
    elif request.method == 'PUT':
        car = get_object()
        if not car:
            raise ValidationError({'msg': 'car not found', 'status': status.HTTP_400_BAD_REQUEST})
        serializer = CarSerializers(instance=car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg': 'Updated',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })
        
    elif request.method == 'PATCH':
        car = get_object
        if not car:
            raise ValidationError({'msg': 'car not found', 'status': status.HTTP_400_BAD_REQUEST})
        serializer = CarSerializers(instance=car, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg': 'Updated',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })



