"""
Created on Wed Aug 21 17:41:22 2024

@author: ohalbe

Generic Rotorcraft Model User interface
Inspired from the image processing project of Rafael Casa Maximo
https://github.com/RafaelCasamaximo/contExt/tree/main

Node based control system editor based on the NodiumPy project
https://github.com/farzadshayanfar/nodiumpy/tree/master

"""

from userinterface import Userinterface
from callbacks import Callbacks

"""
    App class generates the frontend user interface to add aircraft configuration
    and interact with the backend mathematical models
"""
class App:
    def __init__(self) -> None:
        self.interface = Userinterface(Callbacks())
        pass


if __name__ == '__main__':
   app = App()
   
   



# import sys
# import numpy as np
# import dearpygui.dearpygui as dpg


# dpg.create_context()
# with dpg.font_registry():
#     default_font = dpg.add_font("fonts\OpenSans-Regular.ttf", 20)
    
# dpg.create_viewport(title = "Rotorcraft Configuration", width = 800, height = 600)

# with dpg.window(label = "Rotorcraft Configuration", width = 700, height = 500):
#     dpg.bind_font(default_font)
#     dpg.add_input_float(label = "Air Density(rho)", default_value = 1.225, tag = "rho_in")
#     dpg.add_input_int(label = "No. of Blades(Nb)", default_value = 3, tag = "Nb_in")
#     dpg.add_input_float(label = "Blade Radius 'm'", default_value = 2.2, tag = "rotor_rad_m_in")
#     dpg.add_input_float(label = "Chord Length 'm'", default_value = 0.132, tag = "blade_chord_m_in")
#     dpg.add_input_float(label = "Blade Twist 'deg'", default_value = -9.5, tag = "blade_tw_deg_in")
#     dpg.add_input_float(label = "Lift-Slope Coeff. per rad(Cl_alpha)", default_value = 0.12*180/np.pi, tag = "Cl_alpha_in")
#     dpg.add_input_float(label = "Blade Zero-Lift Drag Coeff.(Cd_0)", default_value = 0.01, tag = "Cd_0_in")
#     dpg.add_input_float(label = "Rotor Tip Velocity 'm/s'", default_value = 200, tag = "v_tip_in")
#     dpg.add_input_float(label = "Root Cutout(%)", default_value = 0.2, tag = "root_cutout_percent_in")
#     dpg.add_input_float(label = "Climb Velocity(m/s)", default_value = 0, tag = "v_climb_in")
#     dpg.add_input_float(label = "Thrust Required(N)", default_value = 250*9.80665, tag = "Thrust_req_N_in")
    
#     #   Showing Output in Interface by Calling Main Function
#     # dpg.add_button(label = "Run BEMT_estimate_climb", callback = run_BEMT_estimate_climb)   # Run
    
#     dpg.add_text(label = 'P_bemt_tip_loss', tag = "P_bemt_tip_loss")
#     dpg.add_text(label = "blade_pitch_75_tip_loss", tag = "blade_pitch_75_tip_loss")
#     dpg.add_text(label = "P_bemt", tag = "P_bemt")
#     dpg.add_text(label = "P_mom", tag = "P_mom")
#     dpg.add_text(label = "P_induced", tag = "P_induced")
#     dpg.add_text(label = "P_profile", tag = "P_profile")

# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()