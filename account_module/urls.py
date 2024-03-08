from django.urls import path ,include
from . import views
urlpatterns = [
    path('profile',views.Profile.as_view(),name='profile'),
    path('signup',views.signup.as_view(),name='sign_up'),
    path('activate-account/<email_active_code>', views.ActivateAccountView.as_view(), name='activate_account'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout_page'),
    path('forget-pass/', views.ForgetPasswordView.as_view(), name='forget_password_page'),
    path('reset-pass/<active_code>', views.ResetPasswordView.as_view(), name='reset_password_page'),
    path('favorit<int:pk>',views.favorit,name='favorite'),
    path('sendemailtoall',views.sendd_email,name='send_email_to_all'),
    
    path('remove_fav<int:pk>',views.remove_fav,name='remove_fav'),
    path('edit-profile/<int:pk>',views.Edit_profilr.as_view(),name='edit_profile'),
 

]