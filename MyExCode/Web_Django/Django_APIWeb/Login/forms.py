from django import forms


class addUserForm(forms.Form):
    '''新增使用者表單'''
    account = forms.CharField(label='帳號', max_length=20)
    account.widget.attrs.update({'class': 'form-control'})  # 套上css檔
    password = forms.CharField(
        label='密碼', max_length=30, widget=forms.PasswordInput)
    password.widget.attrs.update({'class': 'form-control'})  # 套上css檔


class editUserForm(forms.Form):
    '''編輯使用者表單'''
    default_account = ''
    account = forms.CharField(
        label='帳號', max_length=20, initial=default_account)
    account.widget.attrs.update({'class': 'form-control'})  # 套上css檔
    accountState = forms.ChoiceField(
        label='狀態', choices=[('Active', '正常'), ('Locked', '鎖定')], initial='Active')
    accountState.widget.attrs.update({'class': 'form-control'})
    detial = forms.CharField(label='備註')
    detial.widget.attrs.update({'class': 'form-control'})  # 套上css檔


class changePassword(forms.Form):
    password = forms.CharField(
        label='密碼', max_length=30, widget=forms.PasswordInput)
    password.widget.attrs.update({'class': 'form-control'})  # 套上css檔
