from django.db import models


class Maincategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    addressline1 = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    addressline2 = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    addressline3 = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    pin = models.CharField(max_length=50, default=None, null=True, blank=True)
    city = models.CharField(max_length=50, default=None, null=True, blank=True)
    state = models.CharField(
        max_length=50, default=None, null=True, blank=True)
    pic = models.FileField(
        upload_to='images', default='images/defaultlogopic.png', null=True, blank=True)

    def __str__(self):
        return str(self.id)+" "+self.username


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    maincategory = models.ForeignKey(Maincategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, default=None)
    baseprice = models.IntegerField()
    discount = models.IntegerField()
    finalprice = models.IntegerField()
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.CharField(max_length=20, default="In Stock")
    pic1 = models.ImageField(
        upload_to="images", default='nopic.jpg', null=True, blank=True)
    pic2 = models.ImageField(
        upload_to="images", default='nopic.jpg', null=True, blank=True)
    pic3 = models.ImageField(
        upload_to="images", default='nopic.jpg', null=True, blank=True)
    pic4 = models.ImageField(
        upload_to="images", default='nopic.jpg', null=True, blank=True)

    def __str__(self):
        return str(self.id)+" "+self.name


class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    addressline1 = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    addressline2 = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    addressline3 = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    pin = models.CharField(max_length=50, default=None, null=True, blank=True)
    city = models.CharField(max_length=50, default=None, null=True, blank=True)
    state = models.CharField(
        max_length=50, default=None, null=True, blank=True)
    pic = models.FileField(
        upload_to="images", default='images/defaultlogopic.png', null=True, blank=True)

    def __str__(self):
        return str(self.id)+" "+self.username


class Wishlist(models.Model):
    id= models.AutoField(primary_key=True)
    buyer= models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+" "+self.buyer.username

order = ((0,"Cancelled"),(1,"Not Packed"),(2,"Packed"),(3,"Out For Delivery"),(4,"Delievered"))
payment = ((1,"pending"),(2,"Successful"))
class checkout(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.IntegerField()
    shipping = models.IntegerField()
    final = models.IntegerField()
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    mode = models.CharField(max_length=20,default="POD")
    orderstatus = models.IntegerField(choices=order,default=1)
    paymentstatus = models.IntegerField(choices=payment,default=1)
    rppid = models.CharField(max_length=1000,default="",null=True,blank=True)
    rpoid = models.CharField(max_length=1000,default="",null=True,blank=True)
    rpsid = models.CharField(max_length=1000,default="",null=True,blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" "+self.buyer.username

class CheckoutProducts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    price = models.IntegerField()
    qty = models.IntegerField()
    total = models.IntegerField()
    pic = models.ImageField()
    checkout = models.ForeignKey(checkout,on_delete=models.CASCADE)
    

    def __str__(self):
        return "pid = "+str(self.id)+" checkout Id "+str(self.checkout.id)


class Newsletter(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50,unique=True)


    def __str__(self):
        return self.email

contactStatusChoice = ((1,"Active"),(2,"Resolved"))
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="",null=True,blank=False)
    email = models.EmailField(max_length=50,default="",null=True,blank=False)
    phone = models.IntegerField(default="",null=True,blank=False)
    message = models.TextField(blank=True)
    status = models.IntegerField(choices = contactStatusChoice,default=1)

    def __str__(self):
        return str(self.id)+" "+self.email+" "+self.message