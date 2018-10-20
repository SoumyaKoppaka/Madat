from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import generic

from ..decorators import local_body_required
from ..forms import LocalBodySignUpForm, EventForm
from ..models import User, BloodDonationEvent
from ..utils import send_event_message

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


def view_event(request):
    all_products = BloodDonationEvent.objects.all()
    return render(request, 'roles/local_bodies/all_event.html', {'all_products': all_products})


@login_required
@local_body_required
def upload_event(request):
    #if not request.user.is_authenticated:
        #return render(request, 'registration/signup_form.html')
    #else:
        form = EventForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            send_event_message()
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
            #return render(request, 'roles/local_bodies/local_bodies_home.html', {'event': event})
