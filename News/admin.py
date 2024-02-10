from django.contrib import admin

from .models import Photo, News, Like, Comment, LikeComment


class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

	class Meta:
		model = News


admin.site.register(Photo)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(LikeComment)
