from . import models
from .serializers import *


def formcash():
    objects = models.Facttable.objects.filter(laboratoryid=2).filter(date=timezone.datetime(2021, 4, 27)).filter(
        department=1).order_by('analyteid')
    data = {}
    for objec in objects:
        data[objec.analyteid] = {'testresult': objec.testresult,
                                 'devicetype': objec.devicetype,
                                 'latnumber': objec.latnumber,
                                 'testmethod': objec.testmethod,
                                 'kittype': objec.kittype,
                                 'analytecv': objec.analytecv,
                                 'analyteid': objec.analyteid,
                                 }
    return data


def Latnumbers_info():
    objects = models.Latnumber.objects.all()
    data = []
    for i in objects:
        if i.latnumber not in data:
            data.append(i.latnumber)
    return data


def old_days_data(request):
    objects = models.Facttable.objects.filter(department=get_department(request)['department']).filter(
        laboratoryid=request.user.last_name)
    data = []
    for i in objects:
        if i.date not in data:
            data.append(i.date)
    return data


def Laboratory_info(request):
    try:
        objects = models.Laboratory.objects.get(pk=request.user.last_name)
    except:
        return {'error': 'not found lab!'}
    ser = Laboratory_serializers(objects, many=False)
    return (ser.data)


def get_department(request):
    if request.path == '/formB':
        department = 1
        department_name = 'biochemistry'
    elif request.path == '/formHM':
        department = 2
        department_name = 'hematology'
    elif request.path == '/formHO':
        department = 3
        department_name = 'hormone'
    else:
        department = "can not found department ! "
        department_name = ''
    department = 1
    department_name = 'biochemistry'
    return {'department': department, 'department_name': department_name}


def UpdateCash(value):
    #     obj_cash = models.Cash.objects.filter(laboratoryid=value.laboratoryid).filter(analyteid=value.analyteid).filter(department=value.department)
    #     up = obj_cash.update(date=value.date,
    #                     kittype=value.kittype,
    #                     testmethod=value.testmethod,
    #                     devicetype=value.devicetype,
    #                     latnumber=value.latnumber,
    #                     analytecv=value.analytecv,
    #                     testresult=value.testresult)
    #
    objects = models.Cash.objects.filter(laboratoryid=value['laboratoryid']).filter(
        analyteid=value['analyteid']).filter(department=value['department'])
    if objects:
        result = objects.update(date=value['date'],
                                kittype=value['kittype'],
                                testmethod=value['testmethod'],
                                devicetype=value['devicetype'],
                                latnumber=value['latnumber'],
                                analytecv=value['analytecv'],
                                testresult=value['testresult'])
        return result
    else:
        return 0


def CashToFact(laboratoryid, department):
    Cash_objects = models.Cash.objects.filter(testresult__isnull=False).filter(laboratoryid=laboratoryid,
                                                                               department=department)
    if Cash_objects:
        for value in Cash_objects:
            value.date = timezone.now()
            fact_obj = models.Facttable(laboratoryid=value.laboratoryid, analyteid=value.analyteid,
                                        department=value.department, date=value.date,
                                        kittype=value.kittype,
                                        testmethod=value.testmethod,
                                        devicetype=value.devicetype,
                                        latnumber=value.latnumber,
                                        analytecv=value.analytecv,
                                        testresult=value.testresult)
            fact_obj.save()
            value.date = None
            value.kittype = None
            value.testmethod = None
            value.devicetype = None
            value.latnumber = None
            value.analytecv = None
            value.testresult = None
            value.save()
            return 1
    else:
        return 0


def Analyte_info():
    objects = models.Analyte.objects.filter(department='biochemistry')
    data = {}
    for objec in objects:
        data[objec.id] = {'analyte_name': objec.analyte_name,
                          'department': objec.department,
                          'accdev': objec.accdev,
                          'tea': objec.tea,
                          'unit': objec.unit,
                          'up': objec.up,
                          'down': objec.down,
                          }
    return (data)


def THUDAY():
    weekday = timezone.datetime('w')
    day = timezone.datetime('Y-m-d')


def Loc_info(request):
    obj = models.Loc.objects.filter(labid=request.user.last_name).filter(
        form=get_department(request)['department']).filter(loc=0)
    if obj:
        ser = Loc_serializers(obj, many=False)
        return (ser.data)
    else:
        return 'not found'


def Device_info(request):
    objects = models.Device.objects.filter(department=get_department(request)['department_name'])
    ser = Device_serializers(objects, many=True)
    data = {}
    for i in ser.data:
        data[i['id']] = i
    return (data)

def Tmethod_info(request):
    objects = models.Tmethod.objects.filter(department=get_department(request)['department_name'])
    ser = Tmethod_serializers(objects, many=True)
    data = {}
    for i in ser.data:
        data[i['id']] = i
    return (data)

def Devicecompany_info(request):
    objects = models.Devicecompany.objects.filter(department=get_department(request)['department_name'])
    ser = Devicecompany_serializers(objects, many=True)
    data = {}
    for i in ser.data:
        data[i['id']] = i
    return (data)
