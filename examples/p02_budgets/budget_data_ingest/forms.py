from django import forms
from data_ingest.forms import UploadForm


DEFAULT_FILE_EXTENSIONS = (".xlsx", ".xls", ".csv")


class UploadForm(UploadForm):
    agency = forms.CharField(max_length=40)
    year = forms.IntegerField()
    data_source = forms.CharField(max_length=40)
