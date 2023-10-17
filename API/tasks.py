from celery import shared_task
from .models import File


class Containers:
    video = ['.mov', '.mp4', '.avi']
    image = ['.png', '.jpg']
    audio = ['.mp3', '.avc']
    text = ['.xlsx', '.txt', '.doc', '.docx', '.pdf']


@shared_task()
def handle_file(file_id):
    file = File.objects.get(id=file_id)
    file_as_string = file.get_file_as_string()
    index_of_container_in_string = file_as_string.rfind('.')
    file_container = file_as_string[index_of_container_in_string:]
    if file_container in Containers.video:
        response = 'Handling video..'
        print(response)
        file.processed = True
        file.save()
        return response
    elif file_container in Containers.audio:
        response = 'Handling audio..'
        print(response)
        file.processed = True
        file.save()
        return response
    elif file_container in Containers.image:
        response = 'Handling image..'
        print(response)
        file.processed = True
        file.save()
        return response
    elif file_container in Containers.text:
        response = 'Handling text..'
        print(response)
        file.processed = True
        file.save()
        return response
    else:
        response = 'Handling some file..'
        print(response)
        file.processed = True
        file.save()
        return response
