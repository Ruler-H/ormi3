from rest_framework import serializers
from .models import Post
from rest_framework.authtoken.models import Token # 토큰 모델 Token.objects.get() 이런 식으로 토큰 확인 가능
from rest_framework.validators import UniqueValidator # 중복 검사(회원 가입할 때 동일한 아이디가 있는지 검사 등)
from django.contrib.auth.password_validation import validate_password # 비밀번호 유효성 검사
from django.contrib.auth.models import User # User 모델(기본 User 모델 사용시 사용자명, 비밀번호, 이메일 필드만 사용 가능 => 상속받아 커스터마이징 가능)
from django.contrib.auth import authenticate

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    '''
    회원 가입 시리얼라이저
    '''
    username = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())] # 중복 검사
    )
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password], # 중복 검사
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True,
    )

    class Meta:
        model = User
        fields = '__all__' # ['필드명', '필드명', '필드명'] 이렇게 하는 것은 허용하지 않음


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': '비밀번호가 일치하지 않습니다.'})
        return attrs
        
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    '''
    로그인 시리얼라이저
    '''
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True) # write_only=True: password 필드는 읽기 전용으로 설정

    class Meta:
        model = User
        fields = ['username', 'password'] # 로그인 시 아이디와 비밀번호만 필요

    def validate(self, data):
        print(data)
        user = authenticate(**data)
        print(user)
        print(dir(user))
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError("유효하지 않은 로그인입니다.")