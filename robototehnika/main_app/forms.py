from django import forms
from .models import Sign, Review


class SignForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields = ['name', 'phone', 'course', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            'course': forms.Select(attrs={
                'class':
                    'form-select'
            }),

            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'rows': 3
            }),
        }

    # Устанавливаем значение по умолчанию для поля "course"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].empty_label = None  # Убираем '--------'
        self.fields['course'].initial = "1"  # или другой ID/значение по умолчанию


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'rating']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш отзыв',
                'rows': 4
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'placeholder': 'Оценка от 1 до 5'
            }),
        }