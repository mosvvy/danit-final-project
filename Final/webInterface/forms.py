from django import forms

PURPOSES = (
    ("credit_card", "credit card"),
    ("debt_consolidation", "debt consolidation"),
    ("educational", "educational"),
    ("home_improvement", "home improvement"),
    ("major_purchase", "major purchase"),
    ("small_business", "small business"),
    ("all_other", "all other"),
)# get_purposes()

class CheckForm(forms.Form):
    credit_policy = forms.IntegerField(label="Кредитна політика")
    purpose = forms.ChoiceField(label="Мета ", choices = PURPOSES)
    # int_rate = forms.FloatField()
    # installment = forms.FloatField()
    log_annual_inc = forms.FloatField(label="Натуральний показник річного доходу")
    dti = forms.FloatField(label="Співвідношення кредиту до доходу позичальника")
    fico = forms.IntegerField(label="FICO", min_value=300, max_value=850)
    # days_with_cr_line = forms.FloatField()
    # revol_bal = forms.IntegerField()
    # revol_util = forms.FloatField()
    # inq_last_6mths = forms.IntegerField()
    delinq_2yrs = forms.IntegerField(label="Затримка на 30+ за 2 роки")
    pub_rec = forms.IntegerField(label="Кількість негативних відгуків")
