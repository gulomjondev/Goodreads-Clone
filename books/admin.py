from django.contrib import admin

from .models import Book,Author,BookAuthor,BookReview

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    search_fields = ('title','isbn')
    

class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAuthorAdmin(admin.ModelAdmin):
    pass

class BookReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book,BookAdmin)
admin.site.register(Author,BookAdmin)
admin.site.register(BookAuthor,BookAdmin)
admin.site.register(BookReview,BookAdmin)
