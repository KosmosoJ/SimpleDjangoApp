from .form import Signup
from .models import SocialMedia

def footer_info(request):
    form = Signup()
    socials = SocialMedia.objects.all()
    return {'signup':form, 'socials':socials}