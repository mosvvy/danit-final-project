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
            "credit.policy": [0],
            "purpose": [get_purposes()[0]],
            "int.rate": [0],
            "installment": [0],
            "log.annual.inc": [0],
            "dti": [0],
            "fico": [0],
            # "days." : [0],
            # "with.cr.line" : [0],
            "revol.bal": [0],
            "revol.util": [0],
            "inq.last.6mths": [0],
            "delinq.2yrs": [0],
            "pub.rec": [0],
            "not.fully.paid": [0]}
        df = pd.DataFrame(input_val)
        context['res'] = predict_by_value(df)

    context['form'] = form
    return render(request, "data.html", context)
