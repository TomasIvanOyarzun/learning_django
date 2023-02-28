from django.urls import path
from .views import about,hello,hello_with_params,get_all_projects,get_tasks_id,get_all_tasks,get_all_tasks_render,get_all_projects_render,create_tasks


urlpatterns = [
 
    path('', hello),
    path('hello/<str:name>', hello_with_params),
    path('about/', about ),
    path('projects/', get_all_projects),
    path('projects/render/', get_all_projects_render),
    path('tasks/<int:id>', get_tasks_id),
    path('tasks/', get_all_tasks),
    path('tasks/render/', get_all_tasks_render),
    path('task/create', create_tasks )
]