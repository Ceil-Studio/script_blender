import bpy

# Remplacez par les noms d'os que vous souhaitez utiliser
new_bone_names = [
    "ValveBiped.Bip01_Pelvis", "ValveBiped.Bip01_Spine1", "ValveBiped.Bip01_Spine2", "ValveBiped.Bip01_Spine4", "ValveBiped.Bip01_Neck1", "ValveBiped.Bip01_Head1", "ValveBiped.Bip01_L_Clavicle", "ValveBiped.Bip01_L_UpperArm", "ValveBiped.Bip01_L_Forearm", "ValveBiped.Bip01_L_Hand", "ValveBiped.Bip01_L_Finger0",
    "ValveBiped.Bip01_L_Finger01", "ValveBiped.Bip01_L_Finger02", "ValveBiped.Bip01_L_Finger1", "ValveBiped.Bip01_L_Finger11", "ValveBiped.Bip01_L_Finger12", "ValveBiped.Bip01_L_Finger2", "ValveBiped.Bip01_L_Finger21", "ValveBiped.Bip01_L_Finger22", "ValveBiped.Bip01_L_Finger3", "ValveBiped.Bip01_L_Finger31", "ValveBiped.Bip01_L_Finger32", 
    "ValveBiped.Bip01_L_Finger4", "ValveBiped.Bip01_L_Finger41", "ValveBiped.Bip01_L_Finger42", "ValveBiped.Bip01_R_Clavicle", "ValveBiped.Bip01_R_UpperArm", "ValveBiped.Bip01_R_Forearm", "ValveBiped.Bip01_R_Hand", "ValveBiped.Bip01_R_Finger0", "ValveBiped.Bip01_R_Finger01", "ValveBiped.Bip01_R_Finger02", "ValveBiped.Bip01_R_Finger1", 
    "ValveBiped.Bip01_R_Finger11", "ValveBiped.Bip01_R_Finger12", "ValveBiped.Bip01_R_Finger2", "ValveBiped.Bip01_R_Finger21", "ValveBiped.Bip01_R_Finger22", "ValveBiped.Bip01_R_Finger3", "ValveBiped.Bip01_R_Finger31", "ValveBiped.Bip01_R_Finger32", "ValveBiped.Bip01_R_Finger4", "ValveBiped.Bip01_R_Finger41", "ValveBiped.Bip01_R_Finger42", 
    "ValveBiped.Bip01_L_Thigh", "ValveBiped.Bip01_L_Calf", "ValveBiped.Bip01_L_Foot", "ValveBiped.Bip01_L_Toe0", "ValveBiped.Bip01_R_Thigh", "ValveBiped.Bip01_R_Calf", "ValveBiped.Bip01_R_Foot", "ValveBiped.Bip01_R_Toe0",
    # Ajoutez autant de noms que nécessaire
]

# Sélectionnez l'armature active
armature = bpy.context.object

# Vérifiez que l'objet sélectionné est bien une armature
if armature and armature.type == 'ARMATURE':
    bpy.ops.object.mode_set(mode='EDIT')  # Passe en mode Édition pour modifier les os
    
    bones = armature.data.edit_bones
    bone_count = len(bones)
    
    if not 10:
        print("Il n'y a pas assez de nouveaux noms pour remplacer tous les os.")
    else:
        for i, bone in enumerate(bones):
            print(f"{bone.name} {i}")
            
            if i < len(new_bone_names):
                print(f"{i}")
                bone.name = new_bone_names[i]
            else:
                break
    
    bpy.ops.object.mode_set(mode='OBJECT')  # Retourne en mode Objet
else:
    print("Sélectionnez une armature avant d'exécuter le script.")
