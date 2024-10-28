from django.db import models
from django.contrib import admin
class loan_customer(models.Model):
  lc=models.CharField(max_length=20,primary_key="lc")
  name=models.CharField(max_length=50)
  loan_amount=models.IntegerField()
  interest_rate=models.FloatField()
  numberofyears=models.FloatField()
  typeofinterest=models.CharField(max_length=20)
  typeofloan=models.CharField(max_length=20)

class loan_customerAdmin(admin.ModelAdmin):
   list_display=('loan_amount','name','interest_rate','numberofyears','typeofinterest','lc','typeofloan')