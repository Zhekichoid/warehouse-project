from django.urls import path


from . import views

app_name = "products"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('import/', views.import_from_excel, name='import_from_excel'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
]