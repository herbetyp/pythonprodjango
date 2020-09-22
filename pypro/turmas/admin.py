from django.contrib import admin

from pypro.turmas import models


@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'inicio', 'fim']
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ['-inicio']
