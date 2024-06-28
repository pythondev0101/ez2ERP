from django import forms


class ProfileCompanyForm(forms.Form):
    name = forms.CharField(required=True)


class ProfileUserForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    username = forms.CharField(required=True)


