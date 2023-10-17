from django.urls import path
from .views import upload_file, FileListView


urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('files/', FileListView.as_view(), name='files'),
]
