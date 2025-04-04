from rest_framework import serializers 
from .models import Author,Book
from datetime import date 


class BookSerializer(serializers.ModelSerializer):
  class meta:
    model = Book
    fields = '__all__'

    def validate_publication_year(self,value):
      if value > date.today().year:
        raise serializers.ValidationError("Publication year can't be in the future.")
      return value
    

class AuthorSerializer(serializers.ModelSerializer):
  books = BookSerializer(many=True, read_only=True)

  class meta:
    model = Author 
    fields = ['name', 'books']
    