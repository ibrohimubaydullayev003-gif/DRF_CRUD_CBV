from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from .models import Car
from .serializer import CarSerializers


@api_view(['GET'])
def list_car(request):
    car = Car.objects.all()
    serializer = CarSerializers(car, many=True)
    
    return Response({
        'count': car.count(),
        'msg': 'list',
        'status': status.HTTP_200_OK,
        'data': serializer.data
    })


@api_view(['GET'])
def detail_car(request, pk):
    
    car = Car.objects.filter(pk=pk).first()
    
    if not car:
        raise ValidationError({'msg': 'car not found', 'status': status.HTTP_400_BAD_REQUEST})
    
    serialzier = CarSerializers(car)
    
    return Response({
        'msg': 'detail',
        'status': status.HTTP_200_OK,
        'data': serialzier.data
    })



@api_view(['POST'])
def create_car(request):
    
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
    
    
@api_view(['PUT'])
def update_car(request, pk):
    
    car = Car.objects.filter(pk=pk).first()
    
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
    
    
@api_view(['PATCH'])
def update_partial_car(request, pk):
    
    car = Car.objects.filter(pk=pk).first()
    
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
    

@api_view(['DELETE'])
def delete_car(request, pk):    
    car = Car.objects.filter(pk=pk).first()
    
    if not car:
        raise ValidationError({'msg': 'car not found', 'status': status.HTTP_400_BAD_REQUEST})
    
    car.delete()
    
    return Response({
        'msg': 'deleted',
        'status': status.HTTP_204_NO_CONTENT,
    })
