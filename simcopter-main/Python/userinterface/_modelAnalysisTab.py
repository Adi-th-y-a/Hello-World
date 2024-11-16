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

def showModelAnalysis(callbacks):
    with dpg.group(horizontal=True):
        with dpg.child_window(width=350):
            dpg.add_text('Select Analysis', color=_CYAN, indent=100)
            
            dpg.add_radio_button(['Select Analysis Type','Mission Performance',
                                  'Weight & CG', 'Flight Dynamics'],
                                 default_value='Analysis',
                                 tag='_analysisType', callback=_selectAnalysis, horizontal = False)
            dpg.add_separator()
            
            # dpg.add_listbox(tag='interpolationListbox', items=['Nearest', 'Bilinear', 'Bicubic', 'Quadratic', 'Spline3'], width=-1)
            # dpg.add_checkbox(label='Expand Dimensions', tag='resizeInterpolation')
            # dpg.add_text('Node Spacing Increment')
            # dpg.add_slider_int(tag='spacingInterpolationSlider', default_value=0, min_value=0, max_value=7, width=-1)
            # dpg.add_text('Node Removal Increment')
            # dpg.add_slider_int(tag='removalInterpolationSlider', default_value=0, min_value=0, max_value=7, width=-1)
            # dpg.add_checkbox(label='Contour Approximation', tag='approxPolyInterpolation')
            # dpg.add_slider_float(tag='approxPolySlider', default_value=0.001, min_value=0.001, max_value=0.01, width=-1)
            # dpg.add_button(tag='interpolateButton', width=-1, label='Apply Method', callback=lambda sender, app_data: callbacks.interpolation.interpolate(sender, app_data))
            # dpg.add_separator()
            # dpg.add_button(tag='interpolationToMesh', width=-1, label='Export to Mesh Generation', callback=lambda sender, app_data: callbacks.interpolation.exportToMeshGeneration(sender, app_data))
            # dpg.add_separator()
            # dpg.add_button(tag='exportContour', width=-1, label='Export Contour to File', callback=lambda sender, app_data: callbacks.interpolation.exportButtonCall(sender, app_data))
            pass

        # with dpg.window(label="Save File", modal=False, show=False, tag="exportInterpolatedContourWindow", no_title_bar=False, min_size=[600,280]):
        #     dpg.add_text("Name your file")
        #     dpg.add_input_text(tag='inputInterpolatedContourNameText')
        #     dpg.add_separator()
        #     dpg.add_text("You MUST enter a File Name to select a directory")
        #     dpg.add_button(label='Select the directory', width=-1, callback= callbacks.interpolation.openDirectorySelector)
        #     dpg.add_file_dialog(directory_selector=True, min_size=[400,300], show=False, tag='interpolatedContourDirectorySelectorFileDialog', id="interpolatedContourDirectorySelectorFileDialog", callback=callbacks.interpolation.selectFolder)
        #     dpg.add_separator()
        #     dpg.add_text('File Name: ', tag='exportInterpolatedFileName')
        #     dpg.add_text('Complete Path Name: ', tag='exportInterpolatedPathName')
        #     with dpg.group(horizontal=True):
        #         dpg.add_button(label='Save', width=-1, callback=lambda: callbacks.interpolation.exportIndividualContourToFile())
        #         dpg.add_button(label='Cancel', width=-1, callback=lambda: dpg.configure_item('exportInterpolatedContourWindow', show=False))
        #     dpg.add_text("Missing file name or directory.", tag="exportInterpolatedContourError", show=False)

        # with dpg.child_window(tag='InterpolationParent'):
        #     with dpg.plot(tag="InterpolationPlotParent", label="Interpolation Plot", height=-1 - 20, width=-1, equal_aspects=True):
        #         dpg.add_plot_legend()
        #         dpg.add_plot_axis(dpg.mvXAxis, label="x", tag="Interpolation_x_axis")
        #         dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="Interpolation_y_axis")
        #     with dpg.group(horizontal=True):
        #         dpg.add_text('Original Area: --', tag='area_before_interp')
        #         dpg.add_text('Current Area: --', tag='area_after_interp')
        #         dpg.add_text('Delta: --', tag='delta_interp')
        #     pass
    
    
        with dpg.child_window(tag='ModelAnalysisParent', width=1520) as _ModelAnalysisParent:
            dpg.add_text('Analysis Pane', color=_CYAN, indent=700)
            dpg.add_separator()
            print(dpg.get_item_rect_size(_ModelAnalysisParent))
            
            with dpg.group(tag="_analysis_trim", show=False):
                
                dpg.add_text('Trim Specifications', color=_YELLOW)
                with dpg.group(horizontal=True, horizontal_spacing=_DATAHSPACE, indent=_DATAINDENT):
                    dpg.add_input_text(label="Trim Airspeed (m/s)", tag="_TrimASPD", default_value="0", width=100, decimal=True)
                    pass
                # dpg.add_button(label="Button", user_data=[_DataInputParent, _dataEnv], callback=_trackItem, enabled = True)
                dpg.add_separator()
                
                
def _selectAnalysis(sender, app_data, user_data):
    print(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")
    
    if sender=='_analysisType':
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
        if app_data == 'Flight Dynamics':
            dpg.configure_item("_analysis_trim", show=True)
            pass
        elif app_data == 'Fixed Multirotor':
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