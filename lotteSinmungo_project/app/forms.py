
from .models import Problem
from django.contrib.auth.models import User
from django import forms


class ProblemForm(forms.ModelForm): # 만들어진 모델로부터 폼을 사용
    class Meta:
        model = Problem
        fields = ('title','body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['body'].label = "불만사항"


        