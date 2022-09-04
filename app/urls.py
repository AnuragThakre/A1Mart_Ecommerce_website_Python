import statistics
from django.conf import settings
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    # path('', views.home),
    path('',views.ProductView.as_view(),name="home"),   #This is class based view remaining all are function based view 
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('mobile/', views.mobile, name='mobile'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('laptop/', views.laptop, name='laptop'),
    path('accounts/login',auth_views.LoginView.as_view
    (template_name='app/login.html', authentication_form=LoginForm),
    name='login'),
    
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    
    path('passwordchange/',auth_views.PasswordChangeView.as_view
    (template_name='app/passwordchange.html',form_class=MyPasswordChangeForm,
    success_url='/passwordchangedone/'), name='passwordchange'),
    
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view
    (template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    
    path('checkout/', views.checkout, name='checkout'),
    
    path('password-reset/',auth_views.PasswordResetView.as_view
    (template_name='app/passwordreset.html', form_class=MyPasswordResetForm),
    name='password_reset'),
    
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view
    (template_name='app/passwordresetdone.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view
    (template_name='app/passwordresetcofirm.html', form_class=MySetPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view
    (template_name='app/passwordresetcomplete.html'),name='password_reset_complete'),
    
    path('checkout/', views.checkout, name='checkout'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
