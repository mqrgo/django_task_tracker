from rest_framework.routers import DefaultRouter

from task_tracker import views

router = DefaultRouter()

app_name = 'tasks'

urlpatterns = []

router.register('', views.Tasks, basename='tasks')

urlpatterns += router.urls
