import hou

# class Hou:
#     def __init__(self):

hip = "/home/rapa/temp.hipnc"
add_hip = "/home/rapa/test_addCamMantra_1.hipnc"
render_path = "/home/rapa/render/my_filename_001.exr"
# un_name ="/home/rapa/test_hip/un_name.hipnc"

# hou.hipFile.isNewFile()
# hou.hipFile.load(hip) #hip파일 가져오기
# 로드를 하지않아도 빈 houdini 파일로 진행된다.

# node = hou.pwd()
def createCamera():
    root = hou.node("/obj/")
    if root != None:
        n = root.createNode("cam")
        n.parm("focal").set(33)

def createMantra():
    root = hou.node("/out/")
    if root != None:
        n = root.createNode("ifd")
        # s = "/home/rapa/my_filename_0033.exr"
        n.parm("vm_picture").set(render_path)
        n.parm("execute").pressButton()

createCamera()
createMantra()

hou.hipFile.save(file_name=add_hip)

