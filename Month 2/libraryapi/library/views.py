from django.shortcuts import render
from .models import Book , Visitor 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import VisitorSerializer , BookSerializer

@api_view (["GET", "POST" ])
def listAllVisitorsAndCreate(request):
    if request.method=="POST":
        visitor_serializer=VisitorSerializer(data=request.data)
        if visitor_serializer.is_valid(raise_exception=True):
            visitor_serializer.save()
            return Response(visitor_serializer.data,status=status.HTTP_201_CREATED)


    if request.method=="GET":
     visitor=Visitor.objects.all()
     visitor_serializer=VisitorSerializer(visitor, many=True)
     return Response(visitor_serializer.data, status=status.HTTP_200_OK)

@api_view ([ "GET" , "PUT" , "PATCH" , "DELETE" ])
def readAndUpdateAndDeleteVisitor(request, id):
   
   if request.method=="GET":
     visitor=Visitor.objects.filter(id=id).first()
     if visitor:
        visitor_serializer=VisitorSerializer(visitor )
        return Response(visitor_serializer.data, status=status.HTTP_200_OK)
     
     return Response(status=status.HTTP_404_NOT_FOUND)
   
   if request.method=="PUT": 
       visitor=Visitor.objects.filter(id=id).first()
       if visitor is None :
        return Response ({"not found"} , status=status.HTTP_404_NOT_FOUND)
       visitorSerializer=VisitorSerializer(visitor, request.data)
       visitorSerializer.is_valid(raise_exception=True)
       visitorSerializer.save()


   partial=False
   if request.method=="PATCH":
     partial=True
     visitor=Visitor.objects.filter(id=id).first()
     if visitor is None :
        return Response ({"not found"} , status=status.HTTP_404_NOT_FOUND)
     visitorSerializer=VisitorSerializer(visitor, request.data, partial=partial )
     visitorSerializer.is_valid(raise_exception=True)
     visitorSerializer.save()
     return Response(visitorSerializer.data,status=status.HTTP_200_OK)
   

   if request.method=="DELETE":
       visitor=Visitor.objects.filter(id=id).first()
       if visitor is None :
        return Response ({"not found"} , status=status.HTTP_404_NOT_FOUND)
       visitor.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view (["GET", "POST" ])
def listAllBooksAndCreate(request):
    if request.method=="POST":
        book_serializer=BookSerializer(data=request.data)
        if book_serializer.is_valid(raise_exception=True):
            book_serializer.save()
            return Response(book_serializer.data,status=status.HTTP_201_CREATED)


    if request.method=="GET":
     book=Book.objects.all() ####
     book_serializer=BookSerializer(book, many=True)
     return Response(book_serializer.data, status=status.HTTP_200_OK)

@api_view ([ "GET" ,"PUT" , "PATCH" , "DELETE" ])
def readAndUpdateAndDeleteBooks(request, id):
   
   
   if request.method=="GET":
     book=book.objects.filter(id=id).first()
     if book:
        book_serializer=VisitorSerializer(book)
        return Response(book_serializer.data, status=status.HTTP_200_OK)
     
     return Response(status=status.HTTP_404_NOT_FOUND)
   

   if request.method=="PUT": 
       book=Book.objects.filter(id=id).first()
       if book is None :
        return Response ({"not found"} , status=status.HTTP_404_NOT_FOUND)
       book_serializer=BookSerializer(book, request.data)
       book_serializer.is_valid(raise_exception=True)
       book_serializer.save()


   partial=False
   if request.method=="PATCH":
     partial=True
     book=Book.objects.filter(id=id).first()
     if book is None :
        return Response ({"not found"} , status=status.HTTP_404_NOT_FOUND)
     bookSerializer=BookSerializer(book, request.data, partial=partial )
     bookSerializer.is_valid(raise_exception=True)
     bookSerializer.save()
     return Response(bookSerializer.data,status=status.HTTP_200_OK)
   

   if request.method=="DELETE":
       book=Book.objects.filter(id=id).first()
       if book is None :
        return Response ({"not found"} , status=status.HTTP_404_NOT_FOUND)
       book.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)

    
   