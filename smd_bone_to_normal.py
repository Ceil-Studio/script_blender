import bpy
from mathutils import Vector, Matrix

# -----------------------------
# VALIDATION
# -----------------------------
src_obj = bpy.context.object
if not src_obj or src_obj.type != 'ARMATURE':
    raise Exception("Sélectionne une armature SMD")

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
# ROLL RECALCULATION
# -----------------------------
bpy.ops.object.mode_set(mode='OBJECT')
bpy.context.view_layer.objects.active = arm_obj
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.armature.calculate_roll(type='GLOBAL_POS_Y')

bpy.ops.object.mode_set(mode='OBJECT')

print("Armature propre générée : Armature_Clean")
