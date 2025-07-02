from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo # 모델 지정
        fields = ['title', 'due_date'] # 필드 지정
        widgets = { # 입력 필드 지정
            'title': forms.TextInput(attrs={
                'class': 'input-box'
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'input-box'
            })
        }

