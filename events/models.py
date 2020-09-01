from django.db import models
from django.core.exceptions import ValidationError

from wagtail.admin.edit_handlers import Page, FieldPanel, FieldRowPanel
from pages.models import MiscPage, ListPage

import datetime
# Create your models here.

def filter_date(child,parent):
    start_date = child.start_date.date() if type(child.start_date) is datetime.datetime else child.start_date
    end_date = child.end_date.date() if type(child.end_date) is datetime.datetime else child.end_date
    return start_date >= parent.start_date and end_date <= parent.end_date

def sort_key(child):
    return child.start_date.date() if type(child.start_date) is datetime.datetime else child.start_date


class EventPage(MiscPage):

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


    content_panels = MiscPage.content_panels + [
        FieldRowPanel([
            FieldPanel("start_date"),
            FieldPanel("end_date")
        ])
    ]

    parent_page_type = [
        'events.EventListPage'
    ]

    class Meta:
        ordering = ['start_date']

    def clean(self):
        super().clean()
        start_date = self.start_date
        end_date = self.end_date
        if start_date and end_date:
            if end_date < start_date:
                raise ValidationError({
                    "end_date": ValidationError("End date should be greater than start date.")
                    })


class EventListPage(ListPage):
    start_date = models.DateField()
    end_date = models.DateField()

    subpage_types = [
        'events.EventPage',
        'events.EventListPage'
    ]

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
        children = sorted(children, key = sort_key)



        context['children'] = filter(lambda child: filter_date(child,self), children)
        return context
