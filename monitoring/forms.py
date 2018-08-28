from mimetypes import guess_type

from django import forms

CONTENT_TYPES = [
    'text/plain',
    'text/richtext',
    'application/rtf',
    'image/jpeg',
    'image/png',
    'image/gif',
    'application/msword',
    'application/excel',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
]


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        data = self.cleaned_data['file']

        mimetype, encoding = guess_type(data.name)
        if mimetype not in CONTENT_TYPES:
            raise forms.ValidationError("This file extension is not supported")

        return data
