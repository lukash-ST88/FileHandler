import pytest
from django.urls import reverse
import factory
from ..serializers import FileSerializer
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_get_files_request(api_client, file_factory):
    url = reverse('files')
    response = api_client.get(url)
    print(FileSerializer(file_factory()).data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_file_upload(api_client):
    url = reverse('upload')
    response = api_client.post(url, data={'file': SimpleUploadedFile('some_file.txt', b'file content')},
                               format='multipart')
    assert response.status_code == 201


@pytest.mark.django_db
def test_post_file_upload_error(api_client):
    url = reverse('upload')
    response = api_client.post(url, data={'file': 'not_file'},
                               format='multipart')
    assert response.status_code == 400
