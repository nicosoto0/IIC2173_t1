from django.urls import path
from . import views
# the . means that it will look in the seam directory

urlpatterns = [
    # /chat/
    path('', views.IndexView.as_view(), name='index'),

    # chat/[id_message]/
    path('<int:pk>/',views.DetailView.as_view(), name = "msg_detail" ),

    # chat/add_msg/
    path('add_msg/', views.MessageCreate.as_view(), name="message-add"),
]
