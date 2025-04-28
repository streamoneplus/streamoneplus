from django.shortcuts import render
from videos.models import Video

# Create your views here.

def Index(request):
    animation = Video.objects.filter(category__title = 'Animations', status=Video.Status.PUBLISHED).all()[:10]
    artistic = Video.objects.filter(category__title = 'Artistic', status=Video.Status.PUBLISHED).all()[:10]
    comic = Video.objects.filter(category__title = 'Comic Videos', status=Video.Status.PUBLISHED).all()[:10]
    crime = Video.objects.filter(category__title = 'Crime Videos', status=Video.Status.PUBLISHED).all()[:10]
    discovery = Video.objects.filter(category__title = 'Discovery', status=Video.Status.PUBLISHED).all()[:10]
    documentary = Video.objects.filter(category__title = 'Documentary', status=Video.Status.PUBLISHED).all()[:10]
    happening = Video.objects.filter(category__title = 'Happening', status=Video.Status.PUBLISHED).all()[:10]
    howto = Video.objects.filter(category__title = 'Howto', status=Video.Status.PUBLISHED).all()[:10]
    leadership = Video.objects.filter(category__title = 'Leadership and Motivation', status=Video.Status.PUBLISHED).all()[:10]
    movies = Video.objects.filter(category__title = 'Movies', status=Video.Status.PUBLISHED).all()[:10]
    music = Video.objects.filter(category__title = 'Music', status=Video.Status.PUBLISHED).all()[:10]
    event = Video.objects.filter(category__title = 'People and Event', status=Video.Status.PUBLISHED).all()[:10]
    animal = Video.objects.filter(category__title = 'Pets and WildLife', status=Video.Status.PUBLISHED).all()[:10]
    politics = Video.objects.filter(category__title = 'Politics and Politician', status=Video.Status.PUBLISHED).all()[:10]
    property = Video.objects.filter(category__title = 'Properties', status=Video.Status.PUBLISHED).all()[:10]
    religion = Video.objects.filter(category__title = 'Religion', status=Video.Status.PUBLISHED).all()[:10]
    stem = Video.objects.filter(category__title = 'STEM', status=Video.Status.PUBLISHED).all()[:10]
    sport = Video.objects.filter(category__title = 'Sport', status=Video.Status.PUBLISHED).all()[:10]
    
    context = {
        'animation':animation,
        'artistic':artistic,
        'comic':comic,
        'crime':crime,
        'discovery':discovery,
        'documentary':documentary,
        'happening':happening,
        'howt':howto,
        'leadership':leadership,
        'movies':movies,
        'music':music,
        'event':event,
        'animal':animal,
        'politics':politics,
        'property':property,
        'religion':religion,
        'stem':stem,
        'sport':sport
    }
    return render(request, 'homepage/index.html', context)


def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')