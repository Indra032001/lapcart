from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
                  path('show/', views.show_view),
                  path('add/', views.add_view),
                  path('update/<i>/', views.update_view),
                  path('delete/<i>/', views.delete_view),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
