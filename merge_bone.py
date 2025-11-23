import bpy

# --- Trouver l’armature en Pose Mode ---
arm = None

# Vérifier l’objet actif
ao = bpy.context.active_object
if ao and ao.type == "ARMATURE" and ao.mode == "POSE":
    arm = ao

# Sinon chercher dans la scène
if arm is None:
    for obj in bpy.context.scene.objects:
        if obj.type == "ARMATURE" and obj.mode == "POSE":
            arm = obj
            break

if arm is None:
    raise Exception("Aucune armature en Pose Mode trouvée.")

# --- Récupérer les bones sélectionnés SANS UTILISER .select ---
sel_bones = bpy.context.selected_pose_bones
active_bone = bpy.context.active_pose_bone

if not sel_bones or len(sel_bones) < 2:
    raise Exception("Sélectionne au moins deux bones.")

if active_bone is None:
    raise Exception("Aucun bone actif trouvé.")

target_group_name = active_bone.name

# --- Trouver le mesh lié ---
mesh = None
for obj in bpy.context.scene.objects:
    if obj.type == "MESH":
        for mod in obj.modifiers:
            if mod.type == "ARMATURE" and mod.object == arm:
                mesh = obj
                break

if mesh is None:
    raise Exception("Aucun mesh trouvé pour cette armature.")

# --- Passer en Object Mode ---
bpy.context.view_layer.objects.active = mesh
bpy.ops.object.mode_set(mode='OBJECT')

# --- Créer/obtenir le vertex group cible ---
if target_group_name not in mesh.vertex_groups:
    mesh.vertex_groups.new(name=target_group_name)
target_group = mesh.vertex_groups[target_group_name]

# --- Mix des weights ---
for bone in sel_bones:
    if bone.name == target_group_name:
        continue

    if bone.name not in mesh.vertex_groups:
        continue

    src_group = mesh.vertex_groups[bone.name]

    for v in mesh.data.vertices:
        try:
            w = src_group.weight(v.index)
        except:
            w = 0.0

        if w > 0.0:
            try:
                current = target_group.weight(v.index)
            except:
                current = 0.0

            target_group.add([v.index], current + w, "REPLACE")

    mesh.vertex_groups.remove(src_group)

# --- Supprimer les bones source ---
bpy.context.view_layer.objects.active = arm
bpy.ops.object.mode_set(mode='EDIT')

edit_bones = arm.data.edit_bones
for bone in sel_bones:
    if bone.name != active_bone.name and bone.name in edit_bones:
        edit_bones.remove(edit_bones[bone.name])

bpy.ops.object.mode_set(mode='POSE')

print("✔ OK : Merge + suppression des bones source")
