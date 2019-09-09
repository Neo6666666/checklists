from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Response, Survey, Question, Answer, Report, Attachment


class QuestionInline(admin.TabularInline):
    model = Question
    ordering = ("order",)
    extra = 1


class AttachmentInline(GenericTabularInline):
    model = Attachment
    extra = 1
    ct_fk_field = 'object_id'
    ct_field = 'content_type'


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [QuestionInline]


class AnswerBaseInline(admin.StackedInline):
    fields = ("question", "body")
    readonly_fields = ("question",)
    extra = 0
    model = Answer


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "survey", "created", "user")
    list_filter = ("survey", "created")
    date_hierarchy = "created"
    inlines = [AttachmentInline, AnswerBaseInline]
    readonly_fields = ("survey", "created", "updated", "interview_uuid", "user")


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("name", "date_from", "date_to")
    list_filter = ("checklists",)


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass