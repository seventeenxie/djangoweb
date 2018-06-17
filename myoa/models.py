# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class XinhuAdmin(models.Model):
    num = models.CharField(max_length=20, blank=True, null=True)
    user = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    loginci = models.SmallIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    face = models.CharField(max_length=50, blank=True, null=True)
    deptid = models.IntegerField(blank=True, null=True)
    deptname = models.CharField(max_length=50, blank=True, null=True)
    deptids = models.CharField(max_length=30, blank=True, null=True)
    deptnames = models.CharField(max_length=100, blank=True, null=True)
    rankings = models.CharField(max_length=100, blank=True, null=True)
    deptallname = models.CharField(max_length=100, blank=True, null=True)
    superid = models.CharField(max_length=50, blank=True, null=True)
    superman = models.CharField(max_length=20, blank=True, null=True)
    ranking = models.CharField(max_length=255, blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    deptpath = models.CharField(max_length=100, blank=True, null=True)
    superpath = models.CharField(max_length=100, blank=True, null=True)
    groupname = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    apptx = models.IntegerField(blank=True, null=True)
    workdate = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    lastpush = models.DateTimeField(blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    weixinid = models.CharField(max_length=50, blank=True, null=True)
    quitdt = models.DateField(blank=True, null=True)
    style = models.IntegerField(blank=True, null=True)
    pingyin = models.CharField(max_length=50, blank=True, null=True)
    emailpass = models.CharField(max_length=100, blank=True, null=True)
    companyid = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    lastonline = models.DateTimeField(blank=True, null=True)
    duty = models.SmallIntegerField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    issalekpi = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_admin'
        unique_together = (('id', 'user'),)


class XinhuAssetm(models.Model):
    typeid = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    laiyuan = models.CharField(max_length=50, blank=True, null=True)
    shuname = models.CharField(max_length=50, blank=True, null=True)
    dt = models.DateField(blank=True, null=True)
    ckid = models.SmallIntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    buydt = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    useid = models.CharField(max_length=50, blank=True, null=True)
    usename = models.CharField(max_length=50, blank=True, null=True)
    fengmian = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_assetm'


class XinhuBook(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    typeid = models.SmallIntegerField(blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    chuban = models.CharField(max_length=50, blank=True, null=True)
    cbdt = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weizhi = models.CharField(max_length=50, blank=True, null=True)
    shul = models.SmallIntegerField(blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    isbn = models.CharField(max_length=30, blank=True, null=True)
    jieshu = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_book'


class XinhuBookborrow(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    bookid = models.SmallIntegerField(blank=True, null=True)
    bookname = models.CharField(max_length=50, blank=True, null=True)
    jydt = models.DateField(blank=True, null=True)
    yjdt = models.DateField(blank=True, null=True)
    ghtime = models.DateTimeField(blank=True, null=True)
    isgh = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_bookborrow'


class XinhuCarm(models.Model):
    carnum = models.CharField(max_length=10, blank=True, null=True)
    carbrand = models.CharField(max_length=20, blank=True, null=True)
    carmode = models.CharField(max_length=30, blank=True, null=True)
    cartype = models.CharField(max_length=10, blank=True, null=True)
    buydt = models.DateField(blank=True, null=True)
    buyprice = models.IntegerField(blank=True, null=True)
    enginenb = models.CharField(max_length=50, blank=True, null=True)
    ispublic = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    createname = models.CharField(max_length=20, blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    framenum = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_carm'


class XinhuCarmang(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    carid = models.SmallIntegerField(blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    jianame = models.CharField(max_length=50, blank=True, null=True)
    jiaid = models.CharField(max_length=50, blank=True, null=True)
    bujian = models.CharField(max_length=200, blank=True, null=True)
    startdt = models.DateTimeField(blank=True, null=True)
    enddt = models.DateTimeField(blank=True, null=True)
    money = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    nextdt = models.DateField(blank=True, null=True)
    kmshu = models.CharField(max_length=20, blank=True, null=True)
    kmnshu = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_carmang'


class XinhuCarmrese(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    useid = models.CharField(max_length=200, blank=True, null=True)
    usename = models.CharField(max_length=200, blank=True, null=True)
    useren = models.SmallIntegerField(blank=True, null=True)
    startdt = models.DateTimeField(blank=True, null=True)
    enddt = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    carid = models.SmallIntegerField(blank=True, null=True)
    carnum = models.CharField(max_length=10, blank=True, null=True)
    xianlines = models.CharField(max_length=200, blank=True, null=True)
    jiaid = models.CharField(max_length=200, blank=True, null=True)
    jianame = models.CharField(max_length=200, blank=True, null=True)
    kmstart = models.CharField(max_length=20, blank=True, null=True)
    kmend = models.CharField(max_length=20, blank=True, null=True)
    returndt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_carmrese'


class XinhuCarms(models.Model):
    carid = models.IntegerField(blank=True, null=True)
    otype = models.CharField(max_length=20, blank=True, null=True)
    startdt = models.DateField(blank=True, null=True)
    enddt = models.DateField(blank=True, null=True)
    money = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    unitname = models.CharField(max_length=50, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    jiaid = models.CharField(max_length=30, blank=True, null=True)
    jianame = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_carms'


class XinhuCash(models.Model):
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    way = models.CharField(max_length=3, blank=True, null=True)
    optdate = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    istofinance = models.IntegerField(blank=True, null=True)
    privateid = models.IntegerField(blank=True, null=True)
    finid = models.IntegerField(blank=True, null=True)
    salaryid = models.IntegerField(blank=True, null=True)
    jhkid = models.IntegerField(blank=True, null=True)
    heid = models.IntegerField(blank=True, null=True)
    happenddate = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_cash'


class XinhuChargems(models.Model):
    type = models.IntegerField(blank=True, null=True)
    mid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    updatedt = models.DateTimeField(blank=True, null=True)
    key = models.CharField(max_length=200, blank=True, null=True)
    modeid = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_chargems'


class XinhuCity(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=50)
    type = models.IntegerField()
    sort = models.SmallIntegerField(blank=True, null=True)
    pinyin = models.CharField(max_length=50, blank=True, null=True)
    pinyins = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_city'


class XinhuCompany(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    nameen = models.CharField(max_length=200, blank=True, null=True)
    tel = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    fuzeid = models.CharField(max_length=30, blank=True, null=True)
    fuzename = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_company'


class XinhuCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_country'


class XinhuCountryCopy(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_country_copy'


class XinhuCustfina(models.Model):
    htid = models.IntegerField(blank=True, null=True)
    htnum = models.CharField(max_length=20, blank=True, null=True)
    dt = models.DateField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    custid = models.SmallIntegerField(blank=True, null=True)
    custname = models.CharField(max_length=50, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optname = models.CharField(max_length=10, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    ispay = models.IntegerField(blank=True, null=True)
    paydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=200, blank=True, null=True)
    createdt = models.DateTimeField(blank=True, null=True)
    createname = models.CharField(max_length=10, blank=True, null=True)
    creatid = models.SmallIntegerField(blank=True, null=True)
    ismove = models.IntegerField(blank=True, null=True)
    createid = models.SmallIntegerField(blank=True, null=True)
    moneyto = models.CharField(max_length=10, blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_custfina'


class XinhuCustomer(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optname = models.CharField(max_length=10, blank=True, null=True)
    linkname = models.CharField(max_length=20, blank=True, null=True)
    unitname = models.CharField(max_length=100, blank=True, null=True)
    laiyuan = models.CharField(max_length=40, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    routeline = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    createname = models.CharField(max_length=10, blank=True, null=True)
    creatid = models.SmallIntegerField(blank=True, null=True)
    shate = models.CharField(max_length=50, blank=True, null=True)
    shateid = models.CharField(max_length=50, blank=True, null=True)
    isgys = models.IntegerField(blank=True, null=True)
    isstat = models.IntegerField(blank=True, null=True)
    fzid = models.SmallIntegerField(blank=True, null=True)
    fzname = models.CharField(max_length=20, blank=True, null=True)
    htshu = models.SmallIntegerField(blank=True, null=True)
    moneyz = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    moneyd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    code = models.CharField(max_length=15)
    level = models.IntegerField()
    country = models.CharField(max_length=200, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    qq = models.CharField(max_length=18, blank=True, null=True)
    wechat = models.CharField(max_length=20, blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    skype = models.CharField(max_length=30, blank=True, null=True)
    bosstel = models.CharField(max_length=20, blank=True, null=True)
    managertel = models.CharField(max_length=20, blank=True, null=True)
    companytel = models.CharField(max_length=10, blank=True, null=True)
    salemantel = models.CharField(max_length=10, blank=True, null=True)
    desktel = models.CharField(max_length=10, blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    createid = models.SmallIntegerField(blank=True, null=True)
    sheng = models.CharField(max_length=50, blank=True, null=True)
    shi = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    askdate = models.DateField(blank=True, null=True)
    isdis = models.CharField(max_length=50, blank=True, null=True)
    isfenpei = models.IntegerField(blank=True, null=True)
    alitm = models.CharField(max_length=10, blank=True, null=True)
    potenmoney = models.IntegerField(blank=True, null=True)
    fallow = models.TextField(blank=True, null=True)
    monthpro = models.IntegerField(blank=True, null=True)
    weekpro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_customer'


class XinhuCustomerdetali(models.Model):
    mid = models.SmallIntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    impression = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_customerdetali'


class XinhuCustract(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    num = models.CharField(max_length=30, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    custid = models.IntegerField(blank=True, null=True)
    custname = models.CharField(max_length=255, blank=True, null=True)
    linkman = models.CharField(max_length=20, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    moneys = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    startdt = models.DateField(blank=True, null=True)
    enddt = models.DateField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    saleid = models.SmallIntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    signdt = models.DateField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    ispay = models.IntegerField(blank=True, null=True)
    isover = models.IntegerField(blank=True, null=True)
    createname = models.CharField(max_length=20, blank=True, null=True)
    createid = models.SmallIntegerField(blank=True, null=True)
    profile = models.CharField(max_length=10, blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    invoice = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    selfcommission = models.FloatField(blank=True, null=True)
    deptcommission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    formula = models.CharField(max_length=50, blank=True, null=True)
    isoutsell = models.IntegerField(blank=True, null=True)
    bonus = models.IntegerField(blank=True, null=True)
    extrafee = models.CharField(max_length=10, blank=True, null=True)
    invoicecost = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ifdeptcommissionpyay = models.CharField(max_length=2, blank=True, null=True)
    isselfcommissionpay = models.CharField(max_length=2, blank=True, null=True)
    ifinvoicepay = models.CharField(max_length=2, blank=True, null=True)
    actualdate = models.DateField(blank=True, null=True)
    returntax = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    brand = models.CharField(max_length=8, blank=True, null=True)
    statetext = models.IntegerField(blank=True, null=True)
    producttype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_custract'


class XinhuCustsale(models.Model):
    custid = models.IntegerField(blank=True, null=True)
    custname = models.CharField(max_length=50, blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=10, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    dealdt = models.DateTimeField(blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    laiyuan = models.CharField(max_length=20, blank=True, null=True)
    createid = models.SmallIntegerField(blank=True, null=True)
    createname = models.CharField(max_length=20, blank=True, null=True)
    htid = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_custsale'


class XinhuDaily(models.Model):
    dt = models.DateField(blank=True, null=True)
    content = models.CharField(max_length=4000, blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    plan = models.CharField(max_length=2000, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    enddt = models.DateField(blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    mark = models.SmallIntegerField(blank=True, null=True)
    bigplan = models.TextField(blank=True, null=True)
    problem = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_daily'


class XinhuDailyfx(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=10, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    day1 = models.IntegerField(blank=True, null=True)
    day2 = models.IntegerField(blank=True, null=True)
    day3 = models.IntegerField(blank=True, null=True)
    day4 = models.IntegerField(blank=True, null=True)
    day5 = models.IntegerField(blank=True, null=True)
    day6 = models.IntegerField(blank=True, null=True)
    day7 = models.IntegerField(blank=True, null=True)
    day8 = models.IntegerField(blank=True, null=True)
    day9 = models.IntegerField(blank=True, null=True)
    day10 = models.IntegerField(blank=True, null=True)
    day11 = models.IntegerField(blank=True, null=True)
    day12 = models.IntegerField(blank=True, null=True)
    day13 = models.IntegerField(blank=True, null=True)
    day14 = models.IntegerField(blank=True, null=True)
    day15 = models.IntegerField(blank=True, null=True)
    day16 = models.IntegerField(blank=True, null=True)
    day17 = models.IntegerField(blank=True, null=True)
    day18 = models.IntegerField(blank=True, null=True)
    day19 = models.IntegerField(blank=True, null=True)
    day20 = models.IntegerField(blank=True, null=True)
    day21 = models.IntegerField(blank=True, null=True)
    day22 = models.IntegerField(blank=True, null=True)
    day23 = models.IntegerField(blank=True, null=True)
    day24 = models.IntegerField(blank=True, null=True)
    day25 = models.IntegerField(blank=True, null=True)
    day26 = models.IntegerField(blank=True, null=True)
    day27 = models.IntegerField(blank=True, null=True)
    day28 = models.IntegerField(blank=True, null=True)
    day29 = models.IntegerField(blank=True, null=True)
    day30 = models.IntegerField(blank=True, null=True)
    day31 = models.IntegerField(blank=True, null=True)
    totaly = models.SmallIntegerField(blank=True, null=True)
    totalx = models.SmallIntegerField(blank=True, null=True)
    totalw = models.SmallIntegerField(blank=True, null=True)
    explain = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_dailyfx'


class XinhuDemo(models.Model):
    sheng = models.CharField(max_length=50, blank=True, null=True)
    shi = models.CharField(max_length=50, blank=True, null=True)
    xian = models.CharField(max_length=50, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    tanxuan = models.CharField(max_length=50, blank=True, null=True)
    tanxuancheck = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_demo'


class XinhuDept(models.Model):
    num = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    headman = models.CharField(max_length=50, blank=True, null=True)
    headid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_dept'


class XinhuDownload(models.Model):

    class Meta:
        managed = False
        db_table = 'xinhu_download'


class XinhuDuty(models.Model):
    user = models.CharField(max_length=10, blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_duty'


class XinhuEditrecord(models.Model):
    fieldsname = models.CharField(max_length=50, blank=True, null=True)
    oldval = models.CharField(max_length=1000, blank=True, null=True)
    newval = models.CharField(max_length=1000, blank=True, null=True)
    table = models.CharField(max_length=30, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    editci = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_editrecord'


class XinhuEmailCont(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    receid = models.CharField(max_length=500, blank=True, null=True)
    recename = models.CharField(max_length=500, blank=True, null=True)
    receemail = models.CharField(max_length=500, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    senddt = models.DateTimeField(blank=True, null=True)
    ccname = models.CharField(max_length=500, blank=True, null=True)
    ccemail = models.CharField(max_length=500, blank=True, null=True)
    attachpath = models.CharField(max_length=500, blank=True, null=True)
    attachname = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_email_cont'


class XinhuEmailm(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=220, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    sendid = models.SmallIntegerField(blank=True, null=True)
    sendname = models.CharField(max_length=100, blank=True, null=True)
    senddt = models.DateTimeField(blank=True, null=True)
    receid = models.CharField(max_length=2000, blank=True, null=True)
    recename = models.CharField(max_length=4000, blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    hid = models.SmallIntegerField(blank=True, null=True)
    isfile = models.IntegerField(blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    message_id = models.CharField(max_length=100, blank=True, null=True)
    fromemail = models.CharField(max_length=500, blank=True, null=True)
    toemail = models.CharField(max_length=500, blank=True, null=True)
    reply_toemail = models.CharField(max_length=500, blank=True, null=True)
    ccemail = models.CharField(max_length=500, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    ccname = models.CharField(max_length=100, blank=True, null=True)
    ccid = models.CharField(max_length=100, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    numoi = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_emailm'


class XinhuEmails(models.Model):
    mid = models.IntegerField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    zt = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    ishui = models.IntegerField(blank=True, null=True)
    isdel = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    personal = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_emails'


class XinhuFile(models.Model):
    valid = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=200, blank=True, null=True)
    filetype = models.CharField(max_length=50, blank=True, null=True)
    fileext = models.CharField(max_length=20, blank=True, null=True)
    filesize = models.IntegerField(blank=True, null=True)
    filesizecn = models.CharField(max_length=30, blank=True, null=True)
    filepath = models.CharField(max_length=100, blank=True, null=True)
    thumbpath = models.CharField(max_length=100, blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=50, blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=30, blank=True, null=True)
    web = models.CharField(max_length=300, blank=True, null=True)
    mtype = models.CharField(max_length=50, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    downci = models.IntegerField(blank=True, null=True)
    keyoi = models.CharField(max_length=20, blank=True, null=True)
    pdfpath = models.CharField(max_length=100, blank=True, null=True)
    oid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_file'


class XinhuFininfom(models.Model):
    type = models.CharField(max_length=10, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    moneycn = models.CharField(max_length=100, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    bills = models.SmallIntegerField(blank=True, null=True)
    paytype = models.CharField(max_length=20, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    cardid = models.CharField(max_length=50, blank=True, null=True)
    openbank = models.CharField(max_length=50, blank=True, null=True)
    purpose = models.CharField(max_length=100, blank=True, null=True)
    purresult = models.CharField(max_length=100, blank=True, null=True)
    paydt = models.DateField(blank=True, null=True)
    num = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    shibieid = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    invoice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    oncredit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supplier = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    goodstype = models.CharField(max_length=50, blank=True, null=True)
    applyname = models.CharField(max_length=50, blank=True, null=True)
    applydept = models.CharField(max_length=50, blank=True, null=True)
    bonus = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    commission = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    basesalary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    istofinance = models.IntegerField(blank=True, null=True)
    dsinvoice = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    perinvoice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reincoice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    returnmoney = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paytype2 = models.CharField(max_length=10, blank=True, null=True)
    readypay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nopay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tempsalary = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mid = models.SmallIntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    smalltype = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=2, blank=True, null=True)
    tempdate = models.DateField(blank=True, null=True)
    htid = models.IntegerField(blank=True, null=True)
    preinvoice = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    areadinvoice = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    istocontract = models.IntegerField(blank=True, null=True)
    extrafee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_fininfom'


class XinhuFininfomlog(models.Model):
    type = models.CharField(max_length=20, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    explain = models.TextField(blank=True, null=True)
    paytype = models.CharField(max_length=20, blank=True, null=True)
    code = models.CharField(max_length=255)
    mid = models.IntegerField(blank=True, null=True)
    optdate = models.DateField(blank=True, null=True)
    operate = models.CharField(max_length=30, blank=True, null=True)
    happenddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_fininfomlog'


class XinhuFininfos(models.Model):
    mid = models.SmallIntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    sdt = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sm = models.CharField(max_length=100, blank=True, null=True)
    didian = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_fininfos'


class XinhuFlowBill(models.Model):
    sericnum = models.CharField(max_length=50, blank=True, null=True)
    table = models.CharField(max_length=50, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    modeid = models.SmallIntegerField(blank=True, null=True)
    modename = models.CharField(max_length=20, blank=True, null=True)
    uname = models.CharField(max_length=20, blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    udeptname = models.CharField(max_length=30, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    allcheckid = models.CharField(max_length=500, blank=True, null=True)
    isdel = models.IntegerField(blank=True, null=True)
    nstatus = models.IntegerField(blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    nstatustext = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    nowcourseid = models.SmallIntegerField(blank=True, null=True)
    nowcheckid = models.CharField(max_length=500, blank=True, null=True)
    nowcheckname = models.CharField(max_length=500, blank=True, null=True)
    checksm = models.CharField(max_length=200, blank=True, null=True)
    updt = models.DateTimeField(blank=True, null=True)
    createdt = models.DateTimeField(blank=True, null=True)
    tuiid = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_bill'


class XinhuFlowChecks(models.Model):
    table = models.CharField(max_length=30, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    modeid = models.SmallIntegerField(blank=True, null=True)
    courseid = models.SmallIntegerField(blank=True, null=True)
    checkid = models.CharField(max_length=100, blank=True, null=True)
    checkname = models.CharField(max_length=100, blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    addlx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_checks'


class XinhuFlowCname(models.Model):
    num = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    checkid = models.CharField(max_length=50, blank=True, null=True)
    checkname = models.CharField(max_length=50, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    receid = models.CharField(max_length=300, blank=True, null=True)
    recename = models.CharField(max_length=500, blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_cname'


class XinhuFlowCourse(models.Model):
    mid = models.IntegerField(blank=True, null=True)
    nid = models.IntegerField(blank=True, null=True)
    setid = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    checktype = models.CharField(max_length=20, blank=True, null=True)
    checktypeid = models.CharField(max_length=200, blank=True, null=True)
    checktypename = models.CharField(max_length=200, blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    whereid = models.SmallIntegerField(blank=True, null=True)
    where = models.CharField(max_length=500, blank=True, null=True)
    explain = models.CharField(max_length=100, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    courseact = models.CharField(max_length=50, blank=True, null=True)
    checkshu = models.IntegerField(blank=True, null=True)
    checkfields = models.CharField(max_length=500, blank=True, null=True)
    pid = models.SmallIntegerField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    receid = models.CharField(max_length=200, blank=True, null=True)
    recename = models.CharField(max_length=200, blank=True, null=True)
    iszf = models.IntegerField(blank=True, null=True)
    isqm = models.IntegerField(blank=True, null=True)
    coursetype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_course'


class XinhuFlowElement(models.Model):
    mid = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    fields = models.CharField(max_length=50, blank=True, null=True)
    fieldstype = models.CharField(max_length=30, blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    dev = models.CharField(max_length=20, blank=True, null=True)
    isbt = models.IntegerField(blank=True, null=True)
    data = models.CharField(max_length=500, blank=True, null=True)
    islu = models.IntegerField(blank=True, null=True)
    iszs = models.IntegerField(blank=True, null=True)
    attr = models.CharField(max_length=500, blank=True, null=True)
    iszb = models.IntegerField(blank=True, null=True)
    isss = models.IntegerField(blank=True, null=True)
    lattr = models.CharField(max_length=100, blank=True, null=True)
    width = models.CharField(max_length=10, blank=True, null=True)
    lens = models.SmallIntegerField(blank=True, null=True)
    savewhere = models.CharField(max_length=100, blank=True, null=True)
    islb = models.IntegerField(blank=True, null=True)
    ispx = models.IntegerField(blank=True, null=True)
    isalign = models.IntegerField(blank=True, null=True)
    issou = models.IntegerField(blank=True, null=True)
    istj = models.IntegerField(blank=True, null=True)
    gongsi = models.CharField(max_length=500, blank=True, null=True)
    placeholder = models.CharField(max_length=50, blank=True, null=True)
    isonly = models.IntegerField(blank=True, null=True)
    isdr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_element'


class XinhuFlowExtent(models.Model):
    recename = models.CharField(max_length=200, blank=True, null=True)
    receid = models.CharField(max_length=200, blank=True, null=True)
    modeid = models.SmallIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    wherestr = models.CharField(max_length=500, blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField()
    whereid = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_extent'


class XinhuFlowLog(models.Model):
    table = models.CharField(max_length=50, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    statusname = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    courseid = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    ip = models.CharField(max_length=30, blank=True, null=True)
    web = models.CharField(max_length=50, blank=True, null=True)
    checkname = models.CharField(max_length=20, blank=True, null=True)
    checkid = models.SmallIntegerField(blank=True, null=True)
    modeid = models.SmallIntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    step = models.SmallIntegerField(blank=True, null=True)
    qmimg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_log'


class XinhuFlowMenu(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    statusname = models.CharField(max_length=20, blank=True, null=True)
    statuscolor = models.CharField(max_length=20, blank=True, null=True)
    statusvalue = models.IntegerField(blank=True, null=True)
    actname = models.CharField(max_length=20, blank=True, null=True)
    setid = models.SmallIntegerField(blank=True, null=True)
    wherestr = models.CharField(max_length=300, blank=True, null=True)
    explain = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    islog = models.IntegerField(blank=True, null=True)
    issm = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    changeaction = models.CharField(max_length=20, blank=True, null=True)
    fields = models.CharField(max_length=50, blank=True, null=True)
    upgcont = models.CharField(max_length=500, blank=True, null=True)
    iszs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_menu'


class XinhuFlowRemind(models.Model):
    startdt = models.DateTimeField(blank=True, null=True)
    enddt = models.DateTimeField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    modenum = models.CharField(max_length=30, blank=True, null=True)
    table = models.CharField(max_length=30, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    ratecont = models.CharField(max_length=500, blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    rate = models.CharField(max_length=50, blank=True, null=True)
    rateval = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    receid = models.CharField(max_length=100, blank=True, null=True)
    recename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_remind'
        unique_together = (('uid', 'table', 'mid'), ('uid', 'modenum', 'mid'),)


class XinhuFlowSet(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    num = models.CharField(max_length=30)
    sort = models.SmallIntegerField(blank=True, null=True)
    table = models.CharField(max_length=50, blank=True, null=True)
    where = models.CharField(max_length=500, blank=True, null=True)
    summary = models.CharField(max_length=500, blank=True, null=True)
    summarx = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    pctx = models.IntegerField(blank=True, null=True)
    mctx = models.IntegerField(blank=True, null=True)
    wxtx = models.IntegerField(blank=True, null=True)
    emtx = models.IntegerField(blank=True, null=True)
    sericnum = models.CharField(max_length=50, blank=True, null=True)
    isflow = models.IntegerField(blank=True, null=True)
    receid = models.CharField(max_length=255, blank=True, null=True)
    recename = models.CharField(max_length=255, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    islu = models.IntegerField(blank=True, null=True)
    tables = models.CharField(max_length=100, blank=True, null=True)
    names = models.CharField(max_length=100, blank=True, null=True)
    statusstr = models.CharField(max_length=100, blank=True, null=True)
    isgbjl = models.IntegerField(blank=True, null=True)
    isgbcy = models.IntegerField(blank=True, null=True)
    isscl = models.IntegerField(blank=True, null=True)
    isup = models.IntegerField(blank=True, null=True)
    ddtx = models.IntegerField(blank=True, null=True)
    isbxs = models.IntegerField(blank=True, null=True)
    lbztxs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_set'
        unique_together = (('id', 'num'),)


class XinhuFlowTodo(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    num = models.CharField(max_length=30, blank=True, null=True)
    setid = models.SmallIntegerField(blank=True, null=True)
    explain = models.CharField(max_length=100, blank=True, null=True)
    whereid = models.SmallIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    receid = models.CharField(max_length=500, blank=True, null=True)
    recename = models.CharField(max_length=500, blank=True, null=True)
    changefields = models.CharField(max_length=200, blank=True, null=True)
    changecourse = models.CharField(max_length=30, blank=True, null=True)
    boturn = models.IntegerField(blank=True, null=True)
    boedit = models.IntegerField(blank=True, null=True)
    bochang = models.IntegerField(blank=True, null=True)
    bodel = models.IntegerField(blank=True, null=True)
    bozuofei = models.IntegerField(blank=True, null=True)
    botong = models.IntegerField(blank=True, null=True)
    bobutong = models.IntegerField(blank=True, null=True)
    bofinish = models.IntegerField(blank=True, null=True)
    bozhui = models.IntegerField(blank=True, null=True)
    bozhuan = models.IntegerField(blank=True, null=True)
    toturn = models.IntegerField(blank=True, null=True)
    tocourse = models.IntegerField(blank=True, null=True)
    todofields = models.CharField(max_length=100, blank=True, null=True)
    summary = models.CharField(max_length=100, blank=True, null=True)
    botask = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_todo'


class XinhuFlowTodos(models.Model):
    modenum = models.CharField(max_length=30, blank=True, null=True)
    modename = models.CharField(max_length=30, blank=True, null=True)
    table = models.CharField(max_length=30, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    readdt = models.DateTimeField(blank=True, null=True)
    isread = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_todos'


class XinhuFlowWhere(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    setid = models.SmallIntegerField(blank=True, null=True)
    num = models.CharField(max_length=30, blank=True, null=True)
    pnum = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    wheresstr = models.CharField(max_length=500, blank=True, null=True)
    whereustr = models.CharField(max_length=500, blank=True, null=True)
    wheredstr = models.CharField(max_length=500, blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    explain = models.CharField(max_length=200, blank=True, null=True)
    receid = models.CharField(max_length=200, blank=True, null=True)
    recename = models.CharField(max_length=200, blank=True, null=True)
    nreceid = models.CharField(max_length=200, blank=True, null=True)
    nrecename = models.CharField(max_length=200, blank=True, null=True)
    islb = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    syrid = models.CharField(max_length=200, blank=True, null=True)
    syrname = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_flow_where'


class XinhuGoodm(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    custid = models.SmallIntegerField(blank=True, null=True)
    custname = models.CharField(max_length=50, blank=True, null=True)
    discount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_goodm'


class XinhuGoods(models.Model):
    typeid = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    guige = models.CharField(max_length=50, blank=True, null=True)
    xinghao = models.CharField(max_length=50, blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    stockcs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_goods'


class XinhuGoodss(models.Model):
    aid = models.SmallIntegerField(blank=True, null=True)
    count = models.SmallIntegerField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    kind = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    mid = models.SmallIntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_goodss'


class XinhuGroup(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    ispir = models.IntegerField(blank=True, null=True)
    indate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_group'


class XinhuHomeitems(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    num = models.CharField(max_length=30)
    receid = models.CharField(max_length=300, blank=True, null=True)
    recename = models.CharField(max_length=500, blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    row = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_homeitems'
        unique_together = (('id', 'num'),)


class XinhuHrcheck(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=20, blank=True, null=True)
    month = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=2000, blank=True, null=True)
    fenzp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fensj = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fenrs = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fen = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_hrcheck'


class XinhuHrpositive(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    ranking = models.CharField(max_length=30, blank=True, null=True)
    entrydt = models.DateField(blank=True, null=True)
    syenddt = models.DateField(blank=True, null=True)
    positivedt = models.DateField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    isover = models.IntegerField(blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_hrpositive'


class XinhuHrredund(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    ranking = models.CharField(max_length=30, blank=True, null=True)
    entrydt = models.DateField(blank=True, null=True)
    quitdt = models.DateField(blank=True, null=True)
    redundtype = models.CharField(max_length=20, blank=True, null=True)
    redundreson = models.CharField(max_length=100, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    isover = models.IntegerField(blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_hrredund'


class XinhuHrsalary(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    xuid = models.SmallIntegerField(blank=True, null=True)
    uname = models.CharField(max_length=20, blank=True, null=True)
    udeptname = models.CharField(max_length=20, blank=True, null=True)
    ranking = models.CharField(max_length=20, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=10)
    base = models.DecimalField(max_digits=10, decimal_places=2)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    postjt = models.DecimalField(max_digits=10, decimal_places=2)
    skilljt = models.DecimalField(max_digits=10, decimal_places=2)
    travelbt = models.DecimalField(max_digits=10, decimal_places=2)
    telbt = models.DecimalField(max_digits=10, decimal_places=2)
    reward = models.DecimalField(max_digits=10, decimal_places=2)
    punish = models.DecimalField(max_digits=10, decimal_places=2)
    socials = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=10, decimal_places=2)
    ispay = models.IntegerField()
    otherzj = models.DecimalField(max_digits=10, decimal_places=2)
    otherjs = models.DecimalField(max_digits=10, decimal_places=2)
    cidao = models.SmallIntegerField()
    cidaos = models.DecimalField(max_digits=10, decimal_places=2)
    zaotui = models.SmallIntegerField()
    zaotuis = models.DecimalField(max_digits=10, decimal_places=2)
    leave = models.SmallIntegerField()
    leaves = models.DecimalField(max_digits=10, decimal_places=2)
    jiaban = models.SmallIntegerField()
    jiabans = models.DecimalField(max_digits=10, decimal_places=2)
    weidk = models.SmallIntegerField()
    weidks = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'xinhu_hrsalary'


class XinhuHrtransfer(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    tranuid = models.SmallIntegerField(blank=True, null=True)
    tranname = models.CharField(max_length=20, blank=True, null=True)
    trantype = models.CharField(max_length=20, blank=True, null=True)
    olddeptname = models.CharField(max_length=50, blank=True, null=True)
    oldranking = models.CharField(max_length=20, blank=True, null=True)
    effectivedt = models.DateField(blank=True, null=True)
    newdeptname = models.CharField(max_length=50, blank=True, null=True)
    newdeptid = models.SmallIntegerField(blank=True, null=True)
    newranking = models.CharField(max_length=20, blank=True, null=True)
    isover = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_hrtransfer'


class XinhuHrtrsalary(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    effectivedt = models.DateField(blank=True, null=True)
    floats = models.SmallIntegerField(blank=True, null=True)
    ranking = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_hrtrsalary'


class XinhuImGroup(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    pid = models.SmallIntegerField(blank=True, null=True)
    types = models.CharField(max_length=10, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    creatid = models.IntegerField(blank=True, null=True)
    createname = models.CharField(max_length=20, blank=True, null=True)
    createdt = models.DateTimeField(blank=True, null=True)
    face = models.CharField(max_length=50, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    receid = models.CharField(max_length=200, blank=True, null=True)
    recename = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    explain = models.CharField(max_length=200, blank=True, null=True)
    iconfont = models.CharField(max_length=30, blank=True, null=True)
    iconcolor = models.CharField(max_length=7, blank=True, null=True)
    yylx = models.IntegerField(blank=True, null=True)
    urlpc = models.CharField(max_length=200, blank=True, null=True)
    urlm = models.CharField(max_length=200, blank=True, null=True)
    deptid = models.CharField(max_length=100, blank=True, null=True)
    createid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_im_group'


class XinhuImGroupuser(models.Model):
    gid = models.SmallIntegerField()
    uid = models.SmallIntegerField()
    istx = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xinhu_im_groupuser'


class XinhuImHistory(models.Model):
    type = models.CharField(max_length=10, blank=True, null=True)
    receid = models.SmallIntegerField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    sendid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    cont = models.CharField(max_length=200, blank=True, null=True)
    stotal = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_im_history'
        unique_together = (('type', 'receid', 'uid'),)


class XinhuImMenu(models.Model):
    mid = models.SmallIntegerField()
    pid = models.SmallIntegerField()
    name = models.CharField(max_length=10, blank=True, null=True)
    sort = models.SmallIntegerField()
    type = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_im_menu'


class XinhuImMess(models.Model):
    optdt = models.DateTimeField(blank=True, null=True)
    zt = models.IntegerField(blank=True, null=True)
    cont = models.CharField(max_length=4000, blank=True, null=True)
    sendid = models.SmallIntegerField(blank=True, null=True)
    receid = models.SmallIntegerField(blank=True, null=True)
    receuid = models.CharField(max_length=4000, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    fileid = models.IntegerField()
    msgid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_im_mess'


class XinhuImMesszt(models.Model):
    mid = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    gid = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_im_messzt'


class XinhuInfor(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    typename = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    receid = models.CharField(max_length=2000, blank=True, null=True)
    recename = models.CharField(max_length=4000, blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    enddt = models.DateTimeField(blank=True, null=True)
    startdt = models.DateTimeField(blank=True, null=True)
    zuozhe = models.CharField(max_length=30, blank=True, null=True)
    indate = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    fengmian = models.CharField(max_length=100, blank=True, null=True)
    mintou = models.SmallIntegerField(blank=True, null=True)
    maxtou = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_infor'


class XinhuInfors(models.Model):
    mid = models.SmallIntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    touitems = models.CharField(max_length=200, blank=True, null=True)
    touci = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_infors'


class XinhuInvoicein(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_invoicein'


class XinhuKeywords(models.Model):
    keywords = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    createdt = models.DateField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    hotlevel = models.IntegerField(blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_keywords'


class XinhuKnowledge(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    typeid = models.SmallIntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    istrash = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_knowledge'


class XinhuKnowtiku(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    typeid = models.SmallIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    ana = models.CharField(max_length=300, blank=True, null=True)
    anb = models.CharField(max_length=300, blank=True, null=True)
    anc = models.CharField(max_length=300, blank=True, null=True)
    and_field = models.CharField(db_column='and', max_length=300, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    answer = models.CharField(max_length=10, blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_knowtiku'


class XinhuKnowtraim(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    dxshu = models.SmallIntegerField(blank=True, null=True)
    dsshu = models.SmallIntegerField(blank=True, null=True)
    reshu = models.SmallIntegerField(blank=True, null=True)
    startdt = models.DateTimeField(blank=True, null=True)
    enddt = models.DateTimeField(blank=True, null=True)
    kstime = models.SmallIntegerField(blank=True, null=True)
    ydshu = models.SmallIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    receid = models.CharField(max_length=200, blank=True, null=True)
    recename = models.CharField(max_length=200, blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    zfenshu = models.IntegerField(blank=True, null=True)
    hgfen = models.IntegerField(blank=True, null=True)
    tikuid = models.CharField(max_length=200, blank=True, null=True)
    tikuname = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_knowtraim'


class XinhuKnowtrais(models.Model):
    mid = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    kssdt = models.DateTimeField(blank=True, null=True)
    ksedt = models.DateTimeField(blank=True, null=True)
    fenshu = models.SmallIntegerField(blank=True, null=True)
    kstime = models.IntegerField(blank=True, null=True)
    isks = models.IntegerField(blank=True, null=True)
    tkids = models.CharField(max_length=2000, blank=True, null=True)
    dyids = models.CharField(max_length=1000, blank=True, null=True)
    dyjgs = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_knowtrais'
        unique_together = (('mid', 'uid'),)


class XinhuKpi(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    kpi = models.CharField(max_length=255, blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    profitcommission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    kpiratio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ratio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kpi'


class XinhuKqanay(models.Model):
    dt = models.DateField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    ztname = models.CharField(max_length=20, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    states = models.CharField(max_length=20, blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    iswork = models.IntegerField(blank=True, null=True)
    emiao = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqanay'


class XinhuKqdist(models.Model):
    recename = models.CharField(max_length=200, blank=True, null=True)
    receid = models.CharField(max_length=20, blank=True, null=True)
    mid = models.SmallIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    startdt = models.DateField(blank=True, null=True)
    enddt = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqdist'


class XinhuKqdisv(models.Model):
    plx = models.IntegerField(blank=True, null=True)
    receid = models.IntegerField(blank=True, null=True)
    dt = models.DateField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqdisv'


class XinhuKqdkjl(models.Model):
    uid = models.IntegerField()
    dkdt = models.DateTimeField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    lat = models.CharField(max_length=20, blank=True, null=True)
    lng = models.CharField(max_length=20, blank=True, null=True)
    accuracy = models.SmallIntegerField(blank=True, null=True)
    ip = models.CharField(max_length=30, blank=True, null=True)
    mac = models.CharField(max_length=30, blank=True, null=True)
    explain = models.CharField(max_length=200, blank=True, null=True)
    imgpath = models.CharField(max_length=100, blank=True, null=True)
    snid = models.IntegerField(blank=True, null=True)
    sntype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqdkjl'


class XinhuKqdw(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    location_x = models.CharField(max_length=20, blank=True, null=True)
    location_y = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    precision = models.IntegerField(blank=True, null=True)
    scale = models.SmallIntegerField(blank=True, null=True)
    wifiname = models.CharField(max_length=100, blank=True, null=True)
    iswgd = models.IntegerField(blank=True, null=True)
    dwids = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqdw'


class XinhuKqerr(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    errtype = models.CharField(max_length=10, blank=True, null=True)
    dt = models.DateField(blank=True, null=True)
    ytime = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqerr'


class XinhuKqinfo(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    uname = models.CharField(max_length=20, blank=True, null=True)
    stime = models.DateTimeField(blank=True, null=True)
    etime = models.DateTimeField(blank=True, null=True)
    kind = models.CharField(max_length=10, blank=True, null=True)
    qjkind = models.CharField(max_length=20, blank=True, null=True)
    explain = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    totals = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    jiafee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    jiatype = models.IntegerField(blank=True, null=True)
    totday = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqinfo'


class XinhuKqjcmd(models.Model):
    id = models.IntegerField(primary_key=True)
    snid = models.IntegerField(blank=True, null=True)
    cmd = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    qjtime = models.DateTimeField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    cjtime = models.DateTimeField(blank=True, null=True)
    atype = models.CharField(max_length=30, blank=True, null=True)
    others = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqjcmd'


class XinhuKqjsn(models.Model):
    num = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    deptids = models.CharField(max_length=4000, blank=True, null=True)
    userids = models.TextField(blank=True, null=True)
    lastdt = models.DateTimeField(blank=True, null=True)
    space = models.IntegerField(blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)
    usershu = models.IntegerField(blank=True, null=True)
    fingerprintshu = models.IntegerField(blank=True, null=True)
    headpicshu = models.IntegerField(blank=True, null=True)
    clockinshu = models.IntegerField(blank=True, null=True)
    picshu = models.IntegerField(blank=True, null=True)
    romver = models.CharField(max_length=30, blank=True, null=True)
    appver = models.CharField(max_length=30, blank=True, null=True)
    model = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqjsn'
        unique_together = (('id', 'num'),)


class XinhuKqjuser(models.Model):
    snid = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    fingerprint1 = models.TextField(blank=True, null=True)
    fingerprint2 = models.TextField(blank=True, null=True)
    headpic = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqjuser'
        unique_together = (('snid', 'uid'),)


class XinhuKqout(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    outtime = models.DateTimeField(blank=True, null=True)
    intime = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    atype = models.CharField(max_length=2, blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    isxj = models.IntegerField(blank=True, null=True)
    sicksm = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqout'


class XinhuKqsjgz(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    pid = models.SmallIntegerField(blank=True, null=True)
    stime = models.CharField(max_length=20, blank=True, null=True)
    etime = models.CharField(max_length=20, blank=True, null=True)
    qtype = models.IntegerField(blank=True, null=True)
    iskt = models.IntegerField(blank=True, null=True)
    iskq = models.IntegerField(blank=True, null=True)
    isxx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqsjgz'


class XinhuKqxxsj(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    dt = models.DateField(blank=True, null=True)
    pid = models.SmallIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_kqxxsj'


class XinhuLocation(models.Model):
    user = models.CharField(max_length=30, blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    agentid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    location_x = models.CharField(max_length=30, blank=True, null=True)
    location_y = models.CharField(max_length=30, blank=True, null=True)
    scale = models.SmallIntegerField(blank=True, null=True)
    label = models.CharField(max_length=50, blank=True, null=True)
    msgid = models.CharField(max_length=50, blank=True, null=True)
    precision = models.SmallIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    explain = models.CharField(max_length=50, blank=True, null=True)
    imgpath = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_location'


class XinhuLog(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=30, blank=True, null=True)
    web = models.CharField(max_length=100, blank=True, null=True)
    device = models.CharField(max_length=50, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_log'


class XinhuLogintoken(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    token = models.CharField(max_length=50, blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    moddt = models.DateTimeField(blank=True, null=True)
    cfrom = models.CharField(max_length=10, blank=True, null=True)
    device = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=30, blank=True, null=True)
    web = models.CharField(max_length=30, blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_logintoken'


class XinhuMeet(models.Model):
    hyname = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    startdt = models.CharField(max_length=50, blank=True, null=True)
    enddt = models.CharField(max_length=50, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    joinid = models.CharField(max_length=200, blank=True, null=True)
    joinname = models.CharField(max_length=500, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    rate = models.CharField(max_length=100, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    cancelreason = models.CharField(max_length=200, blank=True, null=True)
    jyid = models.CharField(max_length=100, blank=True, null=True)
    jyname = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_meet'


class XinhuMenu(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    pid = models.SmallIntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    icons = models.CharField(max_length=50, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    num = models.CharField(max_length=50, blank=True, null=True)
    ispir = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    ishs = models.IntegerField(blank=True, null=True)
    iszm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_menu'


class XinhuMyadddata(models.Model):
    type = models.CharField(max_length=255)
    impression = models.IntegerField()
    click = models.IntegerField()
    costrmb = models.FloatField()
    cpc = models.FloatField()
    time = models.DateField()
    adduser = models.CharField(max_length=255)
    custnum = models.IntegerField(blank=True, null=True)
    clickrate = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_myadddata'


class XinhuOfficial(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    titles = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=10, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    type = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    receid = models.CharField(max_length=200, blank=True, null=True)
    recename = models.CharField(max_length=200, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    num = models.CharField(max_length=30, blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    filecontid = models.CharField(max_length=30, blank=True, null=True)
    zinum = models.CharField(max_length=30, blank=True, null=True)
    unitname = models.CharField(max_length=50, blank=True, null=True)
    unitsame = models.CharField(max_length=50, blank=True, null=True)
    miji = models.CharField(max_length=50, blank=True, null=True)
    laidt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_official'


class XinhuOption(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    num = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=500, blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    values = models.CharField(max_length=50, blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    receid = models.CharField(max_length=300, blank=True, null=True)
    recename = models.CharField(max_length=300, blank=True, null=True)
    explain = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_option'


class XinhuProject(models.Model):
    pid = models.SmallIntegerField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    startdt = models.DateTimeField(blank=True, null=True)
    enddt = models.DateTimeField(blank=True, null=True)
    fuze = models.CharField(max_length=20, blank=True, null=True)
    fuzeid = models.CharField(max_length=50, blank=True, null=True)
    runuser = models.CharField(max_length=100, blank=True, null=True)
    runuserid = models.CharField(max_length=100, blank=True, null=True)
    progress = models.SmallIntegerField(blank=True, null=True)
    viewuser = models.CharField(max_length=100, blank=True, null=True)
    viewuserid = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_project'


class XinhuReads(models.Model):
    table = models.CharField(max_length=30, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=30, blank=True, null=True)
    web = models.CharField(max_length=30, blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    stotal = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_reads'
        unique_together = (('table', 'mid', 'optid'),)


class XinhuRecord(models.Model):
    district = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    record = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'xinhu_record'


class XinhuRepair(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    assetm = models.CharField(max_length=100, blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    reasons = models.CharField(max_length=500, blank=True, null=True)
    iswx = models.IntegerField(blank=True, null=True)
    money = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    wxname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_repair'


class XinhuReward(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    object = models.CharField(max_length=30, blank=True, null=True)
    objectid = models.SmallIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=50, blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    happendt = models.DateTimeField(blank=True, null=True)
    hapaddress = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_reward'


class XinhuSchedule(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    startdt = models.DateTimeField(blank=True, null=True)
    enddt = models.DateTimeField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    ratecont = models.CharField(max_length=500, blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    rate = models.CharField(max_length=5, blank=True, null=True)
    rateval = models.CharField(max_length=50, blank=True, null=True)
    txsj = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    receid = models.CharField(max_length=100, blank=True, null=True)
    recename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_schedule'


class XinhuSeal(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    bgname = models.CharField(max_length=50, blank=True, null=True)
    bgid = models.CharField(max_length=50, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    sealimg = models.CharField(max_length=100, blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_seal'


class XinhuSealapl(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    sealid = models.SmallIntegerField(blank=True, null=True)
    sealname = models.CharField(max_length=50, blank=True, null=True)
    isout = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_sealapl'


class XinhuSjoin(models.Model):
    type = models.CharField(max_length=10, blank=True, null=True)
    mid = models.IntegerField(blank=True, null=True)
    sid = models.IntegerField(blank=True, null=True)
    indate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_sjoin'


class XinhuSqllog(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    optdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_sqllog'


class XinhuSubscribe(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    cont = models.CharField(max_length=200, blank=True, null=True)
    explain = models.CharField(max_length=100, blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    suburl = models.CharField(max_length=1000, blank=True, null=True)
    suburlpost = models.CharField(max_length=4000, blank=True, null=True)
    lastdt = models.DateTimeField(blank=True, null=True)
    shateid = models.CharField(max_length=300, blank=True, null=True)
    shatename = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_subscribe'


class XinhuSubscribeinfo(models.Model):
    mid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    cont = models.CharField(max_length=200, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    filepath = models.CharField(max_length=200, blank=True, null=True)
    receid = models.CharField(max_length=4000, blank=True, null=True)
    recename = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_subscribeinfo'


class XinhuSupplier(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    explain = models.TextField(blank=True, null=True)
    tel = models.CharField(max_length=15, blank=True, null=True)
    isok = models.IntegerField(blank=True, null=True)
    totalvalue = models.FloatField(blank=True, null=True)
    oncredit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_supplier'


class XinhuTask(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    fenlei = models.CharField(max_length=10, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    time = models.CharField(max_length=200, blank=True, null=True)
    ratecont = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    lastdt = models.DateTimeField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    startdt = models.DateTimeField(blank=True, null=True)
    lastcont = models.CharField(max_length=500, blank=True, null=True)
    explain = models.CharField(max_length=200, blank=True, null=True)
    todoid = models.CharField(max_length=200, blank=True, null=True)
    todoname = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_task'


class XinhuTodo(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    mess = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    table = models.CharField(max_length=50, blank=True, null=True)
    mid = models.SmallIntegerField(blank=True, null=True)
    readdt = models.DateTimeField(blank=True, null=True)
    tododt = models.DateTimeField(blank=True, null=True)
    modenum = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_todo'


class XinhuTovoid(models.Model):
    uid = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    modename = models.CharField(max_length=20, blank=True, null=True)
    modeid = models.SmallIntegerField(blank=True, null=True)
    tonum = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_tovoid'


class XinhuUserinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    num = models.CharField(max_length=20, blank=True, null=True)
    deptname = models.CharField(max_length=30, blank=True, null=True)
    deptnames = models.CharField(max_length=100, blank=True, null=True)
    ranking = models.CharField(max_length=20, blank=True, null=True)
    rankings = models.CharField(max_length=100, blank=True, null=True)
    dkip = models.CharField(max_length=30, blank=True, null=True)
    dkmac = models.CharField(max_length=30, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    workdate = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    quitdt = models.DateField(blank=True, null=True)
    iskq = models.IntegerField(blank=True, null=True)
    isdwdk = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    xueli = models.CharField(max_length=20, blank=True, null=True)
    birtype = models.IntegerField(blank=True, null=True)
    minzu = models.CharField(max_length=20, blank=True, null=True)
    hunyin = models.CharField(max_length=10, blank=True, null=True)
    jiguan = models.CharField(max_length=20, blank=True, null=True)
    nowdizhi = models.CharField(max_length=50, blank=True, null=True)
    housedizhi = models.CharField(max_length=50, blank=True, null=True)
    syenddt = models.DateField(blank=True, null=True)
    positivedt = models.DateField(blank=True, null=True)
    bankname = models.CharField(max_length=50, blank=True, null=True)
    banknum = models.CharField(max_length=30, blank=True, null=True)
    zhaopian = models.CharField(max_length=100, blank=True, null=True)
    idnum = models.CharField(max_length=30, blank=True, null=True)
    spareman = models.CharField(max_length=30, blank=True, null=True)
    sparetel = models.CharField(max_length=50, blank=True, null=True)
    isdaily = models.IntegerField(blank=True, null=True)
    companyid = models.IntegerField(blank=True, null=True)
    duty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xinhu_userinfo'


class XinhuUserinfos(models.Model):
    mid = models.SmallIntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    startdt = models.DateField(blank=True, null=True)
    enddt = models.DateField(blank=True, null=True)
    rank = models.CharField(max_length=50, blank=True, null=True)
    unitname = models.CharField(max_length=50, blank=True, null=True)
    sslx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_userinfos'


class XinhuUserract(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    startdt = models.DateField(blank=True, null=True)
    enddt = models.DateField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    explain = models.CharField(max_length=500, blank=True, null=True)
    httype = models.CharField(max_length=30, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    tqenddt = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    uname = models.CharField(max_length=20, blank=True, null=True)
    companyid = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_userract'


class XinhuVcard(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    gname = models.CharField(max_length=20, blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    unitname = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_vcard'


class XinhuWord(models.Model):
    optid = models.SmallIntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    fileid = models.IntegerField(blank=True, null=True)
    shateid = models.CharField(max_length=200, blank=True, null=True)
    shate = models.CharField(max_length=200, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    typeid = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_word'


class XinhuWork(models.Model):
    num = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    distid = models.CharField(max_length=50, blank=True, null=True)
    dist = models.CharField(max_length=50, blank=True, null=True)
    explain = models.CharField(max_length=4000, blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    optid = models.IntegerField(blank=True, null=True)
    optname = models.CharField(max_length=20, blank=True, null=True)
    startdt = models.DateTimeField(blank=True, null=True)
    enddt = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    txdt = models.DateTimeField(blank=True, null=True)
    fen = models.SmallIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    projectid = models.SmallIntegerField(blank=True, null=True)
    ddid = models.CharField(max_length=50, blank=True, null=True)
    ddname = models.CharField(max_length=50, blank=True, null=True)
    score = models.SmallIntegerField(blank=True, null=True)
    mark = models.SmallIntegerField(blank=True, null=True)
    uid = models.SmallIntegerField(blank=True, null=True)
    applydt = models.DateField(blank=True, null=True)
    isturn = models.IntegerField(blank=True, null=True)
    process = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_work'


class XinhuWouser(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    openid = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    headimgurl = models.CharField(max_length=300, blank=True, null=True)
    adddt = models.DateTimeField(blank=True, null=True)
    optdt = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinhu_wouser'
