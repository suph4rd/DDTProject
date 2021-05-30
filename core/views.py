from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

from DDTProject import settings
from core import forms
from core import models
from core.forms import CustomAuthenticationForm, UnionInteresModelForm


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main_page')
        else:
            return render(request, "core/login.html", locals())
    form = CustomAuthenticationForm(request.POST or None)
    return render(request, "core/login.html", locals())


def get_org_list(request):
    """Достаёт организации по пользователю"""
    return models.User.objects.get(pk=request.user.id).organizationmetod_set.all()


@login_required
def logout_view(request):
    """Выход"""
    logout(request)
    return redirect("login")


@login_required
def main_page(request):
    return render(request, "core/general.html", locals())


@login_required
def udo_view(request):
    queryset = models.Udo.objects.all()
    queryset_count = queryset.count()
    return render(request, "core/udo.html", locals())


@login_required
def staff_view(request):
    form = forms.StaffModelForm()
    if not request.GET.get('type', None):
        return render(request, "core/staff.html", locals())

    form = forms.StaffModelForm(request.GET)
    queryset = models.Staff.objects.filter(type=request.GET['type'])
    if models.StaffCategory.objects.filter(staff__in=queryset.values_list('id', flat=True)).count() < 1:
        return render(request, "core/staff.html", locals())

    name_choice_count = models.Staff.objects.filter(type=request.GET['type']).count()
    form.fields['name'].queryset = models.Staff.objects.filter(type=request.GET['type'])
    name = request.GET['name'] if request.GET.get('name') not in ['', None] else None
    queryset = models.StaffCategory.objects.filter(staff=request.GET['name']) if name else None
    return render(request, "core/staff.html", locals())


@login_required
def create_team_view(request):
    return render(request, "core/create_team.html", locals())


@login_required
def result_participation_view(request):
    return render(request, "core/result_participation.html", locals())


@login_required
def union_interes_view(request):
    form = UnionInteresModelForm()
    if not request.GET.get('type', None):
        return render(request, "core/union_interes.html", locals())

    form = forms.UnionInteresModelForm(request.GET)
    object = models.UnionInteres.objects.filter(type=request.GET['type'], profile=None).last()
    if request.GET.get('type', None) != '2':
        return render(request, "core/union_interes.html", locals())

    profile_choice_count = models.UnionInteresProfile.objects.count()
    form.fields['profile'].queryset = models.UnionInteresProfile.objects.all()
    if request.GET.get('profile'):
        object = models.UnionInteres.objects.filter(type=request.GET.get('profile')).last()
    else:
        object = None
    return render(request, "core/union_interes.html", locals())


@login_required
def info_about_personal_view(request):
    return render(request, "core/info_about_personal.html", locals())


@login_required
def npa_view(request):
    queryset = models.Regulations.objects.all()
    MEDIA_URL = settings.MEDIA_URL
    return render(request, "core/npa.html", locals())


@login_required
def metodic_events_view(request):
    queryset = models.MetodicEvent.objects.all()
    MEDIA_URL = settings.MEDIA_URL
    return render(request, "core/metodic_events.html", locals())


@login_required
def support_platform_view(request):
    return render(request, "core/support_platform.html", locals())


@login_required
def map_view(request):
    district = request.GET.get('district', None)
    district_name = [x[1] for x in models.DISTRICT_CHOICE if str(x[0]) == district]
    district_name = district_name[0] if len(district_name)==1 else None
    if district:
        queryset = models.Udo.objects.filter(district=district)
        queryset_count = queryset.count()
    return render(request, "core/map.html", locals())


@login_required
def list_organization_view(request):
    org_list = get_org_list(request)
    return render(request, "core/user_organizations.html", locals())
