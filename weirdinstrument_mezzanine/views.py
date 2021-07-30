from django.shortcuts import render

def homeview(request):
    # Get all Posts
    if '127' in request.META['HTTP_HOST']:
        template = 'home.html'
    elif 'liufei-piano-studio.com' in request.META['HTTP_HOST']:
        template =  'pinao_home.html'
    # Render app template with context
    return render(request, template,{'templatename':template})



