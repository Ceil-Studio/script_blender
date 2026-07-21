import bpy

def transfer_shape_keys(source_name, target_name):
    source_obj = bpy.data.objects.get(source_name)
    target_obj = bpy.data.objects.get(target_name)

    if not source_obj or not target_obj:
        print("Erreur : Objets introuvables.")
        return

    if not source_obj.data.shape_keys:
        print("Erreur : L'objet source n'a pas de shape keys.")
        return

    # S'assurer que la cible possède une shape key "Basis"
    if not target_obj.data.shape_keys:
        target_obj.shape_key_add(name="Basis")

    # Ajouter le modifier Surface Deform
    surf_mod = target_obj.modifiers.new(name="Transfer_SurfDeform", type='SURFACE_DEFORM')
    surf_mod.target = source_obj

    # Activer l'objet cible et bind la déformation
    bpy.context.view_layer.objects.active = target_obj
    try:
        bpy.ops.object.surfacedeform_bind(modifier=surf_mod.name)
    except RuntimeError as e:
        print(f"Erreur de bind (vérifie que les maillages n'ont pas de géométrie non-manifold ou superposée) : {e}")
        target_obj.modifiers.remove(surf_mod)
        return

    # Récupération des shape keys sources
    s_shape_keys = source_obj.data.shape_keys.key_blocks

    # Mémoriser les valeurs initiales pour ne pas casser la configuration actuelle
    initial_values = {}
    for sk in s_shape_keys:
        initial_values[sk.name] = sk.value
        sk.value = 0.0

    depsgraph = bpy.context.evaluated_depsgraph_get()

    # Itération et transfert de chaque shape key
    for sk in s_shape_keys:
        if sk.name == "Basis":
            continue

        # Activer la shape key courante
        sk.value = 1.0
        bpy.context.view_layer.update()

        # Évaluer la déformation sur le maillage cible
        eval_obj = target_obj.evaluated_get(depsgraph)
        eval_mesh = eval_obj.to_mesh()

        # Créer ou récupérer la shape key correspondante sur la cible
        new_sk = target_obj.data.shape_keys.key_blocks.get(sk.name)
        if not new_sk:
            new_sk = target_obj.shape_key_add(name=sk.name)

        # Copier les coordonnées évaluées
        for i, v in enumerate(eval_mesh.vertices):
            new_sk.data[i].co = v.co

        # Libérer la mémoire du maillage évalué
        eval_obj.to_mesh_clear()
        
        # Reset la shape key source pour la prochaine itération
        sk.value = 0.0

    # Restauration de l'état initial
    for sk in s_shape_keys:
        sk.value = initial_values[sk.name]

    # Nettoyage du modifier
    target_obj.modifiers.remove(surf_mod)
    print(f"Transfert terminé : {len(s_shape_keys)-1} shape keys copiées sur {target_name}.")

# --- Exécution ---
transfer_shape_keys("Head_Original", "Head_Retopo")
