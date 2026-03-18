from django.apps import AppConfig
from django.db.models.signals import post_migrate


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .models import Book
        
        def create_sample_books(sender, **kwargs):
            """Create sample books if none exist"""
            if Book.objects.exists():
                return
            
            sample_books = [
                {
                    'title': 'The Great Gatsby',
                    'author': 'F. Scott Fitzgerald',
                    'price': 10.99,
                    'published_date': '1925-04-10'
                },
                {
                    'title': 'To Kill a Mockingbird',
                    'author': 'Harper Lee',
                    'price': 12.99,
                    'published_date': '1960-07-11'
                },
                {
                    'title': '1984',
                    'author': 'George Orwell',
                    'price': 13.99,
                    'published_date': '1949-06-08'
                }
            ]
            
            for book_data in sample_books:
                Book.objects.get_or_create(
                    title=book_data['title'],
                    defaults={
                        'author': book_data['author'],
                        'price': book_data['price'],
                        'published_date': book_data['published_date']
                    }
                )
        
        post_migrate.connect(create_sample_books, sender=self)
