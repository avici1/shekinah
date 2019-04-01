from django.shortcuts import render

# Create your views here.


def cc_agent_view(request):
    return render(request, 'cc_agent_temp.html')


def accountant_view(request):
    return render(request, 'account_view.html')


def operator_view(request):
    return render(request, 'operator_view.html')


def ceo_view(request):
    return render(request, 'ceo_view.html')


def production_manager_view(request):
    return render(request, 'production_manager_view.html')


def login_view(request):
    return render(request, 'registration/login.html')
