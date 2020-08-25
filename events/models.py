from django.db import models
from django.core.exceptions import ValidationError

from wagtail.admin.edit_handlers import Page, FieldPanel, FieldRowPanel
from pages.models import MiscPage, ListPage

# Create your models here.


class EventPage(MiscPage):

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


    content_panels = MiscPage.content_panels + [
        FieldRowPanel([
            FieldPanel("start_date"),
            FieldPanel("end_date")
        ])
    ]

    def clean(self):
        super().clean()
        start_date = self.start_date
        end_date = self.end_date
        if end_date < start_date:
            raise ValidationError({
                "end_date": ValidationError("End date should be greater than start date.")
                })


class EventListPage(ListPage):
    start_date = models.DateField()
    end_date = models.DateField()

    content_panels = ListPage.content_panels + [
        FieldRowPanel([
            FieldPanel("start_date"),
            FieldPanel("end_date")
        ])
    ]

    def clean(self):
        super().clean()
        start_date = self.start_date
        end_date = self.end_date
        if end_date < start_date:
            raise ValidationError({
                "end_date": ValidationError("End date should be greater than start date.")
                })

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        children = self.get_children().live().public().specific()
        context['children'] = filter(lambda child: child.start_date.date() >= self.start_date and child.end_date.date() <= self.end_date, children)
        return context
