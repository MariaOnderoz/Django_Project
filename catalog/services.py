from config.settings import CASHE_ENABLED
from catalog.models import Category


def get_categories_from_cache():
    if not CACHE_ENABLED:
        return Category.object.all()
    key = "category_list"
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories
