from django.contrib import admin
from .models import Article, Evenement, Donation, Adhesion, Contact
from django.contrib import admin
from .models import Article, Evenement, Donation, Adhesion, Contact
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms

# admin.site.register(Article)
# admin.site.register(Evenement)


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'description_long': CKEditor5Widget(config_name='default'),
        }

class EvenementAdminForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = '__all__'
        widgets = {
            'description_long': CKEditor5Widget(config_name='default'),
        }

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    form = EvenementAdminForm

admin.site.register(Donation)
admin.site.register(Adhesion)
admin.site.register(Contact)
