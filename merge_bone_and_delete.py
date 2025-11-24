import bpy

scene = bpy.context.scene

# On récupère SEULEMENT l’armature active en pose mode
armature = bpy.context.active_object

if not armature or armature.type != "ARMATURE" or armature.mode != "POSE":
    raise Exception("Sélectionne une armature en Pose Mode avant de lancer le script.")

# Sauvegarder l’armature explicitement (pour ne jamais perdre sa référence)
target_armature = armature

# Os sélectionnés
selected_bones = [b.name for b in bpy.context.selected_pose_bones]
active_bone = bpy.context.active_pose_bone

if not active_bone or not selected_bones:
    raise Exception("Sélectionne un os actif et au moins un os à fusionner.")

# Tous les meshes liés à CETTE armature UNIQUEMENT
linked_meshes = []
for obj in scene.objects:
    if obj.type == "MESH":
        for mod in obj.modifiers:
            if mod.type == "ARMATURE" and mod.object == target_armature:
                linked_meshes.append(obj)
                break

# FUSION DES WEIGHTS POUR CHAQUE MESH LIÉ
for mesh in linked_meshes:

    # On ne touche PAS à l’armature active
    bpy.context.view_layer.objects.active = mesh
    bpy.ops.object.mode_set(mode='OBJECT')

    for bone_name in selected_bones:
        if bone_name != active_bone.name:

            mod = mesh.modifiers.new(
                name=f'VertexWeightMix_{bone_name}_to_{active_bone.name}',
                type='VERTEX_WEIGHT_MIX'
            )
            mod.vertex_group_a = active_bone.name
            mod.vertex_group_b = bone_name
            mod.mix_mode = 'ADD'
            mod.mix_set = 'ALL'

            bpy.context.view_layer.objects.active = mesh
            bpy.ops.object.modifier_apply(modifier=mod.name)
            print(f"FUSION → {bone_name} → {active_bone.name}")

            # CLEAN du vertex group source
            if bone_name in mesh.vertex_groups:
                mesh.vertex_groups.remove(mesh.vertex_groups[bone_name])
                print(f"CLEAN weights du groupe : {bone_name}")


# --- SUPPRESSION DES BONES (UNIQUEMENT target_armature) ---
# On réactive explicitement l’armature pour éviter toute confusion
bpy.context.view_layer.objects.active = target_armature
bpy.ops.object.mode_set(mode='EDIT')

edit_bones = target_armature.data.edit_bones

for bone_name in selected_bones:
    if bone_name != active_bone.name and bone_name in edit_bones:
        edit_bones.remove(edit_bones[bone_name])
        print(f"Bone supprimé : {bone_name}")

bpy.ops.object.mode_set(mode='POSE')
print("Terminé : fusion + clean + SUPPRESSION uniquement sur l’armature active.")
