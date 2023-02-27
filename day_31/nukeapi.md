
- cd .nuke
    - 개인 환경 설정
- 모든 사람들의 환경을 일정하게 맞춰주어야 함
- vi .bashrc
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cdb14aba-3311-464c-bcb5-53a0ae59da1c/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/43ebd067-c61a-454c-b035-06529ed6c2eb/Untitled.png)
    
    - Nuke가 설정 파일을 읽는 순서
        1. $NUKE_PATH의 init.py와 menu.py
        
        1. ~/.nuke의 init.py와 menu.py
        
    
    - backend에서 실행되는 항목들은 path, batch render는  init.py
    - UI와 nuke 안에서 사용하는 것들은  menu.py
    
    ```python
    $NUKE_PATH의 init.py
    
    import nuke
    import os
    
    nuke.pluginAddPath("./python")
    os.environ["BROWSER"] = "firefox"
    
    -----------
    menu.py
    --------
    
    from imp import reload
    import nuke
    import nukescripts
    
    # MENU BAR
    menu_bar = menubar.addMenu("script")
    menu_bar.addCommand("space", "nukescripts.start('https://pipeline.jetbrains.space/')", "F1")
    menu_bar.addCommand("kitsu", "nukescripts.start('http://192.168.3.116')", "F2")
    
    # UI TEST
    import nuke_test
    menu_bar.addCommand("test", 'reload(nuke_test);nuke_test.main()', "F3")
    
    ------
    nuke_test   : Test UI 
    -------
    
    import sys
    import os
    from PySide2 import QtWidgets, QtCore, QtUiTools
    
    class TestUI(QtWidgets.QWidget):
    
        def __init__(self) -> None:
            super(TestUI).__init__()
            self.load_ui()
            # print(self.ui.label.text())
    
        def load_ui(self):
            script_path = os.path.realpath(__file__)
            ui_path = os.path.join(os.path.dirname(script_path), 'test.ui')
            ui_file = QtCore.QFile(ui_path)
            ui_file.open(QtCore.QFile.ReadOnly)
            loader = QtUiTools.QUiLoader()
            self.ui = loader.load(ui_file)
            ui_file.close()
    
    def main():
        global app
        try:
            app.ui.close()
        except:
            pass
        app = TestUI()
        app.ui.show()
    ```
    
    - 지섭님 test.py
    
    ```python
    import nuke
    
    read = nuke.nodes.Read()
    read['file'].setValue('{file_path}')
    read['first'].setValue('{first_frame}')
    read['last'].setValue('{last_frame}')
    
    format = nuke.nodes.Reformat()
    format['type'].setValue('to box')
    format['box_fixed'].setValue(True)
    format['box_width'].setValue(1920)
    format['box_height'].setValue(1080)
    format.setInput(0, read)
    
    write = nuke.nodes.Write()
    write['file'].setValue('{save_path}')
    write['file_type'].setValue('mov')
    write['mov64_codec'].setValue('appr')
    write['mov_prores_code_profile'].setValue('ProRes 4:2:2 HQ 10-bit')
    write.setInput(0, format)
    
    nuke.execute(write, '{first_frame}', '{last_frame}')
    ```
    
    - 로컬 .nuke  에 pepper 가져오고 테스트 !
    
    ```python
    .nuke 의  init.py
    
    -------
    
    import nuke
    
    nuke.pluginAddPath("./python")
    nuke.pluginAddPath("/home/rapa/git/hook/python/pepper")
    nuke.pluginAddPath("/mnt/pipeline/packages/int/gazu/0.8.34/d49b50d233fb55275805dbdf0d9ec779d80cb278/python")
    nuke.pluginAddPath("/mnt/pipeline/packages/int/requests/2.28.2/32383fc90933199c950ca6823b6d1e0f634651b6/python")
    nuke.pluginAddPath("/mnt/pipeline/packages/int/urllib3/1.26.14/c90100464e7464b53ef2d620102d65c024615d9e/python")
    nuke.pluginAddPath("/mnt/pipeline/packages/int/charset_normalizer/3.0.1/aa5f91efedaf4e44f5a39182b35f43e3c6551faa/python")
    nuke.pluginAddPath("/mnt/pipeline/packages/int/idna/3.4/32383fc90933199c950ca6823b6d1e0f634651b6/python")
    nuke.pluginAddPath("/mnt/pipeline/packages/int/python_socketio/4.6.1/32383fc90933199c950ca6823b6d1e0f634651b6/python")
    nuke.pluginAddPath("/mnt/pipeline/packages/int/python_engineio/3.14.2/32383fc90933199c950ca6823b6d1e0f634651b6/python")
    
    -----
    menu.py
    -----
    
    from imp import reload
    import nuke
    import nukescripts
    
    # MENU BAR
    menu_bar = menubar.addMenu("test")
    menu_bar.addCommand("naver", "nukescripts.start('https://naver.com/')", "F4")
    # menu_bar.addCommand("kitsu", "nukescripts.start('http://192.168.3.116')", "F2")
    
    # UI TEST
    import nuke_test_1
    menu_bar.addCommand("test_1", 'reload(nuke_test_1);nuke_test_1.main()', "F5")
    
    ----
    nuke_test_1.py
    ----
    
    import sys
    import os
    from PySide2 import QtWidgets, QtCore, QtUiTools
    
    class TestUI(QtWidgets.QWidget):
    
        def __init__(self) -> None:
            super(TestUI).__init__()
            self.load_ui()
            # print(self.ui.label.text())
    
        def load_ui(self):
            script_path = os.path.realpath(__file__)
            ui_path = os.path.join(os.path.dirname(script_path), 'test_1.ui')
            ui_file = QtCore.QFile(ui_path)
            ui_file.open(QtCore.QFile.ReadOnly)
            loader = QtUiTools.QUiLoader()
            self.ui = loader.load(ui_file)
            ui_file.close()
    
    def main():
        global app
        try:
            app.ui.close()
        except:
            pass
        app = TestUI()
        app.ui.show()
    ```
