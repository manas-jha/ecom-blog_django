from django.db import models

# Create your models here.


#libraty information  for the file and the submission of out data into the admin page
# class library_contact(models.Model):
#     lab_id = models.AutoField(max_length=22)
#     category = models.CharField(max_length=45, default="")
#     libraty_shell_no = models.IntegerField(max_,length = 43, default = "")

#     def __str__(self):
#        return self.update_desc[0:7] + "..."
# #class for the desc of the project and remove when unnacessary
# class description(models.Model):
#     pass
    

#All is going normall to project
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class order(models.Model):
    order_id =  models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=50000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    state = models.CharField(max_length=90)
    zip_code = models.CharField(max_length=90)
    phone = models.CharField(max_length=90, default="")


class orderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.CharField(max_length=5000)
    timeStamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."