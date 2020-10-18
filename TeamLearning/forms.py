from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext, gettext_lazy as _


from TeamLearning.models import User, Team, News


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Никнейм (показывается на сайте)")

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'username_not_unique': "Пользователь с таким именем уже существует"
    }

    def clean_username(self):
        cur_username = self.cleaned_data.get('username')
        if User.objects.filter(username=cur_username).count() != 0:
            raise forms.ValidationError("Польователь с таким именем уже существует")
        return cur_username

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)

    class Meta:
        model = User
        fields = ("username", "email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)


class UserForm(forms.ModelForm):
    """A form for creating new users. Includes all the required"""

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['username'].required = True

    class Meta:
        model = User
        fields = ('email', 'username', 'last_name',
                           'first_name', 'avatar', 'professionalism_coefficient')

    """def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        password = User.objects.make_random_password()
        user.set_password(password)
        user.generate_login(settings.LOGIN_LENGTH)
        auth_group = auth_models.Group.objects.get(codename=ROLE_VISITOR)

        # send email
        subject = 'Код доступа в систему ДО "Глобус"'
        template = 'globus/visitor_code_email.txt'
        context = {
            'user': user,
            'group': auth_group
        }

        utils.send_template_email(subject, template, context, settings.SERVICE_EMAIL, user.email)

        if commit:
            user.save()
            user.groups.add(auth_group)
        return user"""


class TeamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        super(TeamForm, self).__init__(*args, **kwargs)

        self.fields['users'].required = False
        self.fields['name'].required = True
        self.fields['description'].required = False

    class Meta:
        model = Team
        fields = ('name', 'users', 'description', 'avatar')


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        super(NewsForm, self).__init__(*args, **kwargs)

        self.fields['author'].required = True
        self.fields['post_header'].required = True
        self.fields['post_text'].required = True
        self.fields['post_image'].required = False
        self.fields['date'].required = True

    class Meta:
        model = News
        fields = ('author', 'post_header', 'post_text', 'post_image', 'date')
