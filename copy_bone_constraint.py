import bpy

sel = [o for o in bpy.context.selected_objects if o.type == 'ARMATURE']

if len(sel) != 2:
    raise Exception("Sélectionne EXACTEMENT 2 armatures")

dst = bpy.context.view_layer.objects.active
if dst.type != 'ARMATURE':
    raise Exception("L'objet actif doit être une armature")

src = sel[0] if sel[1] == dst else sel[1]

for bone_name, src_pb in src.pose.bones.items():
    if bone_name not in dst.pose.bones:
        continue

    dst_pb = dst.pose.bones[bone_name]

    # SUPPRESSION CORRECTE DES CONTRAINTES
    while dst_pb.constraints:
        dst_pb.constraints.remove(dst_pb.constraints[0])

    for c in src_pb.constraints:
        nc = dst_pb.constraints.new(type=c.type)

        for prop in dir(c):
            if prop.startswith("_") or prop in {"rna_type", "type"}:
                continue
            try:
                setattr(nc, prop, getattr(c, prop))
            except:
                pass

        if hasattr(nc, "target") and nc.target == src:
            nc.target = dst
