from website.models import (
    ArticlePage,
    ArticleIndexPage,
    FormPage,
    FormPageField,
    FormConfirmEmail,
    WebPage,
)

"""
QuerySet: https://docs.djangoproject.com/en/2.1/ref/models/querysets/

Internally, a QuerySet can be constructed, filtered,
sliced, and generally passed around without actually
hitting the database. No database activity actually
occurs until you do something to evaluate the queryset.

Note: If you only need to determine the number of records
in the set (and don’t need the actual objects), it’s much
more efficient to handle a count at the database level
using SQL’s SELECT COUNT(*). Django provides a count()
method for precisely this reason.

object.count(): https://docs.djangoproject.com/en/2.1/ref/models/querysets/#django.db.models.query.QuerySet.count

"""

ARTICLE_PAGE = ArticlePage.objects
ARTICLE_INDEX_PAGE = ArticleIndexPage.objects
FORM_PAGE = FormPage.objects
FORM_PAGE_FIELD = FormPageField.objects
FORM_CONFIRM_EMAIL = FormConfirmEmail.objects
WEB_PAGE = WebPage.objects
