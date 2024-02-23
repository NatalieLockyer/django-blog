from django.shortcuts import render

# Create your views here.
def about_me(request):
    """
    Renders the About Page
    """
    about = About.objects.all().order.by('-updated_on').first()

    return render(
        request, 
        "about/about.html",
        {"about": about},
    )
