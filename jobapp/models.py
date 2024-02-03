from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()



    
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)



class cv(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length = 100)
    profession = models.CharField(max_length = 100)
    gmail = models.EmailField()
    phone = models.CharField(max_length = 20)
    linkedin = models.CharField(max_length = 250)
    github = models.CharField(max_length = 250)

    photo = models.ImageField(upload_to='photos/', null=True, blank=True, default='default.jpg')

    description = models.TextField()

    degree1 = models.CharField(max_length = 100, null = True, blank = True)
    university1 = models.CharField(max_length = 100, null = True, blank = True)
    graduation_year1 = models.IntegerField(null = True, blank = True)

    degree2 = models.CharField(max_length = 100, null = True, blank = True)
    university2 = models.CharField(max_length = 100, null = True, blank = True)
    graduation_year2 = models.IntegerField(null = True, blank = True)

    company1 = models.CharField(max_length = 100, null = True, blank = True)
    project1 = models.CharField(max_length = 100, null = True, blank = True)
    experience_description1 = models.TextField(null = True, blank = True)

    company2 = models.CharField(max_length = 100, null = True, blank = True)
    project2 = models.CharField(max_length = 100, null = True, blank = True)
    experience_description2 = models.TextField(null = True, blank = True)

    skill1 = models.CharField(max_length = 100, null = True, blank = True)
    skill2 = models.CharField(max_length = 100, null = True, blank = True)
    skill3 = models.CharField(max_length = 100, null = True, blank = True)
    skill4 = models.CharField(max_length = 100, null = True, blank = True)

    hobbies1 = models.CharField(max_length = 100, null = True, blank = True)
    hobbies2 = models.CharField(max_length = 100, null = True, blank = True)
    hobbies3 = models.CharField(max_length = 100, null = True, blank = True)
    hobbies4 = models.CharField(max_length = 100, null = True, blank = True)

    reference = models.CharField(max_length = 150, null = True, blank = True)

    def __str__(self):
        return (f'{self.full_name} CV')


class JobDetail(models.Model):
    employer = models.ForeignKey(User, on_delete = models.CASCADE)
    position = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    description = models.TextField()
    website = models.CharField(max_length = 256)

    category = models.CharField(max_length = 150)
    level = models.CharField(max_length = 100)
    number_vacancy = models.IntegerField()
    emp_type = models.CharField(max_length = 150)
    salary = models.CharField(max_length= 150)
    date = models.DateField()

    edu_level = models.CharField(max_length = 150)
    exp_req = models.CharField(max_length = 150)
    skill_req = models.CharField(max_length = 200)

    job_desc1 = models.CharField(max_length = 200)
    job_desc2 = models.CharField(max_length = 200)
    job_desc3 = models.CharField(max_length = 200)
    job_desc4 = models.CharField(max_length = 200)
    job_desc5 = models.CharField(max_length = 200)

    other_spec1 = models.CharField(max_length = 256)
    other_spec2 = models.CharField(max_length = 256)
    other_spec3 = models.CharField(max_length = 256)
    other_spec4 = models.CharField(max_length = 256)
    other_spec5 = models.CharField(max_length = 256)
     
    def __str__(self):
        return self.position


class SavedJobs(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    job = models.ForeignKey(JobDetail, on_delete = models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user} | {self.job}"
    
class AppliedJobs(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    job = models.ForeignKey(JobDetail, on_delete = models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user} | {self.job}"