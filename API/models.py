from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='FileHandler/files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def get_file_as_string(self):
        return str(self.file)
