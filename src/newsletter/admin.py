from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm
# For display in admin panel - without list_display, they dont show up
# ModelAdmin allows customization of Admin panels
class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm

	# class Meta:
	# 	model = SignUp
admin.site.register(SignUp, SignUpAdmin)