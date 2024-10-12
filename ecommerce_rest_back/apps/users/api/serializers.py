from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self,validated_data):
        user= User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }

'''
serializer de prueba
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 50)
    email = serializers.EmailField()

    def validate_name(self, value):
        #custom validation
        if 'developer' in value:
            raise serializers.ValidationError("Usuario invalido")
        return value
    
    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError("Debe haber un correo")
        
        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError("No puede cotener lo mismo")
        
        return value

    def validate(self, data):
        return data
    
    def create(self, validated_data):"
    #    print(validated_data)
    #    return Test(**validated_data)

    def update(self, instance, validated_data):
        print(instance)
        print(validated_data)
        #ejemplo
            instance.name = validated_data.get('name', instance.name)
            instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


    def save(self):
        
    '''