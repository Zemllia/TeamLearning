from django import forms

from TeamLearning.models import User, Team, News


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
