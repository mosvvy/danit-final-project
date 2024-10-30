from django.db import models

from Analytics.data_loader import get_purposes

# Create your models here.

# PURPOSES = [
#     ("purpose_credit_card", "credit card"),
#     ("purpose_debt_consolidation", "debt consolidation"),
#     ("purpose_educational", "educational"),
#     ("purpose_home_improvement", "home improvement"),
#     ("purpose_major_purchase", "major purchase"),
#     ("purpose_small_business", "small business")
# ]# get_purposes()
#
# class Data(models.Model):
#     credit_policy =models.IntegerField(name="credit.policy")
#     purpose =models.CharField(max_length=50, choices=PURPOSES, default=None, blank=True, null=True, name="purpose")
#     int_rate =models.FloatField(name="int.rate")
#     installment =models.FloatField(name="installment")
#     log_annual_inc =models.FloatField(name="log.annual.inc")
#     dti =models.FloatField(name="dti")
#     fico =models.IntegerField(name="fico")
#     days_with_cr_line =models.FloatField(name="days.with.cr.line")
#     revol_bal =models.IntegerField(name="revol.bal")
#     revol_util =models.FloatField(name="revol.util")
#     inq_last_6mths =models.IntegerField(name="inq.last.6mths")
#     delinq_2yrs =models.IntegerField(name="delinq.2yrs")
#     pub_rec =models.IntegerField(name="pub.rec")

