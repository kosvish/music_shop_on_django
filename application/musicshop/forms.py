from django import forms
from django.contrib.auth import get_user_model
from .models import Order, Genre, MediaType

# Импорты для поисковика
from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from ajax_select.fields import AutoCompleteSelectField

# AUTH_USER_MODEL находится в моделях

User = get_user_model()



class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_date'].label = 'Дата получения заказа'

    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment'
        )


# Пошёл раздел как сделать авторизацию для пользователя

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    # Тут идёт логика для переопределения (username=Логин, password=Пароль)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    # Проверки на существованиe пользователя и правильность пароля
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError(f'Пользователь с логином {username} не найден в системе')
        if not user.check_password(password):
            raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data


# Создание формы регистрации

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['phone'].label = 'Номер телефона'
        self.fields['address'].label = 'Адрес'
        self.fields['email'].label = 'Почта'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'

    # Проверка на валидность одного поля в моделе, а не всей модели(тут мы проверяем email)

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['net', 'xyz']:
            raise forms.ValidationError(f'Регистрация для домена {domain} не возможна')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Данный почтовый адрес уже зарегестрирован')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Имя {username} занято. Попробуйте другое.')

        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:

        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'address', 'phone', 'email']


# Сам класс для поиска

class SearchForm(forms.Form):

    GENRE_CHOICES = (
        (g['slug'], g['name']) for g in Genre.objects.all().values('slug', 'name')  # <--- на чём будет основываться поиск
    )
    MEDIA_TYPE_CHOICES = (                                                          # <--- на чём будет основываться поиск
        (m['id'], m['name']) for m in MediaType.objects.all().values('id', 'name')
    )

    def __init__(self, *args, **kwargs):                                            # <--- переопределение инита для вставление бутстрапа
        super().__init__(*args, **kwargs)
        self.fields['genre'].label = 'Жанр'                                         # <--- пошли сами поля для поиска
        self.fields['artist'].help_text = ''
        self.fields['media_type'].label = 'Медианоситель'
        self.fields['release_date_from'].label = 'Дата релиза (с)'
        self.fields['release_date_to'].label = 'Дата релиза (по)'

        self.helper = FormHelper()                                                  # <--- импорт формхелпера для красивой обложки с криспи форм
        self.helper.form_class = 'form-check form-check-inline'
        self.helper.layout = Layout(InlineCheckboxes(['genre', 'media_type']))      # <--- Вот тут мы отображаем наши поля для поиска , сюда их заворачиваем

        # дабы нагрузка на нашу БД не было слишком большой тут я инсталю django-ajax-selects(штука которая будет помогать написывать текст в моей выпадашке)

    artist = AutoCompleteSelectField('artist', required=False,
                                     help_text='Начните набор текста что бы увидеть результат')
    genre = forms.MultipleChoiceField(choices=GENRE_CHOICES,
                                      widget=forms.CheckboxSelectMultiple,
                                      required=False)
    media_type = forms.MultipleChoiceField(choices=MEDIA_TYPE_CHOICES,
                                           widget=forms.CheckboxSelectMultiple,
                                           required=False)

    release_date_from = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        required=False
    )
    release_date_to = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        required=False
    )

