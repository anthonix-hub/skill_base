from django.db import models
from django.urls import reverse_lazy,reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()
 
class users(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class categories(models.Model):
    cate_id = models.AutoField(primary_key = True)
    add_categories = models.CharField(max_length = 30)

    def __str__(self):
        return self.add_categories

class product_details(models.Model):
    prod_id = models.AutoField(primary_key = True)
    add_product = models.CharField(max_length = 50)
    slug = models.SlugField(max_length=200, unique=True)
    details = RichTextUploadingField (max_length=49000)
    timestamp = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos/',verbose_name='',null=True )
    cover_img = models.ImageField(blank = True)
    category = models.ForeignKey(categories,on_delete= models.CASCADE)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.details

    # @property
    # def get_comments(self):
    #     return self.comments.all()

class product_base(models.Model):
    base_id = models.AutoField(primary_key = True)
    prod_cate = models.ForeignKey(categories,on_delete=models.CASCADE)
    detail_base = models.ForeignKey(product_details,on_delete=models.CASCADE)
    taged = models.CharField(max_length = 5)

    def __str__(self):
        return self.taged
    
class comment(models.Model):
    post = models.ForeignKey(product_details,related_name='comments',on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    timestamp = models.DateField(auto_now_add=True)
    content = RichTextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    




    