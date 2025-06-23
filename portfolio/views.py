from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Project, Skill, Experience, Education#, Contact
from .forms import ContactForm

def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()
    recent_experience = Experience.objects.first()
    
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
        'recent_experience': recent_experience,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    
    context = {
        'skills': skills,
        'experiences': experiences,
        'education': education,
    }
    return render(request, 'portfolio/about.html', context)

def projects(request):
    project_list = Project.objects.all()
    search_query = request.GET.get('search')
    
    if search_query:
        project_list = project_list.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(technologies__name__icontains=search_query)
        ).distinct()
    
    paginator = Paginator(project_list, 6)
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    
    context = {
        'projects': projects,
        'search_query': search_query,
    }
    return render(request, 'portfolio/projects.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    related_projects = Project.objects.filter(
        technologies__in=project.technologies.all()
    ).exclude(pk=project.pk).distinct()[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            return redirect('portfolio:contact')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'portfolio/contact.html', context)