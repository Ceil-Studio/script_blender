import bpy
import math
from mathutils import Vector, Matrix

# --- CONFIGURATION TAA ---
CORRECTION_TABLE = {
    "ValveBiped.Bip01_R_Clavicle" : 2.98,
    "ValveBiped.Bip01_L_Clavicle" : 2.98,
    "ValveBiped.Bip01_R_UpperArm" : 6.38,
    "ValveBiped.Bip01_L_UpperArm" : 6.38,
    "ValveBiped.Bip01_R_Forearm" : 11.69,
    "ValveBiped.Bip01_L_Forearm" : 11.69,
    "ValveBiped.Bip01_R_Hand" : 11.48,
    "ValveBiped.Bip01_L_Hand" : 11.48,
    "ValveBiped.Bip01_Neck1" : 3.307,
    "ValveBiped.Bip01_Spine" : 4.481,
    "ValveBiped.Bip01_Spine1" : 4.018,
    "ValveBiped.Bip01_Spine2" : 3.519,
    "ValveBiped.Bip01_Spine4" : 8.943,
    "ValveBiped.Bip01_R_Calf" : 17.8481,
    "ValveBiped.Bip01_L_Calf" : 17.8481,
    "ValveBiped.Bip01_R_Foot" : 16.525,
    "ValveBiped.Bip01_L_Foot" : 16.525,
}

def generate_gmod_definebones_direct_math_clipboard():
    obj = bpy.context.active_object
    if not obj or obj.type != 'ARMATURE':
        print("Erreur: Sélectionnez une armature.")
        return

    output_lines = []
    # On stocke ici la valeur de correction REELLE appliquée à chaque os sur l'axe X
    qc_deltas = {}

    def get_depth(bone):
        d = 0
        curr = bone
        while curr.parent:
            d += 1
            curr = curr.parent
        return d
    
    sorted_bones = sorted(obj.pose.bones, key=get_depth)

    for pbone in sorted_bones:
        name = pbone.name
        parent = pbone.parent
        
        # 1. Position locale actuelle (SMD)
        if parent:
            local_mat = parent.matrix.inverted() @ pbone.matrix
            base_pos = local_mat.to_translation()
            base_rot = local_mat.to_euler('XYZ')
        else:
            base_pos = pbone.matrix.translation
            base_rot = pbone.matrix.to_euler('XYZ')

        # 2. Récupérer la correction du parent pour soustraction
        parent_qc_corr = qc_deltas.get(parent.name, 0.0) if parent else 0.0

        # 3. CALCUL DU DELTA LOCAL (Le "1" ou "-1")
        # Formule : Correction = Cible - (Position_Actuelle_Blender + Correction_Parent)
        this_bone_corr_x = 0.0
        if name in CORRECTION_TABLE and parent:
            target_x = CORRECTION_TABLE[name]
            this_bone_corr_x = target_x - (base_pos.x + parent_qc_corr)

        # Mémorisation pour la chaîne hiérarchique
        qc_deltas[name] = parent_qc_corr + this_bone_corr_x

        # 4. Conversion du vecteur de correction vers l'espace de l'os enfant
        # On projette le delta X du parent sur les axes locaux de l'enfant
        if parent:
            rot_rel = local_mat.to_3x3()
            corr_vec_final = rot_rel.inverted() @ Vector((this_bone_corr_x, 0, 0))
        else:
            corr_vec_final = Vector((0,0,0))

        # 5. Formatage de la ligne QC
        line = (
            f'$definebone "{name}" "{parent.name if parent else ""}" '
            f'{base_pos.x:.6f} {base_pos.y:.6f} {base_pos.z:.6f} '
            f'{math.degrees(base_rot.y):.6f} {math.degrees(base_rot.z):.6f} {math.degrees(base_rot.x):.6f} '
            f'{corr_vec_final.x:.6f} {corr_vec_final.y:.6f} {corr_vec_final.z:.6f} '
            f'0.000000 0.000000 0.000000'
        )
        output_lines.append(line)

    # --- ACTION DE COPIE ---
    full_result = "\n".join(output_lines)
    bpy.context.window_manager.clipboard = full_result
    
    print("-" * 30)
    print("RÉSULTAT COPIÉ DANS LE PRESSE-PAPIER")
    print(f"Logique: {len(output_lines)} os traités avec delta soustractif.")
    print("-" * 30)

if __name__ == "__main__":
    generate_gmod_definebones_direct_math_clipboard()