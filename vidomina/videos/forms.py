from django import forms
from .models import Video, Comments

class CommentForm(forms.ModelForm):  
    class Meta:        
        model = Comments    
        fields = [ 'body']
        labels = {
          'body': 'Body'}
        widgets = {
          'body' : forms.widgets.Textarea(attrs={'class': 'bg-gray-50 border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-grey-400 dark-white', 'placeholder':'Drop a comment',
                                                             'cols': 30, 'rows': 5})
                  }