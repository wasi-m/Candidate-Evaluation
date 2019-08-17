
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from candidate.models import Contact, ContactVerified

from .forms import CustomUserCreationForm
from candidate.forms import EvaluationForm
from users.decorators import login_required


class SignUpView(CreateView):

	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'
	
	# def form_valid(self, form):
	# 	msg = form.cleaned_data['email']
	# 	form.send_activation_email(msg)


@login_required()
def dashboard(request):
	data = ContactVerified.objects.all()
	print(data)
	return render(request, 'dashboard.html', {'data': data})


@login_required()
def detail(request, candidate_email):
	try:
		candidate = Contact.objects.get(pk=candidate_email)
	except Contact.DoesNotExist:
		raise Http404("Candidate does not exist")
	return render(request, 'detail.html', {'candidate': candidate})


@login_required()
def results(request, candidate_email):
	data = ContactVerified.objects.filter(contact_id__email=candidate_email)
	return render(request, 'result.html', { 'data': data })


@login_required()
def allfivestarresults(request):
	data = ContactVerified.objects.filter(review_rating__gte="5")
	return render(request, 'topresults.html', { 'data': data })


@login_required()
def evaluate(request, candidate_email):
	if request.method == 'POST':
		form = EvaluationForm(request.POST)
		if form.is_valid():

			current_user = request.user
			candidate = Contact.objects.get(pk=candidate_email)

			vefification_exists = ContactVerified.objects.filter(verified_by=current_user, contact_id=candidate)

			if (vefification_exists.count() == 0):

				contact_verification = ContactVerified()

				contact_verification.verified_by = current_user
				contact_verification.contact_id = candidate
				contact_verification.comment = form.cleaned_data['comment']
				contact_verification.review_rating = form.cleaned_data['review_rating']

				contact_verification.save()
				print('success')
				data = 'sucess'
				return HttpResponseRedirect('/users/dashboard/', {'data':data})
			else:
				data = 'Contact already evaluated'
				print('Contact already evaluated')
				return HttpResponseRedirect('/users/'+candidate_email+'/', {'data':data})

	else:
		form = EvaluationForm()

	return render(request, 'evaluate.html', {'form': form})
