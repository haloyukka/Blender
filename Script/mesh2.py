import bpy
import math

# 既存要素削除
for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)

# 頂点の作成
verts = []
for i in range(0,21):
    x = 2 *math.pi / 20 * i
    verts.append([x, -1, math.sin(x)])

for i in range(0,21):
    x = 2 * math.pi / 20 * i
    verts.append([x,  1, math.sin(x)])

# 面データの作成        
faces = []
for i in range(0,20):
    faces.append([i, i+1, i+22, i+21])

msh = bpy.data.meshes.new("sinmesh") 
msh.from_pydata(verts, [], faces) 
obj = bpy.data.objects.new("sin", msh) 
bpy.context.scene.collection.objects.link(obj) 
