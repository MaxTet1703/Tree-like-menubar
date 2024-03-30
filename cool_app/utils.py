

def get_children(children, nodes_dict):
    """
        Recursive getting child nodes from root node
    """
    for child in children:
        children[child] = nodes_dict.pop(child)
        children[child]["children"] = get_children(
                                        children[child]["children"],
                                        nodes_dict)
        
    return children