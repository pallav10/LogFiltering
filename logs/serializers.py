from django.forms import widgets
from rest_framework import serializers
from logs.models import logdata

class logdataSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    #log_id = serializers.CharField(max_length=200)
    #username = serializers.CharField(max_length=400)
    #byte_transferred = serializers.IntegerField(max_value=None, min_value=None)#CharField(max_length=100)#required=False
    mime = serializers.CharField(max_length=500)

    def create(self, validated_data):
        """
        Create and return a new `logdata` instance, given the validated data.
        """
        return logdata.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `logdata` instance, given the validated data.
        """
        #instance.log_id = validated_data.get('log_id', instance.log_id)
        #instance.username = validated_data.get('username', instance.username)
        #instance.byte_transferred = validated_data.get('byte_transferred', instance.byte_transferred)
        instance.mime = validated_data.get('mime')
        instance.save()
        return instance
    
    #def select(self, instance1, validated_data):
        """
        select and return the existing 'logdata' instance, given the validated data.
        """
