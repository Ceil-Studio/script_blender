import bpy
from mathutils import Vector
from math import radians

obj = bpy.context.object

if not obj or obj.type != 'ARMATURE':
    raise RuntimeError("Sélectionne une armature.")

pose_bones = bpy.context.selected_pose_bones

if not pose_bones:
    raise RuntimeError("Aucun bone sélectionné en Pose Mode.")

bone_names = [pb.name for pb in pose_bones]

# passer en edit mode
bpy.ops.object.mode_set(mode='EDIT')
edit_bones = obj.data.edit_bones

back_vec = Vector((0, 1, 0))  # arrière monde (-Y)

for name in bone_names:
    eb = edit_bones.get(name)
    if not eb:
        continue

    length = (eb.tail - eb.head).length
    eb.tail = eb.head + back_vec * length
    eb.roll = radians(-180)

# retour en pose mode
bpy.ops.object.mode_set(mode='POSE')
