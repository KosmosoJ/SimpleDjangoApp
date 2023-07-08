from .models import Project, Service

def navbar(request):
    projects = Project.objects.all()
    services = Service.objects.all()
    return {'projects':projects, 'services':services}