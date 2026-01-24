import bpy
from mathutils import Vector, Matrix

# -----------------------------
# VALIDATION
# -----------------------------
src_obj = bpy.context.object
if not src_obj or src_obj.type != 'ARMATURE':
    raise Exception("Sélectionne une armature SMD")

# On passe en mode EDIT sur la source pour récupérer les rolls exacts
bpy.context.view_layer.objects.active = src_obj
bpy.ops.object.mode_set(mode='EDIT')
# Dictionnaire pour stocker les rolls { "nom_os": valeur_roll }
original_rolls = {b.name: b.roll for b in src_obj.data.edit_bones}
bpy.ops.object.mode_set(mode='OBJECT')

# -----------------------------
# CREATE CLEAN ARMATURE
# -----------------------------
arm_data = bpy.data.armatures.new("Armature_Clean")
arm_obj = bpy.data.objects.new("Armature_Clean", arm_data)
bpy.context.collection.objects.link(arm_obj)

bpy.context.view_layer.objects.active = arm_obj
bpy.ops.object.mode_set(mode='EDIT')

src_bones = src_obj.data.bones
dst_bones = arm_data.edit_bones
bone_map = {}

# -----------------------------
# CREATE BONES (HEAD ONLY)
# -----------------------------
for b in src_bones:
    nb = dst_bones.new(b.name)
    nb.head = src_obj.matrix_world @ b.head_local
    bone_map[b.name] = nb

# -----------------------------
# PARENTING
# -----------------------------
for b in src_bones:
    if b.parent:
        bone_map[b.name].parent = bone_map[b.parent.name]

# -----------------------------
# TAIL COMPUTATION (CLEAN)
# -----------------------------
DEFAULT_LEN = 3

for b in src_bones:
    nb = bone_map[b.name]
    children = b.children

    if len(children) == 1:
        nb.tail = bone_map[children[0].name].head

    elif len(children) > 1:
        avg = Vector((0, 0, 0))
        for c in children:
            avg += bone_map[c.name].head
        avg /= len(children)
        nb.tail = avg

    else:
        nb.tail = nb.head + Vector((0, DEFAULT_LEN, 0))

    # Safety: zero-length protection
    if (nb.tail - nb.head).length < 0.001:
        nb.tail = nb.head + Vector((0, DEFAULT_LEN, 0))

# -----------------------------
# ROLL CONSERVATION (CORRIGÉ)
# -----------------------------
# Au lieu de recalculer, on applique les valeurs stockées
for b_name, roll_val in original_rolls.items():
    if b_name in dst_bones:
        dst_bones[b_name].roll = roll_val

bpy.ops.object.mode_set(mode='OBJECT')

print("Armature propre générée avec Rolls conservés : Armature_Clean")