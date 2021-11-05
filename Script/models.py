import bpy  # blenderインポート

#1.円柱location:図形の中心座標 radius:円の半径 depth:高さ rotation：立体の回転角(rad)
bpy.ops.mesh.primitive_cylinder_add(location=(-5, 5, 0), radius=1, depth=3, rotation=(0, 0, 0))

#2.立方体 location:図形の中心座標 size:立方体の一辺の長さ rotation：立体の回転角(rad)
bpy.ops.mesh.primitive_cube_add(location=(5, 0, 0), size=1.5, rotation=(0, 0, 0))

#3.球体 location:図形の中心座標  radius :球の半径 subdivisions：分割数
bpy.ops.mesh.primitive_ico_sphere_add(location=(-5, 0, 0), radius=1, subdivisions=5)

#4.monkey location:図形の中心座標  size:サイズ
bpy.ops.mesh.primitive_monkey_add(location = (-5, -5, 0), size = 3.0)

#5.ドーナツ形 location:図形の中心座標 major_radius:輪の半径 minor_radius:筒の半径 rotation:立体の回転角(rad)
bpy.ops.mesh.primitive_torus_add(location=(0, 5, 0), major_radius=1.0, minor_radius=0.1, rotation=(0, 0, 0))

#6.平板(円) location:図形の中心座標 fill_type:塗りつぶし radius:半径 rotation:立体の回転角(rad)
bpy.ops.mesh.primitive_circle_add(location=(5, 5, 0), fill_type="NGON", radius=2, rotation=(0, 0, 0))

#7.平板(正方形) location:図形の中心座標  size :辺の長さ rotation:立体の回転角(rad)
bpy.ops.mesh.primitive_plane_add(location=(5, -5, 0), rotation=(0, 0, 0), size=2)

#8.多角錐 location:図形の中心座標 vertices:頂点の数 radius1,radius2:円の半径 depth:高さ rotation：立体の回転角(rad)
bpy.ops.mesh.primitive_cone_add(location=(0,-5,0),vertices=10,radius1=0.5,radius2=1,depth=3, rotation=(0, 0, 0))
