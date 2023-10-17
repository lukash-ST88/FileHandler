import factory
from ..models import File


class FileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = File

    file = factory.django.FileField(filename='test_filefield')
