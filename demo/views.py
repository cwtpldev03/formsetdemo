from django.shortcuts import render, redirect
from django.views import generic
from .forms import PressureForm, PressureFormset
from .models import PressureFormat
# Create your views here.
def create_book_model_form(request):
    template_name = 'create_normal.html'
    heading_message = 'Model Formset Demo'
    if request.method == 'GET':
        formset = PressureFormset(queryset=PressureFormat.objects.none())
    elif request.method == 'POST':
        formset = PressureFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # only save if name is present
                if form.cleaned_data.get('name'):
                    form.save()
            return redirect('list')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })

class PressureListView(generic.ListView):
    model = PressureFormat
    context_object_name = 'pressure'
    template_name = 'list.html'

