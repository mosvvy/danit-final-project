from django.shortcuts import render
from django import forms

from .models import Data


# Create your views here.

class CheckForm(forms.ModelForm):
    class Meta:
        model = Data

        fields = [
            "credit.policy",
            "purpose",
            "int.rate",
            "installment",
            "log.annual.inc",
            "dti",
            "fico",
            "days.with.cr.line",
            "revol.bal",
            "revol.util",
            "inq.last.6mths",
            "delinq.2yrs",
            "pub.rec",
        ]


def check(request):
    context = {}
    form = CheckForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "data.html", context)
