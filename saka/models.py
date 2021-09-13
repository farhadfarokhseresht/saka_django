from django.db import models


class Analyte(models.Model):
    analyte_name = models.CharField(max_length=30)
    department = models.TextField()
    accdev = models.FloatField(db_column='AccDEV')  # Field name made lowercase.
    tea = models.FloatField(db_column='TEa')  # Field name made lowercase.
    unit = models.CharField(max_length=30)
    up = models.IntegerField()
    down = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'analyte'


class Cash(models.Model):
    laboratoryid = models.IntegerField(db_column='laboratoryID')  # Field name made lowercase.
    analyteid = models.IntegerField(db_column='analyteID')  # Field name made lowercase.
    department = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    kittype = models.IntegerField(blank=True, null=True)
    testmethod = models.IntegerField(blank=True, null=True)
    devicetype = models.IntegerField(blank=True, null=True)
    latnumber = models.CharField(max_length=300, blank=True, null=True)
    analytecv = models.FloatField(db_column='analyteCV', blank=True, null=True)  # Field name made lowercase.
    testresult = models.FloatField(db_column='testResult', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'cash'

    def __str__(self):
        return '%s,%s,%s,%s,%s' % (self.laboratoryid, self.analyteid, self.department, self.date,self.testresult)


class Device(models.Model):
    devicename = models.CharField(max_length=50)
    department = models.CharField(max_length=30)

    class Meta:
        # managed = False
        db_table = 'device'


class Devicecompany(models.Model):
    companyname = models.CharField(db_column='Companyname', max_length=50)  # Field name made lowercase.
    department = models.CharField(max_length=30)

    class Meta:
        # managed = False
        db_table = 'devicecompany'


class Facttable(models.Model):
    laboratoryid = models.IntegerField(db_column='laboratoryID')  # Field name made lowercase.
    analyteid = models.IntegerField(db_column='analyteID')  # Field name made lowercase.
    department = models.IntegerField()
    date = models.DateField()
    kittype = models.IntegerField()
    testmethod = models.IntegerField()
    devicetype = models.IntegerField()
    latnumber = models.CharField(max_length=300)
    analytecv = models.FloatField(db_column='analyteCV')  # Field name made lowercase.
    testresult = models.FloatField(db_column='testResult')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'facttable'


class Info(models.Model):
    laboratoryid = models.IntegerField(db_column='laboratoryID')  # Field name made lowercase.
    analyteid = models.IntegerField(db_column='analyteID')  # Field name made lowercase.
    department = models.IntegerField()
    date = models.DateField()
    kittype = models.IntegerField()
    testmethod = models.IntegerField()
    devicetype = models.IntegerField()
    latnumber = models.CharField(max_length=300)
    analytecv = models.FloatField(db_column='analyteCV')  # Field name made lowercase.
    testresult = models.FloatField(db_column='testResult')  # Field name made lowercase.
    mean = models.FloatField(db_column='Mean', blank=True, null=True)  # Field name made lowercase.
    bias = models.FloatField(db_column='Bias', blank=True, null=True)  # Field name made lowercase.
    sd = models.FloatField(db_column='SD', blank=True, null=True)  # Field name made lowercase.
    adjmean = models.FloatField(db_column='adjMean', blank=True, null=True)  # Field name made lowercase.
    adjsd = models.FloatField(db_column='adjSD', blank=True, null=True)  # Field name made lowercase.
    cv = models.FloatField(blank=True, null=True)
    dev = models.FloatField(db_column='DEV', blank=True, null=True)  # Field name made lowercase.
    sdi = models.FloatField(db_column='SDI', blank=True, null=True)  # Field name made lowercase.
    um = models.FloatField(db_column='Um', blank=True, null=True)  # Field name made lowercase.
    n = models.IntegerField(db_column='N')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'info'


class InfoDevice(models.Model):
    laboratoryid = models.IntegerField(db_column='laboratoryID')  # Field name made lowercase.
    analyteid = models.IntegerField(db_column='analyteID')  # Field name made lowercase.
    department = models.IntegerField()
    date = models.DateField()
    kittype = models.IntegerField()
    testmethod = models.IntegerField()
    devicetype = models.IntegerField()
    latnumber = models.CharField(max_length=300)
    analytecv = models.FloatField(db_column='analyteCV')  # Field name made lowercase.
    testresult = models.FloatField(db_column='testResult')  # Field name made lowercase.
    mean = models.FloatField(db_column='Mean', blank=True, null=True)  # Field name made lowercase.
    bias = models.FloatField(db_column='Bias', blank=True, null=True)  # Field name made lowercase.
    sd = models.FloatField(db_column='SD', blank=True, null=True)  # Field name made lowercase.
    adjmean = models.FloatField(db_column='adjMean', blank=True, null=True)  # Field name made lowercase.
    adjsd = models.FloatField(db_column='adjSD', blank=True, null=True)  # Field name made lowercase.
    cv = models.FloatField(blank=True, null=True)
    dev = models.FloatField(db_column='DEV', blank=True, null=True)  # Field name made lowercase.
    sdi = models.FloatField(db_column='SDI', blank=True, null=True)  # Field name made lowercase.
    um = models.FloatField(db_column='Um', blank=True, null=True)  # Field name made lowercase.
    n = models.IntegerField(db_column='N')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'info_device'


class InfoTD(models.Model):
    laboratoryid = models.IntegerField(db_column='laboratoryID')  # Field name made lowercase.
    analyteid = models.IntegerField(db_column='analyteID')  # Field name made lowercase.
    department = models.IntegerField()
    date = models.DateField()
    kittype = models.IntegerField()
    testmethod = models.IntegerField()
    devicetype = models.IntegerField()
    latnumber = models.CharField(max_length=300)
    analytecv = models.FloatField(db_column='analyteCV')  # Field name made lowercase.
    testresult = models.FloatField(db_column='testResult')  # Field name made lowercase.
    mean = models.FloatField(db_column='Mean', blank=True, null=True)  # Field name made lowercase.
    bias = models.FloatField(db_column='Bias', blank=True, null=True)  # Field name made lowercase.
    sd = models.FloatField(db_column='SD', blank=True, null=True)  # Field name made lowercase.
    adjmean = models.FloatField(db_column='adjMean', blank=True, null=True)  # Field name made lowercase.
    adjsd = models.FloatField(db_column='adjSD', blank=True, null=True)  # Field name made lowercase.
    cv = models.FloatField(blank=True, null=True)
    dev = models.FloatField(db_column='DEV', blank=True, null=True)  # Field name made lowercase.
    sdi = models.FloatField(db_column='SDI', blank=True, null=True)  # Field name made lowercase.
    um = models.FloatField(db_column='Um', blank=True, null=True)  # Field name made lowercase.
    n = models.IntegerField(db_column='N')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'info_t_d'


class InfoTmethod(models.Model):
    laboratoryid = models.IntegerField(db_column='laboratoryID')  # Field name made lowercase.
    analyteid = models.IntegerField(db_column='analyteID')  # Field name made lowercase.
    department = models.IntegerField()
    date = models.DateField()
    kittype = models.IntegerField()
    testmethod = models.IntegerField()
    devicetype = models.IntegerField()
    latnumber = models.CharField(max_length=300)
    analytecv = models.FloatField(db_column='analyteCV')  # Field name made lowercase.
    testresult = models.FloatField(db_column='testResult')  # Field name made lowercase.
    mean = models.FloatField(db_column='Mean', blank=True, null=True)  # Field name made lowercase.
    bias = models.FloatField(db_column='Bias', blank=True, null=True)  # Field name made lowercase.
    sd = models.FloatField(db_column='SD', blank=True, null=True)  # Field name made lowercase.
    adjmean = models.FloatField(db_column='adjMean', blank=True, null=True)  # Field name made lowercase.
    adjsd = models.FloatField(db_column='adjSD', blank=True, null=True)  # Field name made lowercase.
    cv = models.FloatField(blank=True, null=True)
    dev = models.FloatField(db_column='DEV', blank=True, null=True)  # Field name made lowercase.
    sdi = models.FloatField(db_column='SDI', blank=True, null=True)  # Field name made lowercase.
    um = models.FloatField(db_column='Um', blank=True, null=True)  # Field name made lowercase.
    n = models.IntegerField(db_column='N')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'info_tmethod'


class Laboratory(models.Model):
    lab_id = models.AutoField(primary_key=True)
    laboratory_name = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    pass_field = models.CharField(db_column='pass',
                                  max_length=32)  # Field renamed because it was a Python reserved word.
    role = models.CharField(max_length=50)
    phnuber = models.CharField(max_length=12)
    email = models.CharField(max_length=255)
    province = models.CharField(db_column='Province', max_length=300)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=300)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'laboratory'


class Latnumber(models.Model):
    latnumber = models.CharField(max_length=300)

    class Meta:
        # managed = False
        db_table = 'latnumber'


class Loc(models.Model):
    form = models.IntegerField()
    labid = models.IntegerField()
    loc = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'loc'


class Singup(models.Model):
    name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    province = models.CharField(db_column='Province', max_length=50)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'singup'


class Tmethod(models.Model):
    methodname = models.CharField(max_length=50)
    analytename = models.CharField(max_length=50)
    department = models.CharField(max_length=20)

    class Meta:
        # managed = False
        db_table = 'tmethod'
