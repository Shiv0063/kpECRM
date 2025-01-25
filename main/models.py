from django.db import models

# Create your models here.

class GSTModel(models.Model):
    GSTName = models.CharField(max_length=100)
    SGST = models.IntegerField(default=0)
    CGST = models.IntegerField(default=0)


class CostCodeModel(models.Model):
    CostCode = models.IntegerField(default=0)
    Name = models.CharField(max_length=100)
    Remarks = models.TextField()
    
class PartyNameModel(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)

class LabourModel(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.TextField() 
    Mobile1 = models.CharField(max_length=100)
    Mobile2 = models.CharField(max_length=100)
    Remarks = models.TextField()

class ClusterModel(models.Model):
    Name = models.CharField(max_length=100)
    Amount = models.IntegerField(default=0)
    ATM = models.CharField(max_length=100,default='False')
    Branch = models.CharField(max_length=100,default='False')
    HubLocation = models.CharField(max_length=100,default='False')
    Type = models.CharField(max_length=100,null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.ATM == 'True':
            self.Type = "ATM"
        elif self.Branch == 'True':
            self.Type = "Branch"
        else:
            self.Type = "HubLocation"
        super(ClusterModel, self).save(*args, **kwargs)

class PartyModel(models.Model):
    Code = models.CharField(max_length=100, null=True, blank=True)
    PartyName = models.CharField(max_length=100)
    Cluster = models.CharField(max_length=100)
    Active = models.CharField(max_length=100,null=True, blank=True)
    City = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)
    Address = models.TextField() 
    GSTNo = models.CharField(max_length=100)
    NO1 = models.CharField(max_length=100, null=True, blank=True)
    NO2 = models.CharField(max_length=100, null=True, blank=True)
    NO3 = models.CharField(max_length=100, null=True, blank=True)
    NO4 = models.CharField(max_length=100, null=True, blank=True)
    NO5 = models.CharField(max_length=100, null=True, blank=True)
    NO6 = models.CharField(max_length=100, null=True, blank=True)

class RateModel(models.Model):
    Type = models.CharField(max_length=100,null=True, blank=True)
    CodeNo = models.CharField(max_length=100)
    Description = models.TextField() 
    HSNCode = models.IntegerField(default=0)
    Unit = models.CharField(max_length=100)
    Rate = models.CharField(max_length=100,null=True, blank=True)
    Remarks = models.TextField() 
    GSTName = models.CharField(max_length=100)
    SGST = models.IntegerField(default=0)
    CGST = models.IntegerField(default=0)
    IGSTName = models.CharField(max_length=100,null=True, blank=True)
    IGST = models.IntegerField(default=0)

class CountModel(models.Model):
    Counter = models.IntegerField(default=0)
    idf = models.CharField(max_length=100,null=True, blank=True)

class RCModel(models.Model):
    Counter = models.IntegerField(default=0,null=True, blank=True)
    RCCode = models.CharField(max_length=100,null=True, blank=True)
    RCDescription = models.TextField(null=True, blank=True)
    HSNCode = models.IntegerField(default=0,null=True, blank=True)
    Unit = models.CharField(max_length=100,null=True, blank=True)
    Quantity = models.CharField(max_length=100,null=True, blank=True)
    Rate = models.CharField(max_length=100,default='0',null=True, blank=True)
    Labour = models.CharField(max_length=100,default='0',null=True, blank=True)
    Amount = models.CharField(max_length=100,default='0',null=True, blank=True)

class EntryModel(models.Model):
    Counter = models.IntegerField(default=0)
    PartyName = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)
    Code = models.CharField(max_length=100)
    Cluster = models.CharField(max_length=100)
    Cluster_id = models.CharField(max_length=100, null=True, blank=True)
    Address = models.TextField() 
    NO1 = models.CharField(max_length=100, null=True, blank=True)
    NO2 = models.CharField(max_length=100, null=True, blank=True)
    NO3 = models.CharField(max_length=100, null=True, blank=True)
    NO4 = models.CharField(max_length=100, null=True, blank=True)
    CallType = models.CharField(max_length=100)
    Date = models.DateField()
    CallDate = models.DateField(null=True, blank=True)
    CloseDate = models.DateField()
    CodeNo = models.CharField(max_length=100)
    CostCode = models.CharField(max_length=100)
    ContactNo = models.CharField(max_length=100,null=True, blank=True)
    ContactPerson = models.CharField(max_length=100,null=True, blank=True)
    Email = models.CharField(max_length=100,null=True, blank=True)
    CCName = models.CharField(max_length=100,null=True, blank=True)
    Problem = models.TextField() 
    ChallanNo = models.CharField(max_length=100)
    ChallanDate = models.DateField()
    CallAllocatedTo = models.CharField(max_length=100,null=True, blank=True)
    EstimateRecd = models.CharField(max_length=100,null=True, blank=True)
    WorkEngaged = models.CharField(max_length=100,null=True, blank=True) 
    Other = models.CharField(max_length=100,null=True, blank=True) 
    Remark = models.TextField()
    TotalAmount = models.CharField(max_length=100,null=True, blank=True) 
    complet = models.CharField(max_length=100,default='0',null=True, blank=True)
    IN = models.CharField(max_length=100,default='0', blank=True)


    def NDate(self):
        return str(self.Date.strftime('%d-%m-%Y'))
    
    def NCallDate(self):
        return str(self.CallDate.strftime('%d-%m-%Y'))
    
    def NCloseDate(self):
        return self.CloseDate.strftime('%d-%m-%Y')
    
    def NChallanDate(self):
        return self.ChallanDate.strftime('%d-%m-%Y')
    
    def EDate(self):
        return str(self.Date.strftime('%Y-%m-%d'))
    
    def ECallDate(self):
        if self.CallType == 'WorkOrder':
            d = str(self.CallDate.strftime('%Y-%m-%d'))
        else:
            d = ''
        return d
    
    def ECloseDate(self):
        return str(self.CloseDate.strftime('%Y-%m-%d'))   
    def EChallanDate(self):
        return str(self.ChallanDate.strftime('%Y-%m-%d'))
    

class ICountModel(models.Model):
    InvoiceNo = models.IntegerField(default=0)
    Ron = models.CharField(max_length=100,null=True, blank=True)

class InvoiceModel(models.Model):
    Partyid = models.OneToOneField(PartyModel,on_delete=models.SET_NULL,null=True, blank=True)
    InvoiceData = models.DateField(null=True, blank=True)
    InvoiceNo = models.CharField(max_length=100,null=True, blank=True)
    BillMonth = models.CharField(max_length=100,null=True, blank=True)
    PartyName = models.CharField(max_length=100,null=True, blank=True)
    Cluster = models.CharField(max_length=100, null=True, blank=True)
    Cluster_id = models.CharField(max_length=100, null=True, blank=True)
    BillYear = models.CharField(max_length=100,null=True, blank=True)
    Tax = models.CharField(max_length=100,null=True, blank=True)
    datein = models.CharField(max_length=100,null=True, blank=True)
    Type = models.CharField(max_length=100,null=True, blank=True)
    FromDate = models.DateField(null=True, blank=True)
    ToDate = models.DateField(null=True, blank=True)
    Amount = models.CharField(max_length=100,null=True, blank=True)
    GSTAmount = models.CharField(max_length=100,null=True, blank=True)
    TotalAmount = models.CharField(max_length=100,null=True, blank=True)

    def ndate(self):
        return self.InvoiceData.strftime('%d-%m-%Y')

class InvoiceRCModel(models.Model):
    InvoiceNo = models.CharField(max_length=100,null=True, blank=True)
    Counter = models.IntegerField(default=0,null=True, blank=True)
    RCCode = models.CharField(max_length=100,null=True, blank=True)
    RCDescription = models.TextField(null=True, blank=True)
    Quantity = models.CharField(max_length=100,null=True, blank=True)
    Rate = models.CharField(max_length=100,default='0',null=True, blank=True)
    HSNCode = models.IntegerField(default=0,null=True, blank=True)
    Unit = models.CharField(max_length=100,null=True, blank=True)
    Labour = models.CharField(max_length=100,default='0',null=True, blank=True)
    Amount = models.CharField(max_length=100,default='0',null=True, blank=True)
    GSTRate = models.CharField(max_length=100,null=True, blank=True)
    GSTAmount = models.CharField(max_length=100,null=True, blank=True)
    GSTTA = models.CharField(max_length=100,default='0',null=True, blank=True)
    TotalAmount = models.CharField(max_length=100,default='0',null=True, blank=True)

class QCountModel(models.Model):
    QuotationNo = models.IntegerField(default=0)

class QuotationModel(models.Model):
    Counter = models.IntegerField(default=0)
    QuotationNo = models.IntegerField(default=0,null=True, blank=True) 
    Date = models.DateField()
    PartyName = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)
    Address = models.TextField()
    Problem = models.TextField()
    Code = models.CharField(max_length=100)
    CallRef = models.CharField(max_length=100)
    CallNo = models.CharField(max_length=100)
    WorkEngaged = models.CharField(max_length=100,null=True, blank=True) 
    Other = models.CharField(max_length=100,null=True, blank=True)
    Subject = models.CharField(max_length=100,null=True, blank=True) 
    AreaOfWork = models.CharField(max_length=100, null=True, blank=True)
    Remark = models.TextField()
    TC = models.TextField()
    Amount = models.CharField(max_length=100,null=True, blank=True)
    GSTAmount = models.CharField(max_length=100,null=True, blank=True)
    TotalAmount = models.CharField(max_length=100,null=True, blank=True)
    Type = models.CharField(max_length=100,null=True, blank=True)
    BRName = models.CharField(max_length=100,null=True, blank=True)
    MOBILENO = models.CharField(max_length=100,null=True, blank=True)
    EmailID = models.CharField(max_length=100,null=True, blank=True)
    ASDDate = models.DateField(null=True, blank=True)
    ASDNo = models.CharField(max_length=100,null=True, blank=True)

    def ndate(self):
        return self.Date.strftime('%d-%m-%Y')
    
    def NASDDate(self):
        return self.ASDDate.strftime('%d-%m-%Y')
    
class QTTGSTModel(models.Model):
    Counter = models.IntegerField(default=0,null=True, blank=True)
    TYPES = models.CharField(max_length=100,null=True, blank=True)
    RCCode = models.CharField(max_length=100,null=True, blank=True)
    RCDescription = models.TextField(null=True, blank=True)
    Quantity = models.CharField(max_length=100,null=True, blank=True)
    HSNCode = models.IntegerField(default=0,null=True, blank=True)
    Unit = models.CharField(max_length=100,null=True, blank=True)
    Rate = models.CharField(max_length=100,default='0',null=True, blank=True)
    Labour = models.CharField(max_length=100,default='0',null=True, blank=True)
    Amount = models.CharField(max_length=100,default='0',null=True, blank=True)
    GSTRate = models.CharField(max_length=100,null=True, blank=True)
    GSTAmount = models.CharField(max_length=100,null=True, blank=True)
    GSTTA = models.CharField(max_length=100,default='0',null=True, blank=True)
    TotalAmount = models.CharField(max_length=100,default='0',null=True, blank=True)


class ProfileModel(models.Model):
    UserName = models.CharField(max_length=100, null=True, blank=True)
    CompanyName = models.CharField(max_length=100, null=True, blank=True)
    PhoneNo = models.CharField(max_length=100, null=True, blank=True)
    GSTNo = models.CharField(max_length=100, null=True, blank=True)
    PanNo = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Address = models.TextField(null=True, blank=True)