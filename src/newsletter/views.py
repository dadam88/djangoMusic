from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def home(request):
	composers = []
	with open('pianocomposers.txt', 'r') as f:
		for line in f:
			composers.append(line)
	
	# new user
	title = "Welcome"

	# Returning user
	if request.user.is_authenticated():
		title = "My title %s" %(request.user)
	form = SignUpForm(request.POST or None)
	context = {

		"template_title": title,
		"form": form,
		"composers": composers,

	}

	# built in for us
	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.full_name:
			instance.full_name = "Justin"
		instance.save()


	
	# Passes variables to home.html through context list of variables
	return render(request, "home.html", context)