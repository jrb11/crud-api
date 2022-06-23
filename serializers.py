from dataclasses import fields
from rest_framework import serializers
from library.models import Book

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(label="Enter Book Title")
    author = serializers.CharField(label="Enter Author Name")
    isbn = serializers.CharField(label="Enter ISBN Number")
    publisher = serializers.CharField(label="Enter Publisher Name")
