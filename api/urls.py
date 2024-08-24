from .auth.urls import urlpatterns as auth_urls
from .users.urls import urlpatterns as user_urls
from .projects.urls import urlpatterns as project_urls

urlpatterns = [] + auth_urls + user_urls + project_urls