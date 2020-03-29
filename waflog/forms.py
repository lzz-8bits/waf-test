from django import forms
from.models import NodeInfo


class UserForm(forms.Form):
    username = forms.CharField(label='',max_length=100,widget=forms.TextInput(
        attrs={'id': 'username','placeholder': 'User'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(
        attrs={'id': 'password','placeholder': 'Password'}))

'''class modeadimnForm(forms.Form):
    fun_select = [
        ('cmd.run', 'cmd.run'),
        ('test.ping', 'test.ping'),
    ]
    nodelist = forms.ModelChoiceField(queryset=NodeInfo.objects.all(),empty_label="*",to_field_name="hostname",widget=forms.Select(
        attrs={'id':'hostlist', 'class':'selectpicker show-tick form-control', 'name':'hostlist'}))
    funlist = forms.CharField(widget=forms.Select(
        choices=fun_select,attrs={'id':'funlist', 'class':'selectpicker show-tick form-control', 'name':'funlist'}))
    command = forms.CharField(label='命令',widget=forms.TextInput(
        attrs={'class':'form-control','id':'search_name', 'name':'command'}))'''