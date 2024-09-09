from django.shortcuts import render
from django.http import Http404
from . import util
from django.urls import get_resolver

def index(request):
    return render(request, "encyclopedia/index.html")



def entry_page(request, title):
    # Fetch the content of the encyclopedia entry by title
    entry = util.get_entry(title)
    
    # If the entry does not exist, raise a 404 error
    if entry is None:
        raise Http404("The requested encyclopedia entry was not found.")
    
    # If the entry exists, render the entry page with the entry content
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": entry
    })
    
    def show_urls(request):
        url_patterns = get_resolver().url_patterns
        url_list[]
        for pattern in url_patterns:
            url_list.append(str(pattern))
            return Http404("<br>".join(url_list))
    


