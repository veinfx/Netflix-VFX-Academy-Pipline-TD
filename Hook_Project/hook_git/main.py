import hou


class HipAuto:
    def __init__(self):
        hip_path = "/home/rapa/tset_hip/"
        hip = f"{hip_path}test.hipnc"
        addCam_hip = "hip_path/test_addCam_1.hipnc"
        node = hou.pwd()
        hou.hipFile.load(hip)

        pass
# editCam_hip = "/home/rapa/test_hip/test_editCam.hipnc"

        # self._hip = ''
        # self._new_hip = ''


    # def hip_load(self):
    #     hou.hipFile.load(self.hip) #hip파일 가져오기


    def hip_save(self):
        hou.hipFile.save(file_name=self.addCam_hip)


    def createCamera(self):
        root = hou.node("/obj/")
        if root != None:
            n = root.createNode("cam")
            n.parm("focal").set(35)


    # def createMantra(self):
    #     root = hou.node("/out/")
    #     if root != None:
    #         n = root.createNode("ifd")
    #         s = self.hip_path/my_filename_0001.exr"
    #         n.parm("vm_picture").set(s)



def main():
    a = HipAuto()
    a.hip_load()
    a.createCamera()
    # a.createMantra()
    a.hip_save()


# n = hou.node("obj/geo1")
# n.parm("tx").set(1)

if __name__ == "__main__":
    main()


