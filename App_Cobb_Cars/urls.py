from django.urls import path
from django.contrib.auth.views import LogoutView


from .import views

urlpatterns = [
    path('', views.DealerView.as_view(), name='dealer-view'),
    path('dealer-detail/<int:pk>/', views.DealerDetail.as_view(), name="dealer-detail"),
    path('dealer-create', views.DealerCreate.as_view(), name="dealer-create"),
    path('dealer-update/<int:pk>/', views.DealerUpdate.as_view(), name='dealer-update'),
    path('dealer-delete/<int:pk>/', views.DealerDelete.as_view(), name='dealer-delete'),
    path('dealer-login/', views.DealerLogin.as_view(), name='dealer-login'),
    path('logout/',  LogoutView.as_view(next_page = 'dealer-login'), name='logout')
]