from django import forms
from .models import Post


# class PostCreateForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         fields = ('title', 'text', 'categories', )
#         widgets = {
#             'title': forms.TextInput(attrs={'placeholder': "Please, enter a title..."}),
#             'text': forms.Textarea(attrs={'placeholder': "Enter a post's content..."}),
#             'categories': forms.MultipleChoiceField(required=False, to),
#         }
#

class PostListForm(forms.Form):

    sort = forms.ChoiceField(required=False, choices=(
        ('title', 'Title Ac'),
        ('-title', 'Title Dec'),
        ('author', 'Author'),
    ))
    search = forms.CharField(max_length=256, required=False, widget=forms.TextInput)

