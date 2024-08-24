from rest_framework.routers import DefaultRouter
from .views import SprintView

router = DefaultRouter()

router.register(r"sprints", SprintView)

urlpatterns = router.urls