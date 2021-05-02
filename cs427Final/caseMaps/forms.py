from django import forms




class DemographicForm(forms.Form):
    demographic_choices = [
        (0, 'Age'),
        (0, 'Race'),
        (0, 'Gender'),
        (0, 'Age'),
    ]