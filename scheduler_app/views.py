from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import Schedule
from PIL import Image
from PIL.ExifTags import TAGS


def extract_tiff_image_data(image_path):
    try:
        # Open the TIFF image using PIL
        image = Image.open(image_path)

        metadata = {}
        for tag, value in image.tag.items():
            tag_name = TAGS.get(tag)
            metadata[tag_name] = value

        return metadata

    except Exception as e:
        print(f"Error: {e}")
        return None
    


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        image_path = request.FILES.get('image')
        schedule = Schedule.objects.create(title=title, description=description,image=image_path,
                                       start_time=start_time, end_time=end_time)
        schedule.save()
        return redirect('view_tasks')
    return render(request, 'add_task.html')


def view_tasks(request):
    schedules = Schedule.objects.all()
    context = {
        'schedules': schedules
    }
    return render(request, 'schedules.html', context)



def schedule_detail(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    image = schedule.image
    title = schedule.title
    description = schedule.description
    start_time = schedule.start_time
    end_time =  schedule.end_time
    remaining_days = schedule.days_remaining()
    tiff_image_details = extract_tiff_image_data(image)
   

    context = {
        'title': title,
        'description': description,
        'start_time': start_time,
        'end_time': end_time,
        'schedule':schedule,
        'remaining_days':remaining_days,
        'tiff_image_details': tiff_image_details,
        'schedule': schedule

    }
    return render(request, 'schedule_details.html', context)



class ScheduleUpdateView(UpdateView):
    model = Schedule
    template_name = 'update_schedule.html'
    fields = ('title', 'description', 'start_time', 'end_time')
    success_url = reverse_lazy('view_tasks')


class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'delete_schedule.html'
    success_url = reverse_lazy('view_tasks')
