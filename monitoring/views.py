from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from monitoring.forms import UploadFileForm
from monitoring.utils import handle_uploaded_file


class Home(TemplateView):
    template_name = 'home.html'


class Upload(GroupRequiredMixin, FormView):
    group_required = 'User'
    raise_exception = True
    template_name = 'upload.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        handle_uploaded_file(self.request.FILES['file'])
        return super(Upload, self).form_valid(form)

