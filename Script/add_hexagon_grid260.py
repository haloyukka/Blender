#This source code is able to freely use for Blender and users.

bl_info = {
    "name": "Add hexagon_grid",
    "author": "TMO",
    "version": (0, 1, 0),
    "blender": (2, 6, 0),
    "location": "View3D > Add > Mesh > Add hexagon grid",
    "description": "Add hexagon grid",
    "warning": "",
    "wiki_url": "http://www.sousakuba.com/blender/index.html",
    "tracker_url": "",
    "category": "Add Mesh"}

import bpy
from bpy.props import *
from bpy_extras import object_utils
import math
import mathutils

class MSG():
    msg_type = ''
    msg = ''

class MessageBox(bpy.types.Operator, MSG):
    bl_idname = 'va.msg_box'
    bl_label = ''

    def draw(self, context):
        if self.msg_type == 'ERROR':
            self.t = 'ERROR'
        else:
            self.t = 'NONE'

        layout = self.layout
        row = layout.split(0.25)
        row.label(self.msg_type, icon = self.t)
        row.label(self.msg)

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self)

#def vlen(v):
#    return pow( v.x*v.x + v.y*v.y + v.z*v.z, 0.5 )

#def distNP(a,b):
#    return (b.x-a.x)*(b.x-a.x)+(b.y-a.y)*(b.y-a.y)+(b.z-a.z)*(b.z-a.z)

#def normal_vector(v):
#    v_len = vlen(v);
#    v.x /= v_len;
#    v.y /= v_len;
#    v.z /= v_len;

#def zoom(v, val):
#    v.x *= val;
#    v.y *= val;
#    v.z *= val;

#def cross_product(l,r):
#    return mathutils.Vector( (l.y * r.z) - (l.z * r.y), (l.z * r.x) - (l.x * r.z), (l.x * r.y) - (l.y * r.x) )

#def dot_product(l,r):
#    return l.x * r.x + l.y * r.y + l.z * r.z

class main(bpy.types.Operator):
    bl_idname="mesh.add_hexagon_grid"
    bl_label="Hexagon grid"
    bl_options = {'REGISTER', 'UNDO'}

    radius = FloatProperty(name="Radius",
        description="The radius of the hexagon",
        default=0.1,
        min=0.0001,
        max=9999.0,
        unit="LENGTH")

    num_x = IntProperty(name="X Number",
        description="Number of hexagon on the x-axis",
        default=10,
        min=1,
        max=9999)

    num_y = IntProperty(name="Y Number",
        description="Number of hexagon on the y-axis",
        default=10,
        min=1,
        max=9999)

    #def draw(self, context):
    #    return

    def execute(self, context):

        agl = math.pi / 3.0;

        hexagon_size = self.radius;
        hexagon_x_num = self.num_x;
        hexagon_y_num = self.num_y;

        pitch_x = ( hexagon_size + hexagon_size*math.cos(agl) )
        pitch_y = hexagon_size * math.sin(agl)*2.0
        #ofs_x   = hexagon_size + hexagon_size*math.cos(agl)
        ofs_y   = hexagon_size*math.sin(agl)

        wid = pitch_x * (hexagon_x_num-1) + hexagon_size*2.0
        hgt = pitch_y * hexagon_y_num
        if hexagon_x_num > 1:
            hgt += pitch_y*0.5

        origin_ofs_x = hexagon_size - wid * 0.5
        origin_ofs_y = pitch_y*0.5 - hgt * 0.5

        p0_x = hexagon_size
        p0_y = 0
        p1_x = hexagon_size*math.cos(agl)
        p1_y = hexagon_size*math.sin(agl)
        p2_x = -p1_x
        p2_y = p1_y
        p3_x = -hexagon_size
        p3_y = 0
        p4_x = p2_x
        p4_y = -p2_y
        p5_x = p1_x
        p5_y = -p1_y

        verts = []
        faces = []

        vert_pos = 0

        px = 0
        py = 0

        for ny in range(0,hexagon_y_num):
            for nx in range(0,hexagon_x_num):

                px = nx * pitch_x + origin_ofs_x;
                py = ny * pitch_y + origin_ofs_y;

                if nx%2 == 1:
                    py += ofs_y

                verts.append( [ p0_x + px, p0_y + py, 0 ] )
                verts.append( [ p1_x + px, p1_y + py, 0 ] )
                verts.append( [ p2_x + px, p2_y + py, 0 ] )
                verts.append( [ p3_x + px, p3_y + py, 0 ] )
                verts.append( [ p4_x + px, p4_y + py, 0 ] )
                verts.append( [ p5_x + px, p5_y + py, 0 ] )

                faces.append( [vert_pos+0,vert_pos+1,vert_pos+2,vert_pos+3,vert_pos+4,vert_pos+5] )

                vert_pos = vert_pos+6

    #----------------------------------------------------
        n_mesh = bpy.data.meshes.new("mesh")

        #register both edge and face. data broken!!
        #n_mesh.from_pydata(verts, edges, faces)
        #n_mesh.update()

        n_mesh.from_pydata(verts, [], faces)
        n_mesh.update(calc_edges=True)

        object_utils.object_data_add(context, n_mesh, operator=None)



        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(main.bl_idname, main.bl_label, icon="PLUGIN")

def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_mesh_add.append(menu_func)

def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_mesh_add.remove(menu_func)

if __name__ == "__main__":
    register()
