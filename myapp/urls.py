from django.urls import path
from .views import about,hello,hello_with_params,get_all_projects,get_tasks_id,get_all_tasks


urlpatterns = [
 
    path('', hello),
    path('hello/<str:name>', hello_with_params),
    path('about/', about ),
    path('projects/', get_all_projects),
    path('tasks/<int:id>', get_tasks_id),
    path('tasks/', get_all_tasks),
]