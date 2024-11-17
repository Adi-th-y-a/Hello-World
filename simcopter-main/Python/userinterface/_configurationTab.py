import dearpygui.dearpygui as dpg

_YELLOW = (255,255,128)
_CYAN = (0,255,255)
_WHITE = (255,255,255)

_DATAINDENT = 300
_DATAHSPACE = 150
_DATAVSPACE = 7
_TABLEHGT = 60
_TwoColWid = 450
_ThreeColWid = 300
_FourColWid = 300

def showConfiguration(callbacks):
    
    
    # dpg.show_font_manager()
    # dpg.show_style_editor()
    with dpg.group(horizontal=True):
        with dpg.child_window(width=350) as _DataListParent:
            
            # with dpg.file_dialog(directory_selector=False, min_size=[400,300], show=False, tag='file_dialog_id', callback=callbacks.imageProcessing.openFile, cancel_callback=callbacks.imageProcessing.cancelImportImage):
            #     dpg.add_file_extension("", color=(150, 255, 150, 255))
            #     dpg.add_file_extension(".jpg", color=(0, 255, 255, 255))

            
            dpg.add_text('Build Configuration', color=_CYAN, indent=100)

            dpg.add_radio_button(['Select Configuration','Single Main Rotor',
                                  'Fixed Multirotor', 'Generic Rotorcraft'],
                                 default_value='Select Configuration',
                                 tag='config', callback=_selectConfig, horizontal = False)
            dpg.add_separator() 
            # dpg.add_radio_button(["New"], tag='custom', horizontal = True)
        

            with dpg.tree_node(label="Environment", tag="_config_env", default_open=True, show=False):
                with dpg.tree_node(label="Atmosphere"):
                    pass
                with dpg.tree_node(label="Terrain"):
                    pass
            with dpg.tree_node(label="Basic Data", tag="_config_basic", default_open=True, show=False):
                dpg.add_button(label="Mass & Inertia", enabled = True) # 
                
                dpg.add_button(label="Geometry", enabled = False)
            with dpg.tree_node(label="Main Rotor", tag="_config_mr", default_open=True, show=False):
                dpg.add_checkbox(label="Lead Lag Damper", callback=_selectConfig, tag="checkbox_lagdamp")
                pass
            with dpg.tree_node(label="Rotor", tag="_config_rr", default_open=True, show=False):
                pass
            with dpg.tree_node(label="Tail Rotor", tag="_config_tr", default_open=True, show=False):
                pass
            with dpg.tree_node(label="Fuselage", tag="_config_fs", default_open=True, show=False):
                pass
            with dpg.tree_node(label="Powerplant", tag="_config_pp", default_open=True, show=False):
                pass
            with dpg.tree_node(label="Control System", tag="_config_cs", default_open=True, show=False):
                pass
            with dpg.tree_node(label="Landing Gear", tag="_config_lg", default_open=True, show=False):
                pass
            with dpg.tree_node(label="External Bodies", tag="_config_eb", default_open=True, show=False):
                pass
            with dpg.tree_node(label="Lifting Surfaces", tag="_config_ls", default_open=True, show=False):
                dpg.add_checkbox(label="Horizontal Stabilizer", callback=_selectConfig, tag="checkbox_hs")
                dpg.add_checkbox(label="Vertical Stabilizer", callback=_selectConfig, tag="checkbox_vs")
                dpg.add_checkbox(label="End Plate", callback=_selectConfig, tag="checkbox_ep")
                dpg.add_checkbox(label="Wing", enabled = False)
                pass
        
            with dpg.group(tag="exportAsFileGroup", show=True):
                dpg.add_separator()
                dpg.add_text("Save Configuration", color=_YELLOW)
                dpg.add_button(tag='exportAsFile', width=-1, label='Export Configuration as XML file', callback=lambda sender, app_data: callbacks.imageProcessing.exportImage(sender, app_data, 'Processing'))

        with dpg.child_window(tag='DataInputParent', width=1520) as _DataInputParent:
            dpg.add_text('Configuration Data', color=_CYAN, indent=700)
            dpg.add_separator()
            print(dpg.get_item_rect_size(_DataInputParent))
            
            with dpg.group(tag="_data_filename", show=False):
                dpg.add_text('File', color=_YELLOW)
                with dpg.group(horizontal=False, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    dpg.add_input_text(label="File Name", tag="_filename", callback=_log, 
                                       hint="filename must be alphanumeric without spaces", width=400, no_spaces=True)
                    dpg.add_input_text(label="File Description", tag="_filedesc",
                                       hint="configuration description (max 200 characters)", width=400, multiline=True)
                    pass
                # dpg.add_button(label="Button", user_data=[_DataInputParent, _dataEnv], callback=_trackItem, enabled = True)
                dpg.add_separator()
            
            
            with dpg.group(tag="_data_env", show=False):
                
                dpg.add_text('Environment Data', color=_YELLOW)
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    dpg.add_input_text(label="Air density (kg/m3)", tag="_RHO", callback=_log, default_value="1.225", width=100, decimal=True)
                    pass
                # dpg.add_button(label="Button", user_data=[_DataInputParent, _dataEnv], callback=_trackItem, enabled = True)
                dpg.add_separator()
            
            with dpg.group(tag="_data_basic", show=False):
                dpg.add_text('Mass & Inertia Data', color=_YELLOW, bullet=False)
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_ThreeColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_ThreeColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_ThreeColWid)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Mass of Aircraft (kg)", tag="_MH", hint="MH", width=100, decimal=True)
                            dpg.add_input_text(label="Mass of MR blade (kg)", hint="MB", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="IXX (kg-m²)", tag="_IXX", hint="IXX", width=100, decimal=True)
                            with dpg.tooltip(parent="_IXX"):
                                dpg.add_text("Moment of Inertia about X-axis")

                            dpg.add_input_text(label="IYY (kg-m²)", tag="_IYY", hint="IYY", width=100, decimal=True)
                            with dpg.tooltip(parent="_IYY"):
                                dpg.add_text("Moment of Inertia about Y-axis")

                            dpg.add_input_text(label="IZZ (kg-m²)", tag="_IZZ", hint="IZZ", width=100, decimal=True)
                            with dpg.tooltip(parent="_IZZ"):
                                dpg.add_text("Moment of Inertia about Z-axis")

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="IXY (kg-m²)", tag="_IXY", hint="IXY", width=100, decimal=True)
                            with dpg.tooltip(parent="_IXY"):
                                dpg.add_text("Product of inertia with respect to the X and Y axes")

                            dpg.add_input_text(label="IYZ (kg-m²)", tag="_IYZ", hint="IYZ", width=100, decimal=True)
                            with dpg.tooltip(parent="_IYZ"):
                                dpg.add_text("Product of inertia with respect to the Y and Z axes")

                            dpg.add_input_text(label="IXZ (kg-m²)", tag="_IXZ", hint="IXZ", width=100, decimal=True)
                            with dpg.tooltip(parent="_IXZ"):
                                dpg.add_text("Product of inertia with respect to the X and Z axes")
                    
                dpg.add_separator()
            
                dpg.add_text('Geometry Data', color=_YELLOW, bullet=False) #indent=50
 
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_FourColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_FourColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_FourColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_FourColWid)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_text('Main Rotor Position from Origin', color=_WHITE)
                            dpg.add_input_text(label="X-MR (m)", tag="_XMR", hint="XMR", width=100, decimal=True)
                            dpg.add_input_text(label="Y-MR (m)", tag="_YMR", hint="YMR", width=100, decimal=True)
                            dpg.add_input_text(label="Z-MR (m)", tag="_ZMR", hint="ZMR", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_text('Tail Rotor Position from Origin', color=_WHITE)
                            dpg.add_input_text(label="X-TR (m)", tag="_XTR", hint="XTR", width=100, decimal=True)
                            dpg.add_input_text(label="Y-TR (m)", tag="_YTR", hint="YTR", width=100, decimal=True)
                            dpg.add_input_text(label="Z-TR (m)", tag="_ZTR", hint="ZTR", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_text('Fuselage Aero Center from Origin', color=_WHITE)
                            dpg.add_input_text(label="X-FS (m)", tag="_XFS", hint="XFS", width=100, decimal=True)
                            dpg.add_input_text(label="Y-FS (m)", tag="_YFS", hint="YFS", width=100, decimal=True)
                            dpg.add_input_text(label="Z-FS (m)", tag="_ZFS", hint="ZFS", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT, tag='data_geom_hs', show=False):
                            dpg.add_text('Horiz. Stabilizer Position from Origin', color=_WHITE)
                            dpg.add_input_text(label="X-HS (m)", tag="_XHS", hint="XHS", width=100, decimal=True)
                            dpg.add_input_text(label="Y-HS (m)", tag="_YHS", hint="YHS", width=100, decimal=True)
                            dpg.add_input_text(label="Z-HS (m)", tag="_ZHS", hint="ZHS", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT, tag='data_geom_vs', show=False):
                            dpg.add_text('Verical Stabilizer Position from Origin', color=_WHITE)
                            dpg.add_input_text(label="X-VS (m)", tag="_XVS", hint="XVS", width=100, decimal=True)
                            dpg.add_input_text(label="Y-VS (m)", tag="_YVS", hint="YVS", width=100, decimal=True)
                            dpg.add_input_text(label="Z-VS (m)", tag="_ZVS", hint="ZVS", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT, tag='data_geom_ep', show=False):
                            dpg.add_text('End Plate Position from Origin', color=_WHITE)
                            dpg.add_input_text(label="X-EP (m)", tag="_XEP", hint="XEP", width=100, decimal=True)
                            dpg.add_input_text(label="Y-EP (m)", tag="_YEP", hint="YEP", width=100, decimal=True)
                            dpg.add_input_text(label="Z-EP (m)", tag="_ZEP", hint="ZEP", width=100, decimal=True)
                            
                dpg.add_separator()

        
            with dpg.group(tag="_data_mr", show=False):
                dpg.add_text('Main Rotor Data', color=_YELLOW, bullet=False)
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Number of blades", tag="_NBMR", hint="NBMR", width=100, decimal=True)
                            dpg.add_input_text(label="Main Rotor radius (m)", tag="_RADMR", hint="RADMR", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Nominal angular velocity (rad/s)", tag="_OM0MR", hint="OM0MR", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Minimum angular velocity (rad/s)", tag="_OM1MR", hint="OM1MR", width=100, decimal=True)
                            dpg.add_input_text(label="Maximum angular velocity (rad/s)", tag="_OM2MR", hint="OM2MR", width=100, decimal=True)

                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    dpg.add_text("Direction of Rotation")
                    dpg.add_radio_button(["Clockwise", "Anticlockwise"], tag='_DIRMR', 
                                          horizontal = True, default_value='Anticlockwise')

                dpg.add_spacer(height=_DATAVSPACE)
                
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Mass moment of inertia (kg-m)", tag="_MBETAMR", hint="MBETAMR", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Flap moment of inertia (kg-m²)", tag="_IBETAMR", hint="IBETAMR", width=100, decimal=True)
                            dpg.add_input_text(label="Lag moment of inertia (km-m²)", tag="_IZETAMR", hint="IZETAMR",width=100, decimal=True)
                
                

                with dpg.group(horizontal=True):
                    dpg.add_text("Blade Mass & Geometry")
                    dpg.add_radio_button(["Scalar Values", "Blade Element Table"], tag='_MRGeomRadio', 
                                          horizontal = True, callback=_selectMRData, default_value='Scalar Values',
                                          indent=_DATAINDENT)

                dpg.add_spacer(height=_DATAVSPACE)
                
                with dpg.group(horizontal=True, tag="_MRGeomScalars", horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Root chord (m)", tag="_CMR", hint="CMR", width=100, decimal=True)
                            dpg.add_input_text(label="Tip chord (m)", tag="_CTIPMR", hint="CTIPMR", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Taper position (%R)", tag="_THTPMR", hint="THTPMR", width=100, decimal=True)
                            with dpg.tooltip(parent="_THTPMR"):
                                dpg.add_text("Spanwise taper")

                            dpg.add_input_text(label="Linear geometric twist (rad)", tag="_THTWMR", hint="THTWMR", width=100, decimal=True)
                            with dpg.tooltip(parent="_THTWMR"):
                                dpg.add_text("Spanwise twist")

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Mass per unit length (kg/m)", tag="_MBR", hint="MBR", width=100, decimal=True)
                            dpg.add_input_text(label="Tip mass (kg)", tag="_MBTIP", hint="MBTIP", width=100, decimal=True)

                
                with dpg.group(horizontal=True, tag="_MRGeomLookup", show=False):
                    with dpg.file_dialog(label="Select File", width=600, height=400, show=False, callback=lambda s, a, u : print(s, a[1], u), tag="_MRGeom_filedialog"):
                        dpg.add_file_extension(".*", color=(255, 255, 255, 255))
                        dpg.add_file_extension("Data files (*.xls *.xlsx){.xls,.xlsx}", color=(0, 255, 255, 255))
                        dpg.add_file_extension(".xls", color=(255, 255, 0, 255), custom_text="Excel")
                        dpg.add_file_extension(".xlsx", color=(255, 0, 255, 255), custom_text="Excel")
                    
                    dpg.add_button(label="Select Blade Geometry File", user_data=dpg.last_container(), 
                                callback=lambda s, a, u: dpg.configure_item(u, show=True),  indent=_DATAINDENT)
                    
                dpg.add_spacer(height=_DATAVSPACE)
                with dpg.group(horizontal=True, tag="_MRGeomScalars4", horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Rotor center to blade attachment (m)", tag="_AGEOMMR", hint="AGEOMMR", width=100, decimal=True)
                            dpg.add_input_text(label="Rotor center to flapping hinge (m)", tag="_ABETAMR", hint="ABETAMR", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Rotor center to lagging hinge (m)", tag="_AZETAMR", hint="AZETAMR", width=100, decimal=True)
                            dpg.add_input_text(label="Rotor center to torsion hinge (m)", tag="_ATETAMR", hint="ATETAMR", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Shaft forward tilt angle (rad)", tag="_GAMLONMR", hint="GAMLONMR", width=100, decimal=True)
                            dpg.add_input_text(label="Shaft lateral tilt angle (rad)", tag="_GAMLATMR", hint="GAMLATMR", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Swashplate phasing angle (rad)", tag="_DELSPMR", hint="DELSPMR", width=100, decimal=True)
                            dpg.add_input_text(label="Delta 3 angle (rad)", tag="_DEL3MR", hint="DEL3MR", width=100, decimal=True)
                    
                
                with dpg.group(horizontal=True):
                    dpg.add_text("Blade Polars")
                    dpg.add_radio_button(["Scalar Values", "Lookup Table"], tag='_PolarsRadio', 
                                          horizontal = True, callback=_selectMRData, default_value='Scalar Values',
                                          indent=_DATAINDENT)
                    pass
                dpg.add_spacer(height=_DATAVSPACE)
                
                
                with dpg.group(horizontal=True, tag="_MRpolarsScalars", horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Lift curve slope (1/rad)", tag="_CLAMR", hint="CLAMR", width=100, decimal=True)
                            with dpg.tooltip(parent="_CLAMR"):
                                dpg.add_text("Span-wise airfoil lift polar as function of Angle of Attack and Mach number")
                            dpg.add_input_text(label="Drag coefficient (-)", tag="_CD0MR", hint="CD0MR",width=100, decimal=True)
                            with dpg.tooltip(parent="_CD0MR"):
                                dpg.add_text("Span-wise airfoil drag polar as function of Angle of Attack and mach number")
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Pitching moment coefficient (1/rad)", tag="_CMMR", hint="CMMR", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Zero lift angle of attack (rad)", tag="_CLAL0MR", hint="CLAL0MR", width=100, decimal=True)
                            dpg.add_input_text(label="Zero pitch moment angle of attack (rad)", tag="_CMAL0MR", hint="CMAL0MR", width=100, decimal=True)


                with dpg.group(horizontal=True, tag="_MRpolarsLookup", show=False):
                    with dpg.file_dialog(label="Select File", width=600, height=400, show=False, callback=lambda s, a, u : print(s, a, u), tag="_MRPolar_filedialog"):
                        dpg.add_file_extension(".*", color=(255, 255, 255, 255))
                        dpg.add_file_extension("Data files (*.xls *.xlsx){.xls,.xlsx}", color=(0, 255, 255, 255))
                        dpg.add_file_extension(".xls", color=(255, 255, 0, 255), custom_text="Excel")
                        dpg.add_file_extension(".xlsx", color=(255, 0, 255, 255), custom_text="Excel")
                    
                    dpg.add_button(label="Select Blade Polar File", user_data=dpg.last_container(), 
                                callback=lambda s, a, u: dpg.configure_item(u, show=True),  indent=_DATAINDENT)
                    
                dpg.add_text("Blade Dynamic Characteristics")
                
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_ThreeColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_ThreeColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_ThreeColWid)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Flap damping constant", tag="_CDBETAMR", hint="CDBETAMR", width=100, decimal=True)
                            dpg.add_input_text(label="Lag damping constant", tag="_CDZETAMR", hint="CDZETAMR", width=100, decimal=True)
                            dpg.add_input_text(label="Torsion damping const.", tag="_CDTETAMR", hint="CDTETAMR", width=100, decimal=True)
                        with dpg.table_row(height=_TABLEHGT, tag='data_lagdamp', show=False):
                            dpg.add_input_text(label="Lag damper force constant", tag="_CLAGMR", hint="CLAGMR", width=100, decimal=True)
                            dpg.add_input_text(label="Lag damper stiffness", tag="_KLAGMR", hint="KLAGMR", width=100, decimal=True)
                            dpg.add_input_text(label="Zero spring force", tag="_ZETA0MR", hint="ZETA0MR", width=100, decimal=True)
                
                dpg.add_separator()

            with dpg.group(tag="_data_tr", show=False):
                dpg.add_text('Tail Rotor Data', color=_YELLOW, bullet=False)


                dpg.add_text('Blade Specifications', color=_WHITE, bullet=False)
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Number of Blades", tag="_NBTR", hint="NBTR", width=100)
                            dpg.add_input_text(label="Tail Rotor Radius (m)", tag="_RBTR", hint="RBTR", width=100)

                dpg.add_text('Aerodynamic Properties', color=_WHITE, bullet=False)
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        with dpg.table_row(height=_TABLEHGT):

                            dpg.add_input_text(label="Cant Angle with respect to X-Z plane (rad)", tag="_CANTTR", hint="CANTTR",
                                               width=100)
                            with dpg.tooltip(parent="_CANTTR"):
                                dpg.add_text("Tail Rotor cant angle with respect to X-Z plane about X-axis")

                            dpg.add_input_text(label="Blade Root Angle (rad)", tag="_CTR", hint="CTR", width=100)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Blade Tip Angle (rad)", tag="_CTIPTR", hint="CTIPTR", width=100)
                            dpg.add_input_text(label="Solidity (-)", tag="_SIGTR", hint="SIGTR", width=100)


                dpg.add_text('Performance Metrics', color=_WHITE, bullet=False)
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)


                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Nominal Angular Velocity (rad/s)", tag="_OM0TR", hint="OM0TR",
                                               width=100)
                            dpg.add_input_text(label="Tail Rotor to Empennage Separation Distance (m)", tag="_DISTTR",
                                               hint="DISTTR", width=100)


                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    dpg.add_text("Configuration")
                    dpg.add_radio_button(["Pusher ", "Tractor"], tag="_CNFGTR",
                                         horizontal=True, default_value="Pusher")


                with dpg.group(horizontal=True, horizontal_spacing=101, indent=_DATAINDENT):
                    dpg.add_text("Direction of Rotation")
                    dpg.add_radio_button(["Upward", "Downward"], tag="_DIRTR",
                                         horizontal=True, default_value="Anti-Clockwise")
                    with dpg.tooltip(parent="_DIRTR"):
                        dpg.add_text("Blade closest to MR going (1) Upward or (2) Downward")


                dpg.add_text('Miscellaneous', color=_WHITE, bullet=False)
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Area Overlap (m²)", tag="_STR", hint="STR", width=100)
                            with dpg.tooltip(parent="_STR"):
                                dpg.add_text("Tail Rotor overlaping with Empennage")

                            dpg.add_input_text(label="Tip Loss Factor (-)", tag="_BTLTR", hint="BTLTR", width=100)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Blade Lift Curve Slope (1/rad)", tag="_CLATR", hint="CLATR",
                                               width=100)
                            dpg.add_input_text(label="Geometric Twist Distribution (rad/m)", tag="_THTWTR",
                                               hint="THTWTR", width=100)
                            with dpg.tooltip(parent="_THTWTR"):
                                dpg.add_text("Span-wise twist")


                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Pitch Bias (rad)", tag="_BIASTR", hint="BIASTR", width=100)
                            dpg.add_input_text(label="Blade Flap Moment of Inertia (kg·m²)", tag="_IBETATR", hint="IBETATR",
                                               width=100)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Co-efficient of Drag of Tail Rotor Blade", tag="_CD0TR", hint="CD0TR", width=100)
                            with dpg.tooltip(parent="_CD0TR"):
                                dpg.add_text("Span-wise airfoil drag as function of Angle of Attack and Mach Number")

                            dpg.add_input_text(label="Delta 3 Angle (rad)", tag="_DEL3TR", hint="DEL3TR", width=100)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Vertical Fin Blockage Factor", tag="_BFTR", hint="BFTR",
                                               width=100)
                            dpg.add_input_text(label="Gearing Ratio", tag="_GEARTR", hint="GEARTR", width=100)
                            with dpg.tooltip(parent="_GEARTR"):
                                dpg.add_text("OmegaTR/Omega")

                dpg.add_separator()

            with dpg.group(tag="_data_fs", show=False):
                dpg.add_text('Fuselage Data', color=_YELLOW, bullet=False)
                dpg.add_text('Aerodynamic Coefficients', color=_WHITE, bullet=False)
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)


                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Equivalent Drag (m²)", tag="_CDF", hint="CDF", width=100)
                            dpg.add_input_text(label="Co-efficient of Lift due to Angle of Attack", tag="_LAFS", hint="LAFS", width=100)


                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Co-efficient of Drag due to Angle of Attack", tag="_DAFS", hint="DAFS", width=100)
                            dpg.add_input_text(label="Side Force Coefficient", tag="_SAFS", hint="SAFS",
                                               width=100)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Co-efficient of Lift due to Angle of Sideslip", tag="_LSFS", hint="LSFS", width=100)
                            dpg.add_input_text(label="Co-efficient of Drag due to Angle of Sideslip", tag="_DSFS", hint="DSFS", width=100)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Side Force Coefficient", tag="_SSFS", hint="SSFS",
                                               width=100)
                            dpg.add_input_text(label="Pitch Moment Coefficient", tag="_PAFS", hint="PAFS",
                                               width=100)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Roll Moment Coefficient", tag="_RAFS", hint="RAFS",
                                               width=100)
                            dpg.add_input_text(label="Yaw Moment Coefficient", tag="_YAFS", hint="YAFS",
                                               width=100)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Pitch Moment Coefficient", tag="_PSFS", hint="PSFS",
                                               width=100)
                            dpg.add_input_text(label="Roll Moment Coefficient", tag="_RSFS", hint="RSFS",
                                               width=100)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Yaw Moment Coefficient", tag="_YSFS", hint="YSFS",
                                               width=100)

                dpg.add_separator()

            with dpg.group(tag="_data_hs", show=False):
                dpg.add_text('Horizontal Stabilizer Data', color=_YELLOW, bullet=False)
                dpg.add_text('Aerodynamic Properties', color=_WHITE, bullet=False)
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Zero-Lift Angle of Attack (rad)", tag="_CLAL0HS", hint="CLAL0HS",
                                               width=100)
                            dpg.add_input_text(label="Surface Area (m²)", tag="_SHS", hint="SHS", width=100)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Lift Curve Slope (1/rad)", tag="_CLAHS", hint="CLAHS", width=100)
                            with dpg.tooltip(parent="_CLAHS"):
                                dpg.add_text("Lift polar as function of Angle of Attack and Mach number")

                            dpg.add_input_text(label="Co-efficient of Drag", tag="_CD0HS", hint="CD0HS", width=100)
                            with dpg.tooltip(parent="_CD0VS"):
                                dpg.add_text("Spanwise airfoil drag polar as function of Angle of Attack and Mach number")

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Default Angle of Attack (rad)", tag="_ALPHA0HS", hint="ALPHA0HS",
                                               width=100)
                            dpg.add_input_text(label="Downwash Factor", tag="_KLAMHS", hint="KLAMHS",
                                               width=100)
                            with dpg.tooltip(parent="_KLAMHS"):
                                dpg.add_text("Main Rotor to Horizontal Surface Downwash Factor")

                dpg.add_separator()

            with dpg.group(tag="_data_vs", show=False):
                dpg.add_text('Vertical Stabilizer Data', color=_YELLOW, bullet=False)
                dpg.add_text('Aerodynamic Properties', color=_WHITE, bullet=False)
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    with dpg.table(header_row=False):
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)
                        dpg.add_table_column(width_fixed=True, init_width_or_weight=_TwoColWid)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Zero-Lift Angle of Attack (rad)", tag="_CLAL0VS", hint="CLAL0VS",
                                               width=100)
                            dpg.add_input_text(label="Surface Area (m²)", tag="_SVS", hint="SVS", width=100)

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Lift Curve Slope (1/rad)", tag="_CLAVS", hint="CLAVS", width=100)
                            dpg.add_input_text(label="Co-efficient of Drag", tag="_CD0VS", hint="CD0VS", width=100)
                            with dpg.tooltip(parent="_CD0VS"):
                                dpg.add_text("Spanwise airfoil drag polar as function of Angle of Attack and Mach number")

                        with dpg.table_row(height=_TABLEHGT):
                            dpg.add_input_text(label="Default Angle of Attack (rad)", tag="_ALPHA0VS", hint="ALPHA0VS",
                                               width=100)

                dpg.add_separator()

            with dpg.group(tag="_data_lg", show=False):
                dpg.add_text('Landing Gear Data', color=_WHITE, bullet=True)
                with dpg.group(horizontal=True):
                    dpg.add_input_text(label="Spring stiffness (Nm/rad)", tag="_CKLG", width=100, decimal=True)
                pass
                dpg.add_separator()
                
            # with dpg.group(show=True):
            #     dpg.add_text('Component Data')
            #     with dpg.group(horizontal=True):
            #         dpg.add_input_text(label="XYZ ", width=100, decimal=True)
            #     pass
            #     dpg.add_separator()
                
            # with dpg.group(show=True):
            #     dpg.add_text('Component Data')
            #     with dpg.group(horizontal=True):
            #         dpg.add_input_text(label="XYZ ", width=100, decimal=True)
            #     pass
            #     dpg.add_separator()
                

            with dpg.group(tag="_data_end", show=False) as _dataEnd:
                dpg.add_button(label="Go to Top", user_data=[_DataInputParent, _dataEnd], 
                               callback=_trackItem, enabled = True)
                
                with dpg.file_dialog(directory_selector=False, show=False, callback=callbacks.save_data, tag="file_dialog_tag", width=700, height=400):
                    dpg.add_file_extension(".csv")  

                dpg.add_button(label="Save Data", callback=lambda: dpg.show_item("file_dialog_tag"))  
                    
                with dpg.file_dialog(directory_selector=False, show=False, callback=callbacks.load_data, tag="load_file_dialog", width=700, height=400):
                    dpg.add_file_extension(".csv")
                    
                dpg.add_button(tag='loadFile', label='Load Data', callback=lambda: dpg.show_item("load_file_dialog"))

def _config(sender, keyword, user_data):
    widget_type = dpg.get_item_type(sender)
    items = user_data

    if widget_type == "mvAppItemType::mvRadioButton":
        value = True
    else:
        keyword = dpg.get_item_label(sender)
        value = dpg.get_value(sender)

    if isinstance(user_data, list):
        for item in items:
            dpg.configure_item(item, **{keyword: value})
    else:
        dpg.configure_item(items, **{keyword: value})
    
def _selectConfig(sender, app_data, user_data):
    print(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")
    
    if sender=='config':
        dpg.configure_item("_data_filename", show=True)
        dpg.configure_item("_config_env", show=True)
        dpg.configure_item("_data_env", show=True)
        dpg.configure_item("_data_hs", show=True)
        dpg.configure_item("_data_vs", show=True)
        dpg.configure_item("_config_basic", show=True)
        dpg.configure_item("_data_basic", show=True)
        dpg.configure_item("_config_fs", show=True)
        dpg.configure_item("_data_fs", show=True)
        dpg.configure_item("_data_end", show=True)
        if app_data == 'Single Main Rotor':
            dpg.configure_item("_config_rr", show=False)
            dpg.configure_item("_config_mr", show=True)
            dpg.configure_item("_data_mr", show=True)
            dpg.configure_item("_config_tr", show=True)
            dpg.configure_item("_data_tr", show=True)
            # dpg.configure_item("_config_hs", show=True)
            # dpg.configure_item("_config_vs", show=True)
            dpg.configure_item("_config_lg", show=True)
            dpg.configure_item("_config_ls", show=True)
            pass
        elif app_data == 'Fixed Multirotor':
            dpg.configure_item("_config_rr", show=True)
            dpg.configure_item("_config_mr", show=False)
            dpg.configure_item("_data_mr", show=False)
            dpg.configure_item("_config_tr", show=False)
            # dpg.configure_item("_config_hs", show=True)
            # dpg.configure_item("_config_vs", show=True)
            dpg.configure_item("_config_lg", show=True)
            pass
        dpg.configure_item("config", enabled=False)
    
    if sender=='checkbox_hs':
        dpg.configure_item("data_geom_hs", show=app_data)    
    if sender=='checkbox_vs':
        dpg.configure_item("data_geom_vs", show=app_data)    
    if sender=='checkbox_ep':
        dpg.configure_item("data_geom_ep", show=app_data)    
    if sender=='checkbox_lagdamp':
        dpg.configure_item("data_lagdamp", show=app_data)
    
    pass

def _selectMRData(sender, app_data, user_data):
    if sender=='_PolarsRadio' and app_data=='Scalar Values':
        dpg.configure_item("_MRpolarsScalars", show=True)
        dpg.configure_item("_MRpolarsLookup", show=False)
        pass
    elif sender=='_PolarsRadio' and app_data=='Lookup Table':
        dpg.configure_item("_MRpolarsScalars", show=False)
        dpg.configure_item("_MRpolarsLookup", show=True)
        pass
    if sender=='_MRGeomRadio' and app_data=='Scalar Values':
        dpg.configure_item("_MRGeomScalars", show=True)
        dpg.configure_item("_MRGeomLookup", show=False)
        pass
    elif sender=='_MRGeomRadio' and app_data=='Blade Element Table':
        dpg.configure_item("_MRGeomScalars", show=False)
        dpg.configure_item("_MRGeomLookup", show=True)
        pass
    pass

def _log(sender, app_data, user_data):
    print(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")
    
    
def _trackItem(sender, app_data, user_data):
# Format of user_data=[Window Item, Widget Item]

    _, y_window = dpg.get_item_pos(user_data[0])
    _, y_widget = dpg.get_item_pos(user_data[1])
    print("Widget scroll position is:")
    # print(dpg.get_y_scroll(user_data[0]))
    print(dpg.get_y_scroll(user_data[0]))
    # dpg.set_y_scroll(user_data, 500)
    print("window position is: ")
    print(y_window)
    print("Widget position is: ")
    print(y_widget)
    print("Y scroll max is: ")
    print(dpg.get_y_scroll_max(user_data[0]))
    print(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")
    
    if user_data[1] == "_data_end":
        dpg.set_y_scroll(user_data[0], 0)
    else:
        dpg.set_y_scroll(user_data[0], y_widget)
    pass
