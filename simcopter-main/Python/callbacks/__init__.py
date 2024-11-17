# from ._contourExtraction import ContourExtraction

import dearpygui.dearpygui as dpg
import csv


class Callbacks:
    def __init__(self) -> None:
        # self.contourExtraction = ContourExtraction()
        # self.meshGeneration = self.contourExtraction.meshGeneration
        # self.imageProcessing = self.contourExtraction.imageProcessing
        # self.interpolation = self.contourExtraction.interpolation
        pass
    


    def save_data(self, sender, app_data):
        data = {
            "MH (kg)": dpg.get_value('_MH'),
            "RHO (kg/m³)": dpg.get_value('_RHO'),
            "IXX (kg·m²)": dpg.get_value('_IXX'),
            "IYY (kg·m²)": dpg.get_value('_IYY'),
            "IZZ (kg·m²)": dpg.get_value('_IZZ'),
            "IXY (kg·m²)": dpg.get_value('_IXY'),
            "IYZ (kg·m²)": dpg.get_value('_IYZ'),
            "IXZ (kg·m²)": dpg.get_value('_IXZ'),
            "XMR (m)": dpg.get_value('_XMR'),
            "YMR (m)": dpg.get_value('_YMR'),
            "ZMR (m)": dpg.get_value('_ZMR'),
            "XTR (m)": dpg.get_value('_XTR'),
            "YTR (m)": dpg.get_value('_YTR'),
            "ZTR (m)": dpg.get_value('_ZTR'),
            "XFS (m)": dpg.get_value('_XFS'),
            "YFS (m)": dpg.get_value('_YFS'),
            "ZFS (m)": dpg.get_value('_ZFS'),
            "XHS (m)": dpg.get_value('_XHS'),
            "YHS (m)": dpg.get_value('_YHS'),
            "ZHS (m)": dpg.get_value('_ZHS'),
            "XVS (m)": dpg.get_value('_XVS'),
            "YVS (m)": dpg.get_value('_YVS'),
            "ZVS (m)": dpg.get_value('_ZVS'),
            "XEP (m)": dpg.get_value('_XEP'),
            "YEP (m)": dpg.get_value('_YEP'),
            "ZEP (m)": dpg.get_value('_ZEP'),
            "NBMR": dpg.get_value('_NBMR'),  # No units
            "RADMR (m)": dpg.get_value('_RADMR'),
            "OM0MR (rad/s)": dpg.get_value('_OM0MR'),
            "OM1MR (rad/s)": dpg.get_value('_OM1MR'),
            "OM2MR (rad/s)": dpg.get_value('_OM2MR'),
            "DIRMR (°)": dpg.get_value('_DIRMR'),
            "MBETAMR (°)": dpg.get_value('_MBETAMR'),
            "IBETAMR (°)": dpg.get_value('_IBETAMR'),
            "IZETAMR (°)": dpg.get_value('_IZETAMR'),
            "CMR (N·m)": dpg.get_value('_CMR'),
            "CTIPMR": dpg.get_value('_CTIPMR'),  # No units
            "THTPMR (°)": dpg.get_value('_THTPMR'),
            "THTWMR (°)": dpg.get_value('_THTWMR'),
            "MBR (kg)": dpg.get_value('_MBR'),
            "MBTIP (kg)": dpg.get_value('_MBTIP'),
            "AGEOMMR (m²)": dpg.get_value('_AGEOMMR'),
            "ABETAMR (°)": dpg.get_value('_ABETAMR'),
            "AZETAMR (°)": dpg.get_value('_AZETAMR'),
            "ATETAMR (°)": dpg.get_value('_ATETAMR'),
            "GAMLONMR (°)": dpg.get_value('_GAMLONMR'),
            "GAMLATMR (°)": dpg.get_value('_GAMLATMR'),
            "DELSPMR (°)": dpg.get_value('_DELSPMR'),
            "DEL3MR (°)": dpg.get_value('_DEL3MR'),
            "CLAMR": dpg.get_value('_CLAMR'),  # No units
            "CD0MR": dpg.get_value('_CD0MR'),  # No units
            "CMMR": dpg.get_value('_CMMR'),    # No units
            "CLAL0MR": dpg.get_value('_CLAL0MR'),  # No units
            "CMAL0MR": dpg.get_value('_CMAL0MR'),  # No units
            "CDBETAMR": dpg.get_value('_CDBETAMR'),  # No units
            "CDZETAMR": dpg.get_value('_CDZETAMR'),  # No units
            "CDTETAMR": dpg.get_value('_CDTETAMR'),  # No units
            "CLAGMR": dpg.get_value('_CLAGMR'),  # No units
            "KLAGMR": dpg.get_value('_KLAGMR'),  # No units
            "ZETA0MR (°)": dpg.get_value('_ZETA0MR'),
            "NBTR": dpg.get_value('_NBTR'),  # No units
            "RBTR (m)": dpg.get_value('_RBTR'),
            "CANTTR (°)": dpg.get_value('_CANTTR'),
            "CTR": dpg.get_value('_CTR'),  # No units
            "CTIPTR": dpg.get_value('_CTIPTR'),  # No units
            "SIGTR": dpg.get_value('_SIGTR'),  # No units
            "OM0TR (rad/s)": dpg.get_value('_OM0TR'),
            "DISTTR (m)": dpg.get_value('_DISTTR'),
            "CNFGTR": dpg.get_value('_CNFGTR'),  # No units
            "DIRTR (°)": dpg.get_value('_DIRTR'),
            "STR": dpg.get_value('_STR'),  # No units
            "BTLTR (°)": dpg.get_value('_BTLTR'),
            "CLATR": dpg.get_value('_CLATR'),  # No units
            "THTWTR (°)": dpg.get_value('_THTWTR'),
            "BIASTR": dpg.get_value('_BIASTR'),  # No units
            "IBETATR (°)": dpg.get_value('_IBETATR'),
            "CD0TR": dpg.get_value('_CD0TR'),  # No units
            "DEL3TR (°)": dpg.get_value('_DEL3TR'),
            "BFTR": dpg.get_value('_BFTR'),  # No units
            "GEARTR": dpg.get_value('_GEARTR'),  # No units
            "CDF": dpg.get_value('_CDF'),  # No units
            "LAFS (m²)": dpg.get_value('_LAFS'),
            "DAFS (m²)": dpg.get_value('_DAFS'),
            "SAFS (m²)": dpg.get_value('_SAFS'),
            "LSFS (m²)": dpg.get_value('_LSFS'),
            "DSFS (m²)": dpg.get_value('_DSFS'),
            "SSFS (m²)": dpg.get_value('_SSFS'),
            "PAFS (N·m)": dpg.get_value('_PAFS'),
            "RAFS (N·m)": dpg.get_value('_RAFS'),
            "YAFS (°)": dpg.get_value('_YAFS'),
            "PSFS (°/s)": dpg.get_value('_PSFS'),
            "RSFS (°/s)": dpg.get_value('_RSFS'),
            "YSFS (°/s)": dpg.get_value('_YSFS'),
            "CLAL0HS": dpg.get_value('_CLAL0HS'),  # No units
            "SHS (m²)": dpg.get_value('_SHS'),
            "CLAHS": dpg.get_value('_CLAHS'),  # No units
            "CD0HS": dpg.get_value('_CD0HS'),  # No units
            "ALPHA0HS (°)": dpg.get_value('_ALPHA0HS'),
            "KLAMHS": dpg.get_value('_KLAMHS'),  # No units
            "CLAL0VS": dpg.get_value('_CLAL0VS'),  # No units
            "SVS (m²)": dpg.get_value('_SVS'),
            "CLAVS": dpg.get_value('_CLAVS'),  # No units
            "CD0VS": dpg.get_value('_CD0VS'),  # No units
            "ALPHA0VS (°)": dpg.get_value('_ALPHA0VS'),
            "CKLG": dpg.get_value('_CKLG')  # No units
        }
        
    
        file_path = app_data['file_path_name']
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in data.items():
                writer.writerow([key, value])
                
    def load_data(self, sender, app_data):
        # Define a mapping from CSV labels to internal tags
        label_to_tag = {
            "MH (kg)": "_MH",
            "RHO (kg/m³)": "_RHO",
            "IXX (kg·m²)": "_IXX",
            "IYY (kg·m²)": "_IYY",
            "IZZ (kg·m²)": "_IZZ",
            "IXY (kg·m²)": "_IXY",
            "IYZ (kg·m²)": "_IYZ",
            "IXZ (kg·m²)": "_IXZ",
            "XMR (m)": "_XMR",
            "YMR (m)": "_YMR",
            "ZMR (m)": "_ZMR",
            "XTR (m)": "_XTR",
            "YTR (m)": "_YTR",
            "ZTR (m)": "_ZTR",
            "XFS (m)": "_XFS",
            "YFS (m)": "_YFS",
            "ZFS (m)": "_ZFS",
            "XHS (m)": "_XHS",
            "YHS (m)": "_YHS",
            "ZHS (m)": "_ZHS",
            "XVS (m)": "_XVS",
            "YVS (m)": "_YVS",
            "ZVS (m)": "_ZVS",
            "XEP (m)": "_XEP",
            "YEP (m)": "_YEP",
            "ZEP (m)": "_ZEP",
            "NBMR": "_NBMR",
            "RADMR (m)": "_RADMR",
            "OM0MR (rad/s)": "_OM0MR",
            "OM1MR (rad/s)": "_OM1MR",
            "OM2MR (rad/s)": "_OM2MR",
            "DIRMR (°)": "_DIRMR",
            "MBETAMR (°)": "_MBETAMR",
            "IBETAMR (°)": "_IBETAMR",
            "IZETAMR (°)": "_IZETAMR",
            "CMR (N·m)": "_CMR",
            "CTIPMR": "_CTIPMR",
            "THTPMR (°)": "_THTPMR",
            "THTWMR (°)": "_THTWMR",
            "MBR (kg)": "_MBR",
            "MBTIP (kg)": "_MBTIP",
            "AGEOMMR (m²)": "_AGEOMMR",
            "ABETAMR (°)": "_ABETAMR",
            "AZETAMR (°)": "_AZETAMR",
            "ATETAMR (°)": "_ATETAMR",
            "GAMLONMR (°)": "_GAMLONMR",
            "GAMLATMR (°)": "_GAMLATMR",
            "DELSPMR (°)": "_DELSPMR",
            "DEL3MR (°)": "_DEL3MR",
            "CLAMR": "_CLAMR",
            "CD0MR": "_CD0MR",
            "CMMR": "_CMMR",
            "CLAL0MR": "_CLAL0MR",
            "CMAL0MR": "_CMAL0MR",
            "CDBETAMR": "_CDBETAMR",
            "CDZETAMR": "_CDZETAMR",
            "CDTETAMR": "_CDTETAMR",
            "CLAGMR": "_CLAGMR",
            "KLAGMR": "_KLAGMR",
            "ZETA0MR (°)": "_ZETA0MR",
            "NBTR": "_NBTR",
            "RBTR (m)": "_RBTR",
            "CANTTR (°)": "_CANTTR",
            "CTR": "_CTR",
            "CTIPTR": "_CTIPTR",
            "SIGTR": "_SIGTR",
            "OM0TR (rad/s)": "_OM0TR",
            "DISTTR (m)": "_DISTTR",
            "CNFGTR": "_CNFGTR",
            "DIRTR (°)": "_DIRTR",
            "STR": "_STR",
            "BTLTR (°)": "_BTLTR",
            "CLATR": "_CLATR",
            "THTWTR (°)": "_THTWTR",
            "BIASTR": "_BIASTR",
            "IBETATR (°)": "_IBETATR",
            "CD0TR": "_CD0TR",
            "DEL3TR (°)": "_DEL3TR",
            "BFTR": "_BFTR",
            "GEARTR": "_GEARTR",
            "CDF": "_CDF",
            "LAFS (m²)": "_LAFS",
            "DAFS (m²)": "_DAFS",
            "SAFS (m²)": "_SAFS",
            "LSFS (m²)": "_LSFS",
            "DSFS (m²)": "_DSFS",
            "SSFS (m²)": "_SSFS",
            "PAFS (N·m)": "_PAFS",
            "RAFS (N·m)": "_RAFS",
            "YAFS (°)": "_YAFS",
            "PSFS (°/s)": "_PSFS",
            "RSFS (°/s)": "_RSFS",
            "YSFS (°/s)": "_YSFS",
            "CLAL0HS": "_CLAL0HS",
            "SHS (m²)": "_SHS",
            "CLAHS": "_CLAHS",
            "CD0HS": "_CD0HS",
            "ALPHA0HS (°)": "_ALPHA0HS",
            "KLAMHS": "_KLAMHS",
            "CLAL0VS": "_CLAL0VS",
            "SVS (m²)": "_SVS",
            "CLAVS": "_CLAVS",
            "CD0VS": "_CD0VS",
            "ALPHA0VS (°)": "_ALPHA0VS",
            "CKLG": "_CKLG"
        }
    
        # Read the CSV file
        file_path = app_data['file_path_name']
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            
            for row in reader:
                if len(row) == 2:
                    label, value = row[0], row[1]
    
                    # Map the label to the correct tag
                    tag = label_to_tag.get(label)
                    if tag and dpg.does_item_exist(tag):  # Ensure tag exists in UI
                        # Convert value to the appropriate type if needed
                        if value.replace('.', '', 1).isdigit():
                            value = float(value) if '.' in value else int(value)
                        dpg.set_value(tag, value)
                        print(f"Set {tag} ({label}) to {value}")
                    else:
                        print(f"Warning: Label {label} does not have a corresponding tag or the tag does not exist.")

        
        
        


    
