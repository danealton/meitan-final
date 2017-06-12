def page_to_dict(page):
    return {
        'title': page.title,
        'id': page.id,
        'slug': page.get_absolute_url(),
        'children': [page_to_dict(child) for child in page.get_children().filter(in_navigation=True)]
    }

def pages_to_dict(pages):
    return map(page_to_dict, pages)
