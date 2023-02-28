from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label='Title task', max_length=200)
    description = forms.CharField(widget=forms.Textarea)