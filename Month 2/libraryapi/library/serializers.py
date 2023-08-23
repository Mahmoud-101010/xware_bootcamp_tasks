from rest_framework import serializers
from .models import Book ,Visitor

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields='__all__'
class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visitor
        fields='__all__'