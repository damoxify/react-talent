# from django.db import models

# from django.db import models

# class Job(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     company = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     salary = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.title

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
