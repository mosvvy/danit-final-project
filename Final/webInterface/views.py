from asyncio import wait_for
from datetime import time

import pandas as pd
from django.shortcuts import render
from django import forms

from Analytics.data_loader import get_purposes
from Analytics.ml import predict_by_value

# from .models import Data


# Create your views here.

PURPOSES = (
    ("purpose_credit_card", "credit card"),
    ("purpose_debt_consolidation", "debt consolidation"),
    ("purpose_educational", "educational"),
    ("purpose_home_improvement", "home improvement"),
    ("purpose_major_purchase", "major purchase"),
    ("purpose_small_business", "small business")
)# get_purposes()

class CheckForm(forms.Form):
    credit_policy = forms.IntegerField()
    purpose = forms.ChoiceField(choices = PURPOSES)
    int_rate = forms.FloatField()
    installment = forms.FloatField()
    log_annual_inc = forms.FloatField()
    dti = forms.FloatField()
    fico = forms.IntegerField()
    days_with_cr_line = forms.FloatField()
    revol_bal = forms.IntegerField()
    revol_util = forms.FloatField()
    inq_last_6mths = forms.IntegerField()
    delinq_2yrs = forms.IntegerField()
    pub_rec = forms.IntegerField()


def check(request):
    context = {}
    context['res'] = "TEST"
    form = CheckForm(request.POST or None)
    if form.is_valid():
        context['res'] = "predict_by_value(df)"
        # subject = form.cleaned_data["subject"]
        # message = form.cleaned_data["message"]
        # sender = form.cleaned_data["sender"]
        # cc_myself = form.cleaned_data["cc_myself"]
        #
        # recipients = ["info@example.com"]

        input_val = {
            "credit.policy": form.cleaned_data["credit_policy"],
            "purpose": [form.cleaned_data["purpose"]],
            "int.rate": [form.cleaned_data["int_rate"]],
            "installment": [form.cleaned_data["installment"]],
            "log.annual.inc": [form.cleaned_data["log_annual_inc"]],
            "dti": [form.cleaned_data["dti"]],
            "fico": [form.cleaned_data["fico"]],
            "days.with.cr.line" : [form.cleaned_data["days_with_cr_line"]],
            "revol.bal": [form.cleaned_data["revol_bal"]],
            "revol.util": [form.cleaned_data["revol_util"]],
            "inq.last.6mths": [form.cleaned_data["inq_last_6mths"]],
            "delinq.2yrs": [form.cleaned_data["delinq_2yrs"]],
            "pub.rec": [form.cleaned_data["pub_rec"]],
            }
        df = pd.DataFrame(input_val)
        context['res'] = predict_by_value(df)

    context['form'] = form
    return render(request, "data.html", context)
