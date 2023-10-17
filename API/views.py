from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .tasks import handle_file
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import File


@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            file_id = serializer.instance.id
            handle_file.delay(file_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(generics.ListAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
