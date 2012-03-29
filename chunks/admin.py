from django.contrib import admin
from models import Chunk
from defaults.admin import BaseTranslationAdmin

class ChunkAdmin(BaseTranslationAdmin):
  list_display = ('key','description',)
  search_fields = ('key', 'content')

admin.site.register(Chunk, ChunkAdmin)
