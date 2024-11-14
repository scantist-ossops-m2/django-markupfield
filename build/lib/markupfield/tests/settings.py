DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'markuptest.db'
    }
}

import markdown
from django.utils.html import escape, linebreaks, urlize
from docutils.core import publish_parts


def render_rest(markup):
    parts = publish_parts(source=markup, writer_name="html4css1")
    return parts["fragment"]

MARKUP_FIELD_TYPES = [
    ('markdown', markdown.markdown),
    ('ReST', render_rest),
    ('plain', lambda markup: urlize(linebreaks(escape(markup)))),
]

INSTALLED_APPS = (
    'markupfield.tests',
)

SECRET_KEY = 'sekrit'
