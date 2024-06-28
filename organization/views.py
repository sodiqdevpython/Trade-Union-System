from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import User, UserExtraData
from organization.models import Money, Application, Organization, Event
from .permissions import superuser_required
from .forms import EventForm

@login_required
def dashboard(request):
    if request.user.is_staff:
        verify_user = User.objects.filter(is_verified=False)
        current_money = Money.objects.get(id=1)
        users_salaries = sum(UserExtraData.objects.values_list('salary', flat=True))
        employee_count = User.objects.filter(is_verified=True).count()
        application_count = Application.objects.all().count()
        organization = Organization.objects.get(id=1)
        the_latest_news = Event.objects.get(id=1)
        context = {
            'current_money': current_money,
            'users_salary': float(users_salaries) / 100,
            'employee_count': employee_count,
            'application_count': application_count,
            'organization': organization,
            'should_verify': verify_user.count(),
            'verify_user': verify_user,
            'the_latest_news': the_latest_news
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('profile')

@login_required
def profile(request):
    if not request.user.is_verified:
        return redirect('filling_info')
    else:
        context = {
            'data': get_object_or_404(User, id=request.user.id),
            'events': Event.objects.all()[::4]
        }
        return render(request, 'profile.html', context)

@login_required
@user_passes_test(superuser_required)
def tables(request):
    users_data = User.objects.all().filter(is_verified=True)
    context = {
        'users_data': users_data
    }
    return render(request, 'tables.html', context)

@login_required
def billing(request):
    money = Money.objects.get(id=1)
    users_salaries = sum(UserExtraData.objects.values_list('salary', flat=True))
    context = {
        'money': money,
        'users_salaries': users_salaries
    }
    return render(request, 'billing.html', context)


@login_required
@user_passes_test(superuser_required)
def user_profile(request, id_card):
    user = get_object_or_404(User, id_card=id_card)
    context = {
        'data': user
    }

    return render(request, 'profile.html', context)

@login_required
def verify_user(request, id):
    user = get_object_or_404(User, id=id)
    user.is_verified=True
    user.save()
    return redirect('dashboard')

@login_required
@user_passes_test(superuser_required)
def create_event(request):
    if request.method=='POST':
        form = EventForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = EventForm()
    
    context = {
        'form': form
    }

    return render(request, 'add_event.html', context)

@login_required
def event_detail(request, id):
    data = get_object_or_404(Event, id=id)

    context = {
        'data': data
    }

    return render(request, 'detail_event.html', context)