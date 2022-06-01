from django import forms
from .models import Group


class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True)
    group = forms.CharField(max_length=100, required=False)

    def clean_group(self):
        title = self.cleaned_data['group']
        data_is = Group.objects.filter(title=title).exists()

        if not data_is and title != '':
            raise forms.ValidationError('Такой группы нет.')
        return title

    class Meta:
        fields = (
            'text', 'group'
        )
