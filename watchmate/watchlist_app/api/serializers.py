from dataclasses import field
from wsgiref.validate import validator
from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'
        
    # def validate_title(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Title is too short !")
    #     else:
    #         return value
        
    # def validate(self, data):
    #     if data['title'] == data['storyline']:
    #         raise serializers.ValidationError("Name and Description should not be same !")
    #     else:
    #         return data
        
    # def validate(self, data):
    #     if data["title"] == data["storyline"]:
    #         return serializers.ValidationError("Title & Description should be different !")
    #     else:
    #         raise data
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    WatchList = WatchListSerializer(many=True, read_only=True)
    # WatchList = serializers.StringRelatedField(many=True)
    # WatchList = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # WatchList = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-details'
    # )
    # WatchList = serializers.HyperlinkedIdentityField(view_name='movie-details')
    class Meta:
        model = StreamPlatform
        fields = '__all__'

# class MovieSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Movie
#         fields = '__all__'
#         # exclude = ['name']
#         # fields = ['name','description','active']
        
#     def get_len_name(self, objects):
#         return len(objects.name)
#         # length = len(objects.name)

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should not be same.")
#         else:
#             return data
    
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         else:
#             return value

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
    # active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should not be same.")
#         else:
#             return data
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     return value 