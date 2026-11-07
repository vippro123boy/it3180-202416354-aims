def search_by_category(items, category):
    return [item for item in items if item.category.lower() == category.lower()]

def search_by_title(items, keyword):
    return [item for item in items if keyword in item.title]
