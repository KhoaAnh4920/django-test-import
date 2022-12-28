from rest_framework import serializers, exceptions
from member.models import Member


class MemberSerializer(serializers.Serializer):
    firstname = serializers.CharField(required=True, max_length=30, error_messages={
                                      'required': 'First name is required', 'max_length': 'First name can not be than 30 characters', 'blank': 'First name can not blank', 'null': 'First name can not null'})
    lastname = serializers.CharField(required=True, max_length=30, error_messages={
        'required': 'Last name is required', 'max_length': 'Last name can not be than 30 characters', 'blank': 'Last name can not blank', 'null': 'Last name can not null'})
    email = serializers.EmailField(required=True, error_messages={
        'required': 'Email is required', 'blank': 'Email can not blank', 'null': 'Email can not null', 'invalid': 'Invalid Email Format', 'unique': 'Email already exist'})
    birth_date = serializers.DateField(required=True, error_messages={
        'required': 'Birth day is required', 'blank': 'Birth day can not blank', 'null': 'Birth day can not null', 'invalid': 'Invalid Date Format'})
    contact = serializers.CharField(
        required=True, max_length=100, allow_blank=True, error_messages={
            'required': 'Contact is required', 'max_length': 'Contact can not be than 100 characters', 'null': 'Contact can not null'})
    parent = serializers.IntegerField(required=True, allow_null=True, error_messages={
        'required': 'Parent is required', 'invalid': 'Parent must be a number or NULL'})

    def validate_data(email, parent):
        error = ''
        member = Member.objects._mptt_filter(email=email).first()
        if member:
            error += ', Email already exist'
        try:
            parent_id = int(parent)
            if parent is not None:
                member_parent = Member.objects._mptt_filter(
                    parent_id=parent_id).first()
                if not member_parent:
                    error += f', Not found member with id {parent_id}'
        except:
            error += ', Parent must be a number'
        return error
