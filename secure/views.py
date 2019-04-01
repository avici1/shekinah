from django.shortcuts import render, redirect
from secure.models import Access
# Create your views here.


def secure_login(request):
    acc = Access(username=request.POST.get('username'))
    if acc is not None:
        lvl = acc.lvl
        if lvl == 'ceo':
            return redirect('ceo/')
        elif lvl == 'acc':
            return redirect('acc/')
        elif lvl == 'op':
            return redirect('op/')
        elif lvl == 'pr':
            return redirect('pr/')
        elif lvl == 'cc':
            return redirect('cc/')
        else:
            return redirect('login/')

    else:
        return redirect('login/')


def secure_home(request):
    return redirect('accounts/login/')
