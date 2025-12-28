import bpy

selected = set(bpy.context.selected_objects)

def get_hierarchy(obj, result=None):
    if result is None:
        result = []
    result.append(obj)
    for child in obj.children:
        get_hierarchy(child, result)
    return result

# racines = objets sélectionnés sans parent sélectionné
roots = [o for o in selected if o.parent not in selected]

for root in roots:
    # créer la collection
    col = bpy.data.collections.new(root.name)
    bpy.context.scene.collection.children.link(col)

    # récupérer toute la hiérarchie
    hierarchy = get_hierarchy(root)

    for obj in hierarchy:
        # enlever de toutes les collections
        for c in obj.users_collection:
            c.objects.unlink(obj)

        # ajouter à la nouvelle collection
        col.objects.link(obj)
