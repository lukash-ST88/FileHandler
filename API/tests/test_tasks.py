import pytest
import factory
from ..tasks import handle_file


@pytest.mark.parametrize('container,Handler',
                         [('.txt', 'Handling text..'), ('.mp3', 'Handling audio..'),
                          ('.mov', 'Handling video..'),
                          ('.png', 'Handling image..'), ('.bat', 'Handling some file..')])
def test_task_file_handler(db, file_factory, container, Handler):
    file = file_factory(file=factory.django.FileField(filename=f'test_filefield{container}'))
    response = handle_file.apply(args=(file.id,)).get()
    assert response == Handler
