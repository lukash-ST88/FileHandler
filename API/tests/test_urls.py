from django.urls import reverse, resolve
from ..views import FileListView, upload_file


def test_url_file_list():
    url = reverse('files')
    assert resolve(url).func.view_class == FileListView


def test_upload():
    url = reverse('upload')
    assert resolve(url).func == upload_file
