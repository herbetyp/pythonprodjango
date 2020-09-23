from django.contrib import admin

from pypro.turmas import models


class MatriculaInline(admin.TabularInline):
    model = models.Turma.alunos.through
    extra = 1
    readonly_fields = ['data']
    autocomplete_fields = ['usuario']
    ordering = ['-data']


@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]
    list_display = ['nome', 'slug', 'inicio', 'fim']
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ['-inicio']
