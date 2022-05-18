from django.contrib import admin
from django.urls import path
from hp import views as hp_1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('json/', hp_1.v1, name = 'json'),
    path('detail/<int:pk>/',hp_1.v1_details, name ='detail'),
    path()
]

# from django.urls import include, path
# from rest_framework import routers
# from hp import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]