from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.shortcuts import render

from exam_project.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'profile/profile-login.html'


class SignUpView(views.CreateView):
    template_name = 'profile/profile-create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('show index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('show index')


class UserDetailsView(views.DetailView):
    template_name = 'profile/profile-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['username'] = self.object.username
        context['email'] = self.object.email
        # context['age'] = self.object.age
        #TODO add age and total price for products

        return context


class UserEditView(views.UpdateView):
    template_name = 'profile/profile-edit.html'
    model = UserModel
    fields = ('username', 'first_name', 'last_name', 'email')

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk
        })


class UserDeleteView(views.DeleteView):
    template_name = 'profile/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('show index')
