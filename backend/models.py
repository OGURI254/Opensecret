from django.db import models
from django.contrib import admin




class Work(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    client = models.CharField(max_length=100)
    services = models.TextField()
    project = models.TextField()
    image = models.ImageField(upload_to='works/', null=True, blank=True)

    def __str__(self):
        return self.title

class WorkImage(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='work_images/', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.work.title}"

class WorkImageInline(admin.TabularInline):
    model = WorkImage

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    inlines = [WorkImageInline]

@admin.register(WorkImage)
class WorkImageAdmin(admin.ModelAdmin):
    pass



class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField()
    picture = models.ImageField(upload_to='blog/', null=True, blank=True)
    categories = models.ManyToManyField('Category', related_name='blogs')
    tags = models.ManyToManyField('Tag', related_name='blogs')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

    # contact

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name



