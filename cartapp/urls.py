from django.urls import path
from django.contrib.auth import views as auth_views
from cartapp.views import signin,signup,category,products,detail,order,return_view,cancel_view,cart_view,contact,otp,logout,review,home
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
app_name='cartapp'

urlpatterns=[
    path('category',category,name='category'),
    path('s/',signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('logout/', logout, name='logout'),
    path('products/<int:product_id>/<slug:slug>/',products, name='products'),
    path('<int:product_id>/<slug:slug>',detail,name='detail'),
    path('detail/',detail,name='detail'),
    path('cart/',cart_view,name='cart_view'),
    path('order/',order,name='order'),
    path('success/',return_view,name='return_view'),
    path('cancel/',cancel_view,name='cancel_view'),
    path('otp/<str:otp>/<str:username>/<str:password>/<str:email>/',otp, name='otp'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('contact/',contact,name='contact'),
    path('<int:product_id>/<slug:slug>/review/',review, name='review'),
    path('',home,name='home'),
    
]





