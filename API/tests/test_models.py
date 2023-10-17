import json


def test_file_create(db, file_factory):
    file = file_factory()
    assert file.id


def test_get_file_as_string(db, file_factory):
    file = file_factory()
    assert type(file.get_file_as_string()) is str
