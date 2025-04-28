from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, IpAddress, Video, Comments
from .forms import CommentForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from hitcount.views import HitCountMixin
from hitcount.utils import get_hitcount_model
import datetime
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# Create your views here.
#animation home
def animation_home(request):
   animation_videos = all_animation_videos(request)
   return render(request, 'video/animationList.html', {'animation_videos':animation_videos})

def all_animation_video_view(request):
   animation_videos = all_animation_videos(request)
   context = {'animation_videos':animation_videos}
   return render(request, "video/partials/videohome/animation.html", context)

def all_animation_videos(request):
   objs = Video.objects.filter(category__title = 'Animations', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#animation home ends here


#artistic home
def artistic_home(request):
   artistic_videos = all_artistic_videos(request)
   return render(request, 'video/artisticList.html', {'artistic_videos':artistic_videos})

def all_artistic_video_view(request):
   artistic_videos = all_artistic_videos(request)
   context = {'artistic_videos':artistic_videos}
   return render(request, "video/partials/videohome/artistic.html", context)

def all_artistic_videos(request):
   objs = Video.objects.filter(category__title = 'Artistic', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#artistic home ends here




#sport home
def sport_home(request):
   sport_videos = all_sport_videos(request)
   return render(request, 'video/sportList.html', {'sport_videos':sport_videos})

def all_sport_video_view(request):
   sport_videos = all_sport_videos(request)
   context = {'sport_videos':sport_videos}
   return render(request, "video/partials/videohome/sport.html", context)

def all_sport_videos(request):
   objs = Video.objects.filter(category__title = 'Sport', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#sport home ends here


#comic home
def comic_home(request):
   comic_videos = all_comic_videos(request)
   return render(request, 'video/comicList.html', {'comic_videos':comic_videos})

def all_comic_video_view(request):
   comic_videos = all_comic_videos(request)
   context = {'comic_videos':comic_videos}
   return render(request, "video/partials/videohome/comic.html", context)

def all_comic_videos(request):
   objs = Video.objects.filter(category__title = 'Comic Videos', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#comic home ends here



#crime home
def crime_home(request):
   crime_videos = all_crime_videos(request)
   return render(request, 'video/crimeList.html', {'crime_videos':crime_videos})

def all_crime_video_view(request):
   crime_videos = all_crime_videos(request)
   context = {'crime_videos':crime_videos}
   return render(request, "video/partials/videohome/crime.html", context)

def all_crime_videos(request):
   objs = Video.objects.filter(category__title = 'Crime Videos', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#crime home ends here

#discovery home
def discovery_home(request):
   discovery_videos = all_discovery_videos(request)
   return render(request, 'video/discoveryList.html', {'discovery_videos':discovery_videos})

def all_discovery_video_view(request):
   discovery_videos = all_discovery_videos(request)
   context = {'discovery_videos':discovery_videos}
   return render(request, "video/partials/videohome/discovery.html", context)

def all_discovery_videos(request):
   objs = Video.objects.filter(category__title = 'Discovery', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#discovery home ends here


#documentary home
def documentary_home(request):
   documentary_videos = all_documentary_videos(request)
   return render(request, 'video/documentaryList.html', {'documentary_videos':documentary_videos})

def all_documentary_video_view(request):
   documentary_videos = all_documentary_videos(request)
   context = {'documentary_videos':documentary_videos}
   return render(request, "video/partials/videohome/documentary.html", context)

def all_documentary_videos(request):
   objs = Video.objects.filter(category__title = 'Documentary', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#documentary home ends here



#happening home
def happening_home(request):
   happening_videos = all_happening_videos(request)
   return render(request, 'video/happeningList.html', {'happening_videos':happening_videos})

def all_happening_video_view(request):
   happening_videos = all_happening_videos(request)
   context = {'happening_videos':happening_videos}
   return render(request, "video/partials/videohome/happening.html", context)

def all_happening_videos(request):
   objs = Video.objects.filter(category__title = 'Happening', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#happening home ends here

#howto home
def howto_home(request):
   howto_videos = all_howto_videos(request)
   return render(request, 'video/howtoList.html', {'howto_videos':howto_videos})

def all_howto_video_view(request):
   howto_videos = all_howto_videos(request)
   context = {'howto_videos':howto_videos}
   return render(request, "video/partials/videohome/howto.html", context)

def all_howto_videos(request):
   objs = Video.objects.filter(category__title = 'Howto', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#howto home ends here

#leadership home
def leadership_home(request):
   leadership_videos = all_leadership_videos(request)
   return render(request, 'video/leadershipList.html', {'leadership_videos':leadership_videos})

def all_leadership_video_view(request):
   leadership_videos = all_leadership_videos(request)
   context = {'leadership_videos':leadership_videos}
   return render(request, "video/partials/videohome/leadership.html", context)

def all_leadership_videos(request):
   objs = Video.objects.filter(category__title = 'Leadership and Motivation', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#leadership home ends here

#movies home
def movies_home(request):
   movies_videos = all_movies_videos(request)
   return render(request, 'video/moviesList.html', {'movies_videos':movies_videos})

def all_movies_video_view(request):
   movies_videos = all_movies_videos(request)
   context = {'movies_videos':movies_videos}
   return render(request, "video/partials/videohome/movies.html", context)

def all_movies_videos(request):
   objs = Video.objects.filter(category__title = 'Movies', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#movies home ends here

#music home
def music_home(request):
   music_videos = all_music_videos(request)
   return render(request, 'video/musicList.html', {'music_videos':music_videos})

def all_music_video_view(request):
   music_videos = all_music_videos(request)
   context = {'music_videos':music_videos}
   return render(request, "video/partials/videohome/music.html", context)

def all_music_videos(request):
   objs = Video.objects.filter(category__title = 'Music', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#music home ends here

#people home
def people_home(request):
   people_videos = all_people_videos(request)
   return render(request, 'video/peopleList.html', {'people_videos':people_videos})

def all_people_video_view(request):
   people_videos = all_people_videos(request)
   context = {'people_videos':people_videos}
   return render(request, "video/partials/videohome/people.html", context)

def all_people_videos(request):
   objs = Video.objects.filter(category__title = 'People and Event', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#people home ends here

#animal home
def animal_home(request):
   animal_videos = all_animal_videos(request)
   return render(request, 'video/animalList.html', {'animal_videos':animal_videos})

def all_animal_video_view(request):
   animal_videos = all_animal_videos(request)
   context = {'animal_videos':animal_videos}
   return render(request, "video/partials/videohome/animal.html", context)

def all_animal_videos(request):
   objs = Video.objects.filter(category__title = 'Pets and WildLife', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#animal home ends here

#politics home
def politics_home(request):
   politics_videos = all_politics_videos(request)
   return render(request, 'video/politicsList.html', {'politics_videos':politics_videos})

def all_politics_video_view(request):
   politics_videos = all_politics_videos(request)
   context = {'politics_videos':politics_videos}
   return render(request, "video/partials/videohome/politics.html", context)

def all_politics_videos(request):
   objs = Video.objects.filter(category__title = 'Politics and Politician', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#politics home ends here

#properties home
def properties_home(request):
   properties_videos = all_properties_videos(request)
   return render(request, 'video/propertiesList.html', {'properties_videos':properties_videos})

def all_properties_video_view(request):
   properties_videos = all_properties_videos(request)
   context = {'properties_videos':properties_videos}
   return render(request, "video/partials/videohome/properties.html", context)

def all_properties_videos(request):
   objs = Video.objects.filter(category__title = 'Properties', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#properties home ends here

#religion home
def religion_home(request):
   religion_videos = all_religion_videos(request)
   return render(request, 'video/religionList.html', {'religion_videos':religion_videos})

def all_religion_video_view(request):
   religion_videos = all_religion_videos(request)
   context = {'religion_videos':religion_videos}
   return render(request, "video/partials/videohome/religion.html", context)

def all_religion_videos(request):
   objs = Video.objects.filter(category__title = 'Religion', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#religion home ends here

#stem home
def stem_home(request):
   stem_videos = all_stem_videos(request)
   return render(request, 'video/stemList.html', {'stem_videos':stem_videos})

def all_stem_video_view(request):
   stem_videos = all_stem_videos(request)
   context = {'stem_videos':stem_videos}
   return render(request, "video/partials/videohome/stem.html", context)

def all_stem_videos(request):
   objs = Video.objects.filter(category__title = 'STEM', status=Video.Status.PUBLISHED).all()
   page_number = request.GET.get('page', 1)
   paginator = Paginator(objs, per_page=10)
   page_objects_home = paginator.get_page(page_number)
   return page_objects_home
#stem home ends here


def Video_details(request, year, month, day, video):
    video = get_object_or_404(Video, 
                              status=Video.Status.PUBLISHED,
                              slug=video,
                              publish__year=year,
                              publish__month=month,
                              publish__day=day)
    category = video.category.title
    most_viewed = Video.objects.filter(status=Video.Status.PUBLISHED).order_by( 'hit_count_generic')[:10]
    
    comments = video.video_comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        form = CommentForm(data=request.POST)
        if form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = form.save(commit=False)
            # Assign the current post to the comment
            new_comment.video = video

            # Assign commenter name
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
            # redirect to same page and focus on that comment
            return redirect(video.get_absolute_url()+'#'+str(new_comment.id))
    else:
        form = CommentForm()
    
    #let's paginate our comment to 10 comments per post
    paginator= Paginator(comments, 10) #10 posts per page
    page_number= request.GET.get('page', 1)
     
    try:
       all_comments= paginator.page(page_number)
    except PageNotAnInteger:
       all_comments= paginator.page(1)
    except EmptyPage:
       all_comments = paginator.page(paginator.num_pages) 
       
  
    
    context = {'video':video,
               'most_viewed': most_viewed,
               'category':category,
               'comments' : comments,
               'all_comments' : all_comments,
               'form' : form,}
    #hitcount logic
    hit_count = get_hitcount_model().objects.get_for_object(video)
    hits = hit_count.hits
    hitContext = context['hitcount'] = {'pk':hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
       hits = hits + 1
       hitContext['hit_counted'] = hit_count_response.hit_counted
       hitContext['hit_message'] = hit_count_response.hit_message
       hitContext['total_hits'] = hits

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        IpAddress.objects.get(ip=ip)
    except IpAddress.DoesNotExist:
        ip = IpAddress(ip=ip, created=datetime.datetime.now())
        ip.save()
    
    return render(request, 'video/details.html', context)
    
    

def video_likes(request, pk):
    video = Video.objects.get(pk=pk)
    if request.method =='POST':
        if not video.likes.filter(id=request.user.pk).exists():
            video.likes.add( request.user)
            video.save()
            return render(request, 'video/partials/like.html', context={'video':video})
        else:
            video.likes.remove(request.user)
            video.save()
            return render(request, 'video/partials/like.html', context={'video':video})
    else:
       return render(request, 'video/partials/like.html', context={'video':video})
    
     
@login_required
def post_comment(request, post_id):    
  video = get_object_or_404(Video, id=post_id, status=Video.Status.PUBLISHED)    
  comment = None    
  # A comment was posted    
  form = CommentForm(data=request.POST)
  if form.is_valid():        
     # Create a Comment object without saving it to the database        
     comment = form.save(commit=False)        
     # Assign the post to the comment        
     comment.video = video
     comment.name = request.user         
     # Save the comment to the database        
     comment.save() 
     return redirect(video.get_absolute_url()+'#'+str(comment.id))
      
  return render(request , 'comment/comment_confirm.html',                           
                {'video': video,                            
                 'form': form,                            
                 'comment': comment})
                 
                 
class Like_comment(LoginRequiredMixin, View):
   def post(self, request, post_pk=None, pk=None, *args, **kwargs):
      post = Video.objects.get(pk=post_pk)
      comment = Comments.objects.get(pk=pk)
      if request.method=="POST":
          is_dislike = False
          for dislike in comment.dislikes.all():
            if dislike ==request.user:
                is_dislike = True
                break
          if is_dislike:
             comment.dislikes.remove(request.user)
             
        

          is_like = False
          for like in comment.likes.all():
            if like == request.user:
               is_like = True
               break
          if not is_like:
             comment.likes.add(request.user)
             
             return render(request,'comment/partials/like.html', context={'comment':comment, 'post':post})
          if is_like:
             comment.likes.remove(request.user)
             return render(request,'comment/partials/like.html', context={'comment':comment, 'post':post})
      else:
         return render(request,'comment/partials/like.html', context={'comment':comment, 'post':post})


def Update_Comment(request, pk=None):
   comment = Comments.objects.get(pk=pk)
   comment.edited = False
   next  = request.POST.get('next', '/')
   if request.method == 'POST':
      
      form = CommentForm(request.POST,  instance=comment)
      if form.is_valid():
         comment.edited = True
         form.save()
         comment.edited = True
         messages.success(request, 'Your Comment Updated Successuflly')
         return HttpResponseRedirect(next)
         #return redirect('blog:my_page')
         
   else:
      form = CommentForm(instance=comment)
   

   return render(request, 'comment/partials/comment_edit_form.html',
                   { 'form':form,
                   'comment':comment,
 })
 
 
# handling reply, reply view
def reply_page(request):
    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():
            post_id = request.POST.get('post_id')  # from hidden input
            print(post_id)
            parent_id = request.POST.get('parent')  # from hidden input
            post_url = request.POST.get('post_url')  # from hidden input

            reply = form.save(commit=False)
    
            reply.video = Video(id=post_id)
            reply.video_parent = Comments(id=parent_id)
            comment = Comments.objects.get(id=parent_id)
             # Assign reply to the login user
            reply.name = request.user
            reply.save()
            return redirect(post_url + '#' + str(reply.id))

    return redirect("/")