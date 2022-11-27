from django.shortcuts import render
from .models import Style
from .forms import StyleForm


# Create your views here.


def my_form(request):
    all_data = Style.objects.all()
    context ={
        'style': all_data
    }
    if request.method == "POST":
        module_id = request.POST.get('module,id',False)
        title = request.POST['title']
        instructor = request.POST['instructor']
        module_course = request.POST['course']
        type = request.POST['type']
        description = request.POST['description']

        new_data = Style(module_id = module_id, title=title,instructor=instructor,module_course=module_course,type = type,description = description)
        new_data.save()

    return render(request, 'cstyle.html', context)
