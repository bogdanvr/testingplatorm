from django.contrib import admin
import lessons.models


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('problem', 'status', 'user',)
    list_filter = ('problem', 'user', 'status')


admin.site.register(lessons.models.Lesson)
admin.site.register(lessons.models.Problem)
admin.site.register(lessons.models.Submission, SubmissionAdmin)
admin.site.register(lessons.models.Test)
admin.site.register(lessons.models.Uslugi)
admin.site.register(lessons.models.Order)
admin.site.register(lessons.models.SubUslugi)
