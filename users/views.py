from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from .forms import UserSignUpForm, UpdateProfile
from django.contrib.auth.decorators import login_required
from .forms import UserExtraDataForm
from .models import UserExtraData, Job, User

def sign_out(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            user = authenticate(id_card=form.cleaned_data.get('id_card'), password=form.cleaned_data.get('password1'))
            if user is not None:
                login(request, user)
                return redirect('dashboard') 
        else:
            print(form.errors)

    else:
        form = UserSignUpForm()

    return render(request, 'registration/sign-up.html', {'form': form})


@login_required
def profile_update(request, id):
    user_profile = get_object_or_404(User, id=id)
    updating_profile = get_object_or_404(UserExtraData, user=user_profile)
    if request.method=='POST' and user_profile.id==request.user.id:
        form = UpdateProfile(request.POST or None, instance=updating_profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = UpdateProfile(instance=updating_profile)
    
    context = {
            'form': form,
            'data': updating_profile
        }
    
    return render(request, 'profile_update.html', context)

@login_required
def filling_info(request):
    if request.method=='POST':
        form = UserExtraDataForm(request.POST or None)
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.user = request.user
            user_data.save()
            return redirect('filling_info')
        else:
            print(form.errors)
    else:
        if UserExtraData.objects.filter(user=request.user).exists():
            can_update = False
        else:
            can_update = True
        form = UserExtraDataForm()

    if UserExtraData.objects.filter(user=request.user).exists():
        can_update = False
    else:
        can_update = True
    
    return render(request, 'filling_info.html', context={'can_update': can_update, 'job_list': Job.objects.all()})