from .metrics import ModelsGauges
from ..query_sets import (
    ARTICLE_PAGE,
    ARTICLE_INDEX_PAGE,
    FORM_PAGE,
    FORM_PAGE_FIELD,
    FORM_CONFIRM_EMAIL,
    WEB_PAGE,
)
from ..labels import (
    ARTICLE,
    ARTICLE_INDEX,
    FORM,
    FORM_FIELD,
    EMAIL,
    WEBPAGE,
)
GAUGE = ModelsGauges()


def models_gauge_monitor():

    GAUGE.django_model_objects.labels(ARTICLE).set(ARTICLE_PAGE.count())
    GAUGE.django_model_objects.labels(ARTICLE_INDEX).set(ARTICLE_INDEX_PAGE.count())
    GAUGE.django_model_objects.labels(FORM).set(FORM_PAGE.count())
    GAUGE.django_model_objects.labels(FORM_FIELD).set(FORM_PAGE_FIELD.count())
    GAUGE.django_model_objects.labels(EMAIL).set(FORM_CONFIRM_EMAIL.count())
    GAUGE.django_model_objects.labels(WEBPAGE).set(WEB_PAGE.count())
