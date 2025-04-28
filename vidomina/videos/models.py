from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class IpAddress(models.Model):
    ip = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    title = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
    
class PublishedManager(models.Manager):    
    def get_queryset(self):        
        return super().get_queryset().filter(status=Video.Status.PUBLISHED) #status field must be set to PUBLISHED too
    
class DraftManager(models.Manager):    
    def get_queryset(self):        
        return super().get_queryset().filter(status=Video.Status.DRAFT)
    
class Video(models.Model):
    class Status(models.TextChoices):    #the status we have choices we can select from among Draft, Published, Pending. That is what TextChoices does like Drop down list box in html 
        DRAFT = 'DF', 'Draft'    
        PUBLISHED = 'PB', 'Published'
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250) 
    video = models.FileField(upload_to='videos')
    poster = models.ImageField(upload_to='posters')
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='video_posts' )
    publish = models.DateTimeField(default=timezone.now)  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    likes = models.ManyToManyField(User, related_name='video_likes', blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', 
                                        related_query_name='hit_count_generic_relation')
    
    objects = models.Manager() # The default manager. 
    published = PublishedManager() # Our custom manager.  
    draft = DraftManager() 

    class Meta:
        ordering = ['-publish'] #Last(newest) published to be at the top.
        indexes = [        
                models.Index(fields=['-publish']),        
                      ]
    def __str__(self):       
         return self.title
    
    def get_absolute_url(self):
        return reverse('videos:post_detail',
                       args=[self.publish.year,                             
                              self.publish.month,                             
                              self.publish.day,                             
                              self.slug])
    
    def get_comments(self):
        return self.video_comments.filter(video_parent=None).filter(active=True)
                              
                              
class Comments(models.Model):    
    video = models.ForeignKey(Video,                            
                             on_delete=models.CASCADE,                             
                             related_name='video_comments',) 
    
    name = models.ForeignKey(User,  on_delete=models.CASCADE,            
                                related_name='user_comments' )    
    email = models.EmailField()    
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)    
    active = models.BooleanField(default=True)
    video_parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="comment_replies", null=True, blank=True)
    edited = models.BooleanField(default=False)
    edited_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_video_comment', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_video_comment', blank=True)
    #section_name = models.CharField(max_length=50, default='Politics', editable=False)
    
    class Meta:        
        ordering = ['created']        
        indexes = [            
            models.Index(fields=['created']),       
              ]
    def __str__(self):        
        return f'Comment by {self.name} on {self.video}'
    
    def get_comments(self):
        return Comments.objects.filter(video_parent=self).filter(active=True)
