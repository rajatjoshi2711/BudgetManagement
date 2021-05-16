from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

from django.core.exceptions import ValidationError
def phoneValidation(value):
    if len(str(value)) == 10:
        return value
    else:
        raise ValidationError('phone no. should be of 10 digit')

# Property Details
class Property(models.Model):
    type = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200, default='')


# User Details
class User(AbstractUser):
    is_sale = models.BooleanField(default=False)
    is_finance = models.BooleanField(default=False)
    is_purchase = models.BooleanField(default=False)
    is_management = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField()


class Sale(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # sale_mobile = models.IntegerField(default=0)
    # sale_address = models.CharField(max_length=200, default='')
    # sale_description = models.CharField(max_length=500, default='No description is added')
    # sale_image = models.FileField(upload_to='images/', null=True, verbose_name="", default='profile-01.jpg')

    def __str__(self):
        return self.user.username


class Finance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # finance_mobile = models.IntegerField(default=0)
    # finance_address = models.CharField(max_length=200, default='')
    # finance_description = models.CharField(max_length=500,  default='No description is added')
    # finance_image = models.FileField(upload_to='images/', null=True, verbose_name="", default='profile-01.jpg')

    def __str__(self):
        return self.user.username


class Purchase(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # purchase_mobile = models.IntegerField(default=0)
    # purchase_address = models.CharField(max_length=200, default='')
    # purchase_description = models.CharField(max_length=500, default='No description is added')
    # purchase_image = models.FileField(upload_to='images/', null=True, verbose_name="", default='profile-01.jpg')

    def __str__(self):
        return self.user.username


class Management(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # management_mobile = models.IntegerField(default=0)
    # management_address = models.CharField(max_length=200, default='')
    # management_description = models.CharField(max_length=500,  default='No description is added')
    # management_image = models.FileField(upload_to='images/', null=True, verbose_name="", default='profile-01.jpg')

    def __str__(self):
        return self.user.username


class Vendor_Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    mobile = models.IntegerField(default='', validators=[phoneValidation])
    email = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=200, default='')
    is_gst = models.BooleanField( default=False, null=True, blank=True)
    gstin = models.CharField(max_length=100, default='')
    bank_name = models.CharField(max_length=100, default='')
    pan = models.CharField(max_length=100, default='')
    ifsc = models.CharField(max_length=100, default='')
    account_no = models.IntegerField(default=0)
    is_pan = models.BooleanField( default=False, null=True, blank=True)
    black_list = models.BooleanField( default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Project_model(models.Model):
    project_no = models.CharField(max_length=40, default='', primary_key=True)
    name = models.CharField(max_length=100, default='')
    allocate = models.IntegerField(default=0)
    utilized = models.IntegerField(default=0)
    available = models.IntegerField(default=0)

    def __str__(self):
        return str(self.project_no)

class Rml_model(models.Model):
    class Meta:
        unique_together = (('project_no', 'rml_no'),)
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_utilized_lte_allocate",
                check=models.Q(utilized__lte=models.F("allocate")),
            )
        ]

    project_no = models.ForeignKey(Project_model, on_delete=models.CASCADE)
    rml_no = models.CharField(null=False, max_length=40)
    specification = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=False)
    unit = models.CharField(max_length=20, null=False)
    #unit_price = models.IntegerField(null=True,blank=True)
    allocate = models.IntegerField(default=0)
    utilized = models.IntegerField(default=0)
    available = models.IntegerField(default=models.F('allocate'))
    attachment = models.BooleanField(default=True)

    def __str__(self):
        return str(self.project_no)


class Purchase_Order_Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor_Model, on_delete=models.CASCADE)
    invoice_for = models.CharField(max_length=255,default='')
    project = models.ForeignKey(Project_model, on_delete=models.CASCADE,related_name='project')
    rml = models.CharField(null=False, max_length=40)

    sub_total = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    total_gst = models.IntegerField(default=0)
    total_sgst = models.IntegerField(default=0)
    total_cgst = models.IntegerField(default=0)
    attachment = models.FileField(upload_to='files/', null=True,blank=True, verbose_name="", default='')
    po_date = models.DateTimeField(default=datetime.datetime.now())
    total_igst = models.IntegerField(default=0)

    class Meta:
        db_table = 'Purchase_Order_Model'

    def __str__(self):
        return str(self.id)


class Particulars(models.Model):

    purchase = models.ForeignKey(Purchase_Order_Model,related_name='purchase', on_delete=models.CASCADE,)
    particular = models.CharField(max_length=100, default='')
    tax_value = models.IntegerField(default=0)
    gst = models.IntegerField(default=0)
    cgst = models.IntegerField(default=0)
    sgst = models.IntegerField(default=0)
    igst = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    class Meta:
        db_table = 'Particulars'

    def __str__(self):
        return self.particular


class Invoice_Model(models.Model):
    project = models.ForeignKey(Project_model, on_delete=models.CASCADE)
    invoice_for = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor_Model, on_delete=models.CASCADE)
    rml = models.CharField(null=False, max_length=40)
    total_amount = models.IntegerField(default=0)
    total_igst = models.IntegerField(default=0)
    total_sgst = models.IntegerField(default=0)
    total_cgst = models.IntegerField(default=0)
    # sub_total = models.IntegerField(default=0)
    # packing = models.IntegerField(default=0)
    # freight = models.IntegerField(default=0)
    # insurance= models.IntegerField(default=0)
    grand_total = models.IntegerField(default=0)
    PO_Issued = models.BooleanField(default=False)
    remark = models.CharField(max_length=1000, default='')
    po_no = models.ForeignKey(Purchase_Order_Model, on_delete=models.CASCADE)
    terms = models.CharField(max_length=1000, default='')
    due_date = models.DateTimeField(default=datetime.datetime.now())
    invoice_date = models.DateTimeField(default=datetime.datetime.now())
    total_gst = models.IntegerField(default=0)

    class Meta:
        db_table = 'Invoice_Model'

    def __str__(self):
        return self.invoice_for


class Invoice(models.Model):

    invoice = models.ForeignKey(Invoice_Model, related_name='invoice', on_delete=models.CASCADE,)
    description = models.CharField(max_length=100, default='')
    amount = models.IntegerField(default=0)
    igst = models.IntegerField(default=0)
    cgst = models.IntegerField(default=0)
    sgst = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    gst = models.IntegerField(default=0)
    total = models.IntegerField(default=0)


    class Meta:
        db_table = 'Invoice'

    def __str__(self):
        return self.description


class Payment_Model(models.Model):
    invoice_id = models.IntegerField(default=0)
    amount = models.IntegerField( default=0)
    remain_amount = models.IntegerField(default=0)
    transaction_type = models.CharField(max_length=200, default='')
    transaction_mode = models.CharField(max_length=100, default='')
    date = models.DateTimeField(default='2021-05-01')
    transaction_id = models.CharField(max_length=100,default='')

    def str(self):
        return self.invoice_id

class Request_model(models.Model):
    po_id = models.IntegerField(default=0)
    invoice_id = models.IntegerField(default=0)
    vendor = models.CharField(max_length=100, default='')
    amount = models.IntegerField(default=0)
    payment_terms = models.CharField(max_length=200, default='')
    due_date = models.DateTimeField()
   
    date = models.DateTimeField(default=datetime.datetime.today().strftime('%Y-%m-%d'))
    
    status = models.CharField(max_length=100, default='Pending')
    project_no = models.CharField(max_length=40, default='')
    tds = models.IntegerField(default=0)
    tds_type = models.CharField(max_length=100, default='')
    adv_pay = models.IntegerField(default=0)
    net_pay_amt = models.IntegerField(default=0)
    bal_pay_amt = models.IntegerField(default=0)


    def str(self):
        return self.status