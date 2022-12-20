from django.urls import path
from .views import one, two, three, ClassEndpointView, get_obj_by_id


urlpatterns = [
    path('one/', one),
    path('two/', two),
    path('three/', three),
    path('class/', ClassEndpointView.as_view()),
    path('object/<int:obj_id>/', get_obj_by_id),
]