from rest_framework import serializers
from . import models
from django.utils import timezone


class Cash_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cash
        fields = '__all__'
        #read_only_fields = ("laboratoryid", 'analyteid', 'department')

    # def validate_name(self, value):
    #     if value == 'milad':
    #         raise serializers.ValidationError('you are blocked!')
    #     else:
    #         return value

    def update(self, instance, validated_data):
        old_laboratoryid = instance.laboratoryid
        old_analyteid = instance.old_analyteid
        old_department = instance.department
        obj = super().update(instance, validated_data)
        obj.laboratoryid = old_laboratoryid
        obj.analyteid = old_analyteid
        obj.department = old_department
        obj.save()
        return obj


class Analyte_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Analyte
        fields = '__all__'


class Device_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = '__all__'

class Tmethod_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Tmethod
        fields = '__all__'

class Devicecompany_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Devicecompany
        fields = '__all__'


class Facttable_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Facttable
        fields = '__all__'


class Info_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Info
        fields = '__all__'


class InfoDevice_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.InfoDevice
        fields = '__all__'


class InfoTD_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.InfoTD
        fields = '__all__'


class InfoTmethod_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.InfoTmethod
        fields = '__all__'


class Laboratory_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Laboratory
        fields = '__all__'


class Latnumber_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Latnumber
        fields = '__all__'


class Loc_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Loc
        fields = ['form','labid','loc']


class Tmethod_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Tmethod
        fields = '__all__'


class Singup_serializers(serializers.ModelSerializer):
    class Meta:
        model = models.Singup
        fields = '__all__'
