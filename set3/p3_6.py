def binary_tree_max(tree: dict):
    """
    Função que encontra o maior value dentro de um dict = {'value': n, 'children':[]} com 3 ramos
    """

    has_children = tree.get('children', 0)

    if has_children == []:
        return tree['value']

    children_value = []

    #Para cada dicionario aninhado, value é anexado ao children_value
    for children_dicts in tree['children']:
        children_value.append(binary_tree_max(children_dicts))

    if tree['value'] >= max(children_value):
        return tree['value']
    else:
        return max(children_value)

def tree_max(tree: dict):
    """
    Função que encontra o maior value dentro de um dict = {'value': n, 'children':[]} com 3 ramos
    """

    has_children = tree.get('children', 0)

    if has_children == []:
        return tree['value']

    children_value = []

    #Para cada dicionario aninhado, value é anexado ao children_value
    for children_dicts in tree['children']:
        children_value.append(binary_tree_max(children_dicts))

    if tree['value'] >= max(children_value):
        return tree['value']
    else:
        return max(children_value)