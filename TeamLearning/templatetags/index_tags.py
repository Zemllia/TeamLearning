from django import template
from django.utils.safestring import mark_safe

from TeamLearning.models import News

register = template.Library()


@register.simple_tag(takes_context=True, name="get_logged_user")
def get_logged_user(context):
    logout_element = ""
    if context['request'].user.username != '':
        return mark_safe(context['request'].user.username + "<br><a href = /logout/> выйти </a>")
    else:
        return mark_safe("<a href = /login/> войти </a>")


@register.simple_tag(takes_context=True, name="load_news")
def load_news(context):
    news = News.objects.all().order_by('-date')
    posts = ""
    for post in news:
        header = post.post_header
        post_text = generate_post_text(post)
        post_image = post.post_image.url
        author = post.author
        date = post.date
        post_html = """<div class="post">
        <h1 class="post-header">{}</h1>
        <div class="post-text">
            {}
        </div>
        <div class="post-image">
            <img src="{}" height="480" width="640">
        </div>
        <a class="post-author">Автор: {}</a>
        <a class="post-date">{}</a>
        </div>""".format(header, post_text, post_image, author, date)
        posts += post_html
    return mark_safe(posts)


def generate_post_text(post):
    post_text = str(post.post_text)
    print(post.post_text)
    separated_text = post_text.split("\n")
    print(separated_text)
    final_text = ""
    for item in separated_text:
        final_text += "<p>" + item + "</p>"
    return final_text
