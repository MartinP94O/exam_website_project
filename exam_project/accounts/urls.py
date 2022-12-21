from django.urls import path, include

from exam_project.accounts.views import SignInView, SignUpView, SignOutView, UserDetailsView, UserEditView, \
    UserDeleteView


urlpatterns = (
    path('create/', SignUpView.as_view(), name='create profile'),
    path('login/', SignInView.as_view(), name='login profile'),
    path('logout/', SignOutView.as_view(), name='logout profile'),
    path('<int:pk>/', include([
        path('details/', UserDetailsView.as_view(), name='profile details'),
        path('edit/', UserEditView.as_view(), name='profile edit'),
        path('delete/', UserDeleteView.as_view(), name='delete profile'),
    ])),
)
