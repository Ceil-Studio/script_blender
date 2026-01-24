import bpy

def add_constraints_to_active():
    # 1. Vérification de la sélection
    selected_objects = bpy.context.selected_objects
    active_object = bpy.context.active_object

    # On s'assure qu'il y a exactement 2 objets sélectionnés
    if len(selected_objects) != 2:
        print("Erreur : Veuillez sélectionner exactement deux armatures.")
        return

    # On s'assure que l'objet actif est bien une armature
    if active_object.type != 'ARMATURE':
        print("Erreur : L'objet actif doit être une armature.")
        return

    # Identifier l'objet "Source" (l'autre objet sélectionné qui n'est pas l'actif)
    source_object = None
    for obj in selected_objects:
        if obj != active_object:
            source_object = obj
            break
            
    # Vérifier que la source est aussi une armature
    if source_object.type != 'ARMATURE':
        print("Erreur : L'autre objet sélectionné n'est pas une armature.")
        return

    print(f"Cible (Source) : {source_object.name} -> Receveur (Actif) : {active_object.name}")

    # 2. Passer en mode Pose pour être sûr (optionnel mais recommandé)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # 3. Boucle sur les os de l'armature active (le receveur)
    count = 0
    for p_bone in active_object.pose.bones:
        bone_name = p_bone.name
        
        # Vérifier si l'os existe dans l'armature source
        if bone_name in source_object.data.bones:
            
            # --- Ajout de Copy Location ---
            const_loc = p_bone.constraints.new(type='COPY_LOCATION')
            const_loc.target = source_object
            const_loc.subtarget = bone_name
            const_loc.name = "Copy Loc (Script)"
            
            # --- Ajout de Copy Rotation ---
            const_rot = p_bone.constraints.new(type='COPY_ROTATION')
            const_rot.target = source_object
            const_rot.subtarget = bone_name
            const_rot.name = "Copy Rot (Script)"
            
            count += 1
        else:
            print(f"Attention : L'os '{bone_name}' n'existe pas dans l'armature source.")

    print(f"Terminé ! Contraintes ajoutées sur {count} os.")

# Exécuter la fonction
add_constraints_to_active()