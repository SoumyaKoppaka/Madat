from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import generic

from roles.templates.roles.filters import UserFilter
from ..decorators import local_body_required, recipient_required
from ..forms import LocalBodySignUpForm, EventForm
from ..models import User, BloodDonationEvent, Recipient

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


class LocalBodySignUpView(generic.CreateView):
    model = User
    form_class = LocalBodySignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 5
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('local_bodies:local_bodies_home')


@method_decorator([login_required, local_body_required], name='dispatch')
class LocalBodyHomeView(generic.TemplateView):
    template_name = 'roles/local_bodies/local_bodies_home.html'
    model = BloodDonationEvent


def view_event(request):
    user_list = BloodDonationEvent.objects.all()
    filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'roles/local_bodies/all_event.html', {'filter': filter})


# def view_event(request):
#   all_products = BloodDonationEvent.objects.all()
# filter = UserFilter(request.GET, queryset=BloodDonationEvent.objects.all())
#  return render(request, 'roles/local_bodies/all_event.html', {'all_products': all_products})
# return render(request, 'roles/local_bodies/all_event.html', {'filter': filter})
# def get_context_data(self, **kwargs):
#   context = super().get_context_data(**kwargs)
#  context['filter']=UserFilter(self.request.GET, queryset=self.get_queryset())
# return context
def view_scheme(request, name):
    product = BloodDonationEvent.objects.get(name=name)
    return render(request, 'roles/local_bodies/scheme.html', {'product': product})


@login_required
@recipient_required
def if_eligible(request, name):
    user = User.objects.get(pk=request.user.id)
    product = BloodDonationEvent.objects.get(name=name)
    if user.recipient.designation == product.el_designation:
        if user.recipient.gender == product.el_gender:
            if user.recipient.age <= product.el_age:
                if user.recipient.income == product.el_income:
                    if user.recipient.education == product.el_education:
                        return render(request, 'roles/local_bodies/eligible_yes.html', {'product': product})
    return render(request, 'roles/local_bodies/eligible_no.html', {'product': product})


@login_required
@local_body_required
def upload_event(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        event = form.save(commit=False)
        event.user = request.user
        event.save()
        return render(request, 'roles/local_bodies/local_bodies_home.html', {'event': event})
    context = {
        "form": form,
    }
    return render(request, 'roles/local_bodies/upload_event.html', context)


'''
            event.poster = request.FILES['poster']
            file_type = event.poster.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'event': event,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'roles/local_bodies/upload_event.html', context)
                '''
# return render(request, 'roles/local_bodies/local_bodies_home.html', {'event': event})
