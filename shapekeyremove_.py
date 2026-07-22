import bpy


def remove_underscores_from_shapekeys(selected_only=False):
    # Choix entre la sélection courante ou l'ensemble de la scène
    objects = bpy.context.selected_objects if selected_only else bpy.context.scene.objects

    renamed_count = 0
    obj_count = 0

    for obj in objects:
        # Vérification si l'objet est un mesh avec des Shape Keys
        if obj.type == 'MESH' and obj.data.shape_keys:
            key_blocks = obj.data.shape_keys.key_blocks
            obj_renamed = False

            for key in key_blocks:
                if "_" in key.name:
                    old_name = key.name
                    key.name = key.name.replace("_", "")
                    print(f"[{obj.name}] ShapeKey : '{old_name}' -> '{key.name}'")
                    renamed_count += 1
                    obj_renamed = True

            if obj_renamed:
                obj_count += 1

    print(
        f"\nTerminé. {renamed_count} ShapeKey(s) renommée(s) sur {obj_count} objet(s)."
    )


# Passer 'selected_only=True' si tu veux cibler uniquement les objets sélectionnés
remove_underscores_from_shapekeys(selected_only=False)