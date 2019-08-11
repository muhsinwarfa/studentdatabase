
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new',views.create, name='new'),
    path('delete/<int:id>',views.delete_record, name='delete'),
    path('edit/<int:id>', views.update_record, name='edit'),
    path('view/<int:id>', views.view_record, name='view'),

]