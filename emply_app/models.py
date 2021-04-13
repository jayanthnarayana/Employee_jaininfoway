from django.db import models


class Emp(models.Model):

    name=models.CharField(max_length=200,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True) #inbuilt email field can also be used

    def __str__(self):          
        return 'name:{}, age:{}, email:{}, \
            '.format(self.name, self.age,
            self.email)

    class Meta:
        db_table = "Emp"
