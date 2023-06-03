from django.contrib import admin


from django.contrib import admin

from .models import tokens,user_admin,loging,user_cookies
from django import forms

from django import forms
# from .widgets import RichTextEditorWidget


class AccountModelForm(forms.ModelForm):
    mse = forms.CharField(widget=forms.Textarea, label="备注", required=False)

    class Meta:
        model = loging
        fields = '__all__'

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        loging.mse: {'widget': forms.Textarea},
    }

# class AccountAdmin(admin.ModelAdmin):

#     form = AccountModelForm


class tokensAdmin(admin.ModelAdmin):
    list_display = ('token', 'creatime',"Recentime","balance","purchasetime","timelength","remark","isBanned")



# @admin.register(loging)
class logingAdmin(admin.ModelAdmin):
    form = AccountModelForm
    list_display = ('uid', 'creatime',"users","state")
    # formfield_overrides = {
    #     loging.mse: {'widget': forms.Textarea},
    # }


    
class user_cookiesAdmin(admin.ModelAdmin):
    list_display = ('uid',"creatime","state")

class user_adminAdmin(admin.ModelAdmin):
    list_display = ('username',"creatime","Recentime","uses")

admin.site.register(tokens,tokensAdmin)
admin.site.register(user_admin,user_adminAdmin)
admin.site.register(loging,logingAdmin)
admin.site.register(user_cookies,user_cookiesAdmin)
# Register your models here.
