import bpy

scene = bpy.context.scene

for obj in scene.objects:
    if obj and obj.type == 'MESH':
        # Trouver l'armature liée
        armature = next((mod.object for mod in obj.modifiers if mod.type == 'ARMATURE'), None)
        
        if armature and armature.type == 'ARMATURE':
            # Passer en mode Pose pour l'armature
            bpy.context.view_layer.objects.active = armature
            bpy.ops.object.mode_set(mode='POSE')

            # Obtenir les os sélectionnés via context
            selected_bones = [b.name for b in bpy.context.selected_pose_bones]

            # Obtenir l'os actif
            active_bone = bpy.context.active_pose_bone

            if active_bone and selected_bones:
                # Revenir en mode Object pour le mesh
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.mode_set(mode='OBJECT')

                for bone_name in selected_bones:
                    if bone_name != active_bone.name:
                        # Ajouter un modificateur Vertex Weight Mix
                        vgroup_name_a = active_bone.name
                        vgroup_name_b = bone_name

                        mod = obj.modifiers.new(
                            name=f'VertexWeightMix_{bone_name}_to_{active_bone.name}',
                            type='VERTEX_WEIGHT_MIX'
                        )
                        mod.vertex_group_a = vgroup_name_a
                        mod.vertex_group_b = vgroup_name_b
                        mod.mix_mode = 'ADD'
                        mod.mix_set = 'ALL'
                        
                        bpy.context.view_layer.objects.active = obj
                        bpy.ops.object.modifier_apply(modifier=mod.name)

                        print(f"FUSION → {bone_name} → {active_bone.name}")

                        # CLEAN du vertex group source
                        if bone_name in obj.vertex_groups:
                            obj.vertex_groups.remove(obj.vertex_groups[bone_name])
                            print(f"CLEAN weights du groupe : {bone_name}")

                # --- SUPPRIMER LES BONES SOURCE (sauf l'actif) ---
                bpy.context.view_layer.objects.active = armature
                bpy.ops.object.mode_set(mode='EDIT')
                edit_bones = armature.data.edit_bones
                for bone_name in selected_bones:
                    if bone_name != active_bone.name and bone_name in edit_bones:
                        edit_bones.remove(edit_bones[bone_name])
                        print(f"Bone supprimé : {bone_name}")
                bpy.ops.object.mode_set(mode='POSE')

            else:
                print("Veuillez sélectionner un os actif et au moins un autre os.")
        else:
            print("Aucune armature trouvée liée à l'objet mesh.")
