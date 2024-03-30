

def get_children(children, nodes_dict):
    for child in children:
        children[child] = nodes_dict.pop(child)
        children[child]["children"] = get_children(
                                        children[child]["children"],
                                        nodes_dict)
        
    return children