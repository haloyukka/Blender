import bpy

# 既存要素削除
for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)

# 頂点データの作成
verts = [[-2.0, -2.0, 0.0], [-2.0, 2.0,  0.0], [2.0, 2.0,  0.0] , [2.0, -2.0,  0.0], [2.0, -2.0, 4.0] , [2.0, 2.0, 4.0]  ]
# 面データの作成        
faces = [[0,1,2,3], [2,3,4,5]]

msh = bpy.data.meshes.new("cubemesh") #Meshデータの宣言
msh.from_pydata(verts, [], faces) # 頂点座標と各面の頂点の情報でメッシュを作成
obj = bpy.data.objects.new("cube", msh) # メッシュデータでオブジェクトを作成
bpy.context.scene.collection.objects.link(obj) # シーンにオブジェクトを配置
