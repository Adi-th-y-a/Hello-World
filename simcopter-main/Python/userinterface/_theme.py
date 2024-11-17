import dearpygui.dearpygui as dpg
import platform
import os

def get_correct_path(relative_path):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative_path
    )

def setup_themes():

    dpg.set_viewport_small_icon("icons/Icon.ico")
    dpg.set_viewport_large_icon("icons/Icon.ico")

    with dpg.theme() as global_theme:
        with dpg.theme_component(0):
            # Main Styles
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 8, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 20, 4)
            dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 4, 2)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 20, 10)
            dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing, 4, 4)
            dpg.add_theme_style(dpg.mvStyleVar_IndentSpacing, 20)
            dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 14)
            dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize, 20)

            # Border Styles
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 10)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 1)
            dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, 1)
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1)

            # Rounding Style
            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 12)
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 12)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
            dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 12)
            dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 9)
            dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 12)
            dpg.add_theme_style(dpg.mvStyleVar_TabRounding, 12)

        dpg.bind_theme(global_theme)
        
    with dpg.theme(tag="logo_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (18, 18, 19))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (18, 18, 19))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (18, 18, 19))
    
    with dpg.theme() as disabled_theme:
        with dpg.theme_component(dpg.mvInputFloat, enabled_state=False):
            dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_Button, [155, 155, 155])
    
        with dpg.theme_component(dpg.mvInputInt, enabled_state=False):
            dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_Button, [155, 155, 155])
            
    # dpg.bind_theme(disabled_theme)

    # FIXME: Blurry font on Windows with DPI scaling
    # https://github.com/hoffstadt/DearPyGui/issues/1380

    fontPath = ''
    fontPathWindows = 'fonts\OpenSans-Regular.ttf'
    fontPathLinux = 'fonts/OpenSans-Regular.ttf'

    if platform.system() == 'Windows':
        fontPath = fontPathWindows
    else:
        fontPath = fontPathLinux

    if platform.system() == 'Windows':
        fontPath = get_correct_path(fontPath)

    try:
        with dpg.font_registry():
            large_font = dpg.add_font(fontPath, 24)
            default_font = dpg.add_font(fontPath, 20)

        dpg.bind_font(default_font)
    except:
        pass