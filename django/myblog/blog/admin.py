from django.contrib import admin

from .models import Article

# 默认显示
# admin.site.register(Article)

# 默认其它字段
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')

    # 添加时间过滤器
    list_filter = ('pub_time', )

admin.site.register(Article, ArticleAdmin)


