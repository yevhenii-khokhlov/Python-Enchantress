from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View


class LoginView(View):
    def get(self, request):
        return self._login_page(request, context={})

    @staticmethod
    def _login_page(request, context=None):
        context = context or {}

        # if context is None:
        #     context = {}
        return render(request=request, template_name='users/login_form.html', context=context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                # return HttpResponseRedirect(reverse('home:main-page'))
                return HttpResponseRedirect('/home/')
        context = {
            "errors": [
                "Username or password is incorrect"
            ]
        }
        return self._login_page(request, context)


class UpdateUserView(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateUserView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return self._update_page(request=self.request)

    @staticmethod
    def _update_page(request, context=None):
        context = context or {}

        # if context is None:
        #     context = {}
        return render(request=request, template_name='users/profile_update_page.html', context=context)

    def post(self, request):
        user = request.user
        avatar = request.FILES.get('avatar')

        if avatar:
            user.avatar = avatar
            user.save()

        return self._update_page(request=self.request, context={})
