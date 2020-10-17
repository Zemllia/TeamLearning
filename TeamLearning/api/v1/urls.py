from django.conf.urls import url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from TeamLearning.api.v1 import views as main_views
from rest_framework.authtoken import views

router = routers.SimpleRouter()
# router.register(r'user', main_views.UserViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="TeamLearning API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

api_urlpatterns = router.urls + [
    url(r'^auth/', views.obtain_auth_token),
    path(
        'documentation/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
