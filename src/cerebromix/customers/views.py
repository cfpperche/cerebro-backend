# coding: utf-8
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.utils.translation import ugettext as _

from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

from cerebromix.customers.forms import LoginForm


class SignInView(View):
    template_name = 'customers/signin.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class SignUpView(TemplateView):
    template_name = 'plans/pricing.html'


def entrar(request):
  
    
    if request.user.is_anonymous():
        next = request.REQUEST.get('next', '/plan/account')
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return HttpResponseRedirect(next)
        else:
            form = LoginForm()
        return render(request, 'customers/signin.html',
            {
                'form': form,
                'next': next,
            }
        )
    else:
        return HttpResponseRedirect(reverse('plans:current_plan'))
        


def sair(request):
    logout(request)
    return HttpResponseRedirect(reverse('customers:signin'))


@login_required
def view_protegida(request):
    return HttpResponse('View protegida!')


@permission_required('aula5.add_categoria')
def view_protegida2(request):
    return HttpResponse('View protegida2!')
