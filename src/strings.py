
'''
All various strings used throughout the whole add-on
'''
strings = {
    "ExportButton_text" : "Export selected muscle(s)",
    "ExportButton_bl_idname" : "object.export_coords",
    "ExportButton_bl_label" : "id_export_button",
    "ExportButton_bl_description" : "Export selected muscle parts (volume, origin, insertion)",

    "DecomposeButton_bl_idname" : "object.decompose",
    "DecomposeButton_bl_description" : "Decompose specified/all muscle(s) in the selected directory",
    "DecomposeButton_type_specified_text" : "Decompose specified muscle",
    "DecomposeButton_type_all_text" : "Decompose all muscles",
    "DecomposeButton_type_specified" : "specified",
    "DecomposeButton_type_all" : "all",

    "Label_output_path_text" : "Output directory",
    "Label_output_filename_text" : "Muscle name (decomposition)",
    "Label_parameters_text" : "Muscle decomposition parameters",

    # Popup messages
    "Message_nothing_selected" : "No object(s) selected!",
    "Message_exporting_finished" : "Exporting finished!",
    "Message_wrong_name_format" : "Wrong muscle name format! Model should be named using following pattern: <muscle_name><space><origin|volume|insertion><space><boundary>!",
    "Message_decomposing_done" : "Decomposing done!",
    "Message_muscle_not_found" :"Corresponding muscle not found. Please, adjust the model manually",
    "Message_file_not_found" : "File was not found! Please, check the filename and directory.",
    "Message_nothing_to_export" : "No muscles to export found in the specified directory.",
    "Message_mdt_not_found" : "MuscleDecomposition executable has not been found in the add-on folder! Please, proceed to user manual for further information.",
    "Message_decomposition_unsuccessful" : "Decomposition has been aborted due to the following reason: ",
    "Message_decomposition_done" : "MuscleDecompositionTest output: ",
}