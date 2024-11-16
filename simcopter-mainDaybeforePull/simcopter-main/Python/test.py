# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:32:56 2024

@author: ohalbe
"""

# import dearpygui.dearpygui as dpg

# dpg.create_context()

# # callback runs when user attempts to connect attributes
# def link_callback(sender, app_data):
#     # app_data -> (link_id1, link_id2)
#     dpg.add_node_link(app_data[0], app_data[1], parent=sender)

# # callback runs when user attempts to disconnect attributes
# def delink_callback(sender, app_data):
#     # app_data -> link_id
#     dpg.delete_item(app_data)

# with dpg.window(label="Tutorial", width=400, height=400):

#     with dpg.node_editor(callback=link_callback, delink_callback=delink_callback):
#         with dpg.node(label="Node 1"):
#             with dpg.node_attribute(label="Node A1"):
#                 dpg.add_input_float(label="F1", width=150)

#             with dpg.node_attribute(label="Node A2", attribute_type=dpg.mvNode_Attr_Output):
#                 dpg.add_input_float(label="F2", width=150)

#         with dpg.node(label="Node 2"):
#             with dpg.node_attribute(label="Node A3"):
#                 dpg.add_input_float(label="F3", width=200)

#             with dpg.node_attribute(label="Node A4", attribute_type=dpg.mvNode_Attr_Output):
#                 dpg.add_input_float(label="F4", width=200)

# dpg.create_viewport(title='Custom Title', width=800, height=600)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()


# DPG DEMO
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=1080, height=800)

demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()



# ## Create new window in callback
# import dearpygui.dearpygui as dpg

# item_table = []

# #builts the context window
# dpg.create_context()
# dpg.create_viewport(title="invengo", width=600, height=600)

# #outputs the data from the inputs and callbacks
# def reg(sender):
#     print(dpg.get_value(sender))
#     item_table.append(dpg.get_value(sender))

# def lel(sender):
#     with dpg.window():
#         pass
        

# #builts the datainputs 
# with dpg.window(tag="PW"):
#     item_name = dpg.add_input_text(label="Gegenstand", hint="Hier den Namen des Gegenstandes eintragen...",callback=reg, on_enter=True)
#     item_amount = dpg.add_combo(label="Menge", default_value=1, items=(1,2,3,"Mehrere"), callback=reg)
#     check_button = dpg.add_button(label="CLICK ME", callback=lel)
# dpg.set_item_callback(item_name, reg)

# #debugging
# print(dpg.get_value(item_name))

# #start the modul  
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.set_primary_window("PW", True)
# dpg.start_dearpygui()
# dpg.destroy_context()




# #### Theme for Disabled Items

# import dearpygui.dearpygui as dpg

# dpg.create_context()
# dpg.create_viewport()
# dpg.setup_dearpygui()

# with dpg.theme() as disabled_theme:
#     with dpg.theme_component(dpg.mvInputFloat, enabled_state=False):
#         dpg.add_theme_color(dpg.mvThemeCol_Text, [155, 155, 155])
#         dpg.add_theme_color(dpg.mvThemeCol_Button, [155, 155, 155])

#     with dpg.theme_component(dpg.mvInputInt, enabled_state=False):
#         dpg.add_theme_color(dpg.mvThemeCol_Text, [155, 155, 155])
#         dpg.add_theme_color(dpg.mvThemeCol_Button, [155, 155, 155])
        
# with dpg.theme() as global_theme:
#     with dpg.theme_component(dpg.mvInputFloat, enabled_state=True):
#         dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
#         dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 0, 0])

#     with dpg.theme_component(dpg.mvInputInt, enabled_state=True):
#         dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
#         dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 0, 0])

# dpg.bind_theme(disabled_theme)
# dpg.bind_theme(global_theme)

# with dpg.window(label="tutorial"):
#     dpg.add_input_float(label="Input float", enabled=True)
#     dpg.add_input_int(label="Input int", enabled=False)
#     dpg.add_button(label="Mass", enabled=False)
#     dpg.add_button(label="Inertia", enabled=False)

# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()



# # Standalone, minimal, complete and verifiable example
# import dearpygui.dearpygui as dpg

# dpg.create_context()
# dpg.create_viewport(title='Button Test', width=600, height=300)


# with dpg.theme() as disabled_theme:
#     with dpg.theme_component(dpg.mvInputFloat, enabled_state=False):
#         dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
#         dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 0, 0])

#     with dpg.theme_component(dpg.mvInputInt, enabled_state=False):
#         dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
#         dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 0, 0])

# dpg.bind_theme(disabled_theme)


def test_func():
    print("Testing Button")
    dpg.configure_item("button_item", show=False)


def test_func1():
    print("Testing Button 1")
    dpg.configure_item("button_item", show=True)
    
with dpg.window(label="button"):
    dpg.add_button(label="Test Button", callback=test_func, show=True, width=400, height=40, tag = "button_item")
    dpg.add_button(label="Test Button 1", callback=test_func1, show=True, width=400, height=40)
    # dpg.add_text(label = "test text", enabled=False)
    dpg.add_input_float(label='test text', enabled=False)
    


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()