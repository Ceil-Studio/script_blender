import bpy
import os

# CHEMIN DU DOSSIER TEXTURES
TEXTURE_DIR = r"/home/ceilciuz/commande/kronos/all_texture"   # <<< À MODIFIER

for mat in bpy.data.materials:
    if not mat.use_nodes:
        continue

    mat_name = mat.name
    tex_name = mat_name + "_d.dds"
    tex_path = os.path.join(TEXTURE_DIR, tex_name)

    if not os.path.exists(tex_path):
        print(f"Texture manquante : {tex_name}")
        continue

    # Charger l'image
    image = bpy.data.images.load(tex_path, check_existing=True)

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Chercher le Principled BSDF
    principled = None
    for n in nodes:
        if n.type == 'BSDF_PRINCIPLED':
            principled = n
            break

    if not principled:
        print(f"Aucun Principled dans {mat_name}")
        continue

    # Créer node Image Texture
    tex_node = nodes.new("ShaderNodeTexImage")
    tex_node.image = image
    tex_node.location = principled.location.x - 400, principled.location.y

    # Brancher sur Base Color
    links.new(tex_node.outputs["Color"], principled.inputs["Base Color"])

    print(f"OK : {mat_name} → {tex_name}")
