from django import forms

class StudentImportForm(forms.Form):
    excel_file = forms.FileField()
