import pandas as pd
from django.shortcuts import render

from Analytics.ml import predict_by_value, train_pipeline, predict_pipeline_by_val
from webInterface.forms import CheckForm

# Create your views here.

def check(request):
    context = {}
    context['res'] = "TEST"
    form = CheckForm(request.POST or None)
    if form.is_valid():
        context['res'] = "predict_by_value(df)"

        input_val = {
            "credit.policy": form.cleaned_data["credit_policy"],
            "purpose": [form.cleaned_data["purpose"]],
            # "int.rate": [form.cleaned_data["int_rate"]],
            # "installment": [form.cleaned_data["installment"]],
            "log.annual.inc": [form.cleaned_data["log_annual_inc"]],
            "dti": [form.cleaned_data["dti"]],
            "fico": [form.cleaned_data["fico"]],
            # "days.with.cr.line" : [form.cleaned_data["days_with_cr_line"]],
            # "revol.bal": [form.cleaned_data["revol_bal"]],
            # "revol.util": [form.cleaned_data["revol_util"]],
            # "inq.last.6mths": [form.cleaned_data["inq_last_6mths"]],
            "delinq.2yrs": [form.cleaned_data["delinq_2yrs"]],
            "pub.rec": [form.cleaned_data["pub_rec"]],
            }
        df = pd.DataFrame(input_val)

        context['res'] = "Схвалено" if predict_pipeline_by_val(df)[0] == 1 else "Не схвалено"

    context['form'] = form
    return render(request, "data.html", context)
