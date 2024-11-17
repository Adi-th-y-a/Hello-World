import dearpygui.dearpygui as dpg
from ._configurationTab import showConfiguration
from ._modelAnalysisTab import showModelAnalysis
from ._extractionTab import showContourExtraction
from ._filteringTab import showFiltering
from ._meshTab import showMeshGeneration
from ._thresholdingTab import showThresholding
from ._theme import setup_themes

"""
    Class Userinterface generates the frontend user-interface of simcopter program
    Frontend UI is developed using Python DearPyGUI (DPG) package.
     
"""
class Userinterface:

    """
        Define the callback parameters and set the function show.
    """
    def __init__(self, callbacks) -> None:
        self.callbacks = callbacks
        self.show()
        pass

    """
        Create DPG context and window and invokes showTabBar function to render each of the tabs and their contents.
    """
    def show(self):
        dpg.create_context()
        dpg.create_viewport(title='SIMCOPTER - Generic Rotorcraft Development Framework', 
                            x_pos=0, y_pos=0, width=1920, height=1080, min_height=600, min_width=900)

        with dpg.window(tag="Main"):
            setup_themes()
            self.showTabBar()
            self.showMenuBar()
            # self.createSaveImageDialog()
            pass
        
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("Main", True)
        dpg.start_dearpygui()
        dpg.destroy_context()
        pass
    
    """
        Render the menu bar
    """
    def showMenuBar(self):
        with dpg.menu_bar():
            self.showMenus()
        pass

    """
        Render the tab bar
    """
    def showTabBar(self):
        with dpg.tab_bar():
            self.showTabs()
        pass
    
# =============================================================================
#     Create the dropdown menus
# =============================================================================
    def showMenus(self):
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="New...")
            dpg.add_menu_item(label="Open...")
            dpg.add_menu_item(label="Save")
            dpg.add_menu_item(label="Save as...")
        with dpg.menu(label="Edit"):
            dpg.add_menu_item(label="Item 1")
            dpg.add_menu_item(label="Item 2")
        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Item 1")
            dpg.add_menu_item(label="Item 2")
        with dpg.menu(label="Help"):
            dpg.add_menu_item(label="Version")
            dpg.add_menu_item(label="About", callback=lambda:dpg.show_tool())
            dpg.add_menu_item(label="Metrics", callback=lambda:dpg.show_tool(dpg.mvTool_Metrics))
            dpg.add_menu_item(label="Shortcuts")
        with dpg.menu(label="Full Screen"):
            dpg.add_menu_item(label="Toggle Fullscreen", callback=lambda:dpg.toggle_viewport_fullscreen())
        pass

    """
        Cria as diferentes tabs do programa e chama o método show<Tab> para popular cada uma das abas.
        Processing: Importação e Cropping da imagem.
        Filtering: Ajustes em níveis de cor, brilho, contraste e blurring na imagem.
        Thresholding: Ajustes na binarização da imagem. Para que a binarização ocorra a imagem é automaticamente convertida para tons de cinza.
        Contour Extraction: Extrai o contorno dos objetos presentes na imagem binarizada. Permite a exportação do arquivo .txt com os dados do contorno.
        Mesh Generation: Gera a malha e possibilita as configurações necessária para método matemáticos com os pontos resultantes da aba anterior. Permite a importação de novos pontos.
    """
    def showTabs(self):
        dpg.add_texture_registry(show=False, tag='textureRegistry')
        with dpg.tab(label='Configuration'):
            showConfiguration(self.callbacks)
            pass
        with dpg.tab(label='Visualization'):
            # showFiltering(self.callbacks)
            
            # Geometry visualization
            # Station Diagram
            pass
        with dpg.tab(label='Model Analysis'):
            showModelAnalysis(self.callbacks)
            # Mission Specification
            # Mission Performance
            # Weight, CG, Balance
            # Aerodynamic Analysis
            # Flight Dynamic Analysis (trim, linearization, stability, time responses, frequency responses)
            # Vibratory Loads
            pass
        with dpg.tab(label='Handling Qualities'):
            pass
        with dpg.tab(label='Control Design'):
        #     showMeshGeneration(self.callbacks)
            pass
        # self.callbacks.imageProcessing.disableAllTags()
        pass
        with dpg.tab(label='Flight Simulation'):
        #     showInterpolation(self.callbacks)
            pass
        with dpg.tab(label='Flight Data Analysis'):
            # Import flight data
            # 
            # showContourExtraction(self.callbacks)
            pass

    def createSaveImageDialog(self):
        with dpg.window(label="Export Image as File", modal=False, show=False, tag="exportImageAsFile", no_title_bar=False, min_size=[600,255]):
            dpg.add_text("Name your file")
            dpg.add_input_text(tag='imageNameExportAsFile')
            dpg.add_separator()
            dpg.add_text("You MUST enter a File Name to select a directory")
            dpg.add_button(width=-1, label='Select the directory', callback=self.callbacks.imageProcessing.exportImageDirectorySelector)
            dpg.add_file_dialog(directory_selector=True, min_size=[400,300], show=False, tag='exportImageDirectorySelector', id="exportImageDirectorySelector", callback=lambda sender, app_data: self.callbacks.imageProcessing.exportImageSelectDirectory(sender, app_data))
            dpg.add_separator()
            dpg.add_text('File Name: ', tag='exportImageFileName')
            dpg.add_text('Complete Path Name: ', tag='exportImageFilePath')
            with dpg.group(horizontal=True):
                dpg.add_button(label='Save', width=-1, callback=self.callbacks.imageProcessing.exportImageAsFile)
                dpg.add_button(label='Cancel', width=-1, callback=lambda: dpg.configure_item('exportImageAsFile', show=False))
            dpg.add_text("Missing file name or directory.", tag="exportImageError", show=False)
