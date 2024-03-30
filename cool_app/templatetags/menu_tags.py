from django import template
from django.db.models.query import Prefetch

from ..models import Menu, MenuItem
from ..utils import get_children

register = template.Library()

@register.inclusion_tag('templatetags/menubar.html', takes_context=True)
def draw_menu(context, menu_name):
    """
        Tag rendering specify menu by its name
        How does it work: firstly data from table is filtered,
        then child nodes move to parent nodes using recurursion.
        After that data is rendered, child nodes are rendered by dropdown tag

        params:
        context: 
        menu_name: menu's name which are used for selet data from db

        return: dict with menu items
    """
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent')
    nodes_dict = {}
    roots = list()
    for item in menu_items:
        item_dict = {
            'title': item.title,
            'slug': item.slug,
            'children': dict()
        }
        if not item.parent:
            nodes_dict[item.pk] = item_dict
            roots.append(item.pk)
            continue 
        if item.parent.slug not in context['request'].path: continue
        nodes_dict[item.pk] = item_dict
        nodes_dict[item.parent_id]["children"][item.pk] = item.pk

    for key in roots:
        if nodes_dict[key]["children"]:
            nodes_dict[key]["children"] = get_children(nodes_dict[key]["children"], nodes_dict)
            break
    print(nodes_dict)
    return {'items': nodes_dict}


@register.inclusion_tag('templatetags/dropdown.html', takes_context=True)
def dropdown(context, children: dict):
    """
     Inclusion tag for rendering child nodes
     
     params:
     children: dict with child nodes

     return: children for rendering
    """
    return {'children': children}