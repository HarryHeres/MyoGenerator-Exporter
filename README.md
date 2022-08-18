# Introduction
A Blender add-on for use in combination with the [MyoGenerator](https://github.com/evaherbst/MyoGenerator) add-on developed by *Eva C. Herbst*.
It's purpose is to be able to easily export **models of muscles** with their *origin* and *insertion* areas out of Blender and decompose them into **a set of muscle fibres** - a more realistic representation.

It is supported by the Myogenerator add-on version **1.0.0** and Blender versions **2.8X.X - 2.9X.X**

# Installation
To install this add-on, download the intended released version and proceed as follows: [How to install](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html).
After a successfull installation, the add-on should be present on the right vertical add-on toolbar (showed by pressing the **N** key).

# Model hierarchy
For the add-on to successfully decompose a muscle, the user has to create **3** separate models:
- Model of the muscle volume
- Model of the origin area
- Model of the insertion area

The name of the models in the scene **MUST** follow a naming convention: 
- For the volume model:`<muscle_name><space>volume`
- For the insertion area: `<muscle_name><space>insertion<space>boundary`
- For the origin area: `<muscle_name><space>origin<space>boundary`

A proper muscle model could have following hierarchy (in the scene):

![](src/docs/GitHub/Blender-muscle-naming.png)

*The name of the muscle model in this case is mAMEM_new*

# Add-on GUI description
The add-on's GUI is fairly simple:

![](./src/docs/GitHub/Blender-addon-gui-final.png) 

## Output directory
This parameter is used for selecting a work folder. 
Export and decomposition functionallities are working with **this** directory.

## Muscle name (decomposition)
This parameter serves **only** for the singular decomposition process (Decompose specified muscle(s)).
After pressing this button, the add-on searches for the [essential]() files in the current working directory (specified by [Output directory](#output-directory))

# Exporting a model
The [3 separate models](#model-hierarchy) can be exported out of Blender.
To export them, user has to select which of the model should be exported. (*in the object hierarchy in the upper right corner; use CTRL + mouse click to select multiple parts*)
After that, click on the **Export selected muscle(s)** to export all the selected models (and their parts).
The number of models/parts to export is **not** limited.

If the export was successfull, the following pop-up should appear:

![](src/docs/GitHub/Blender-muscle-export-1.png)

*If a dialog with different a message appears, please proceed to the [Troubleshooting](#troubleshooting) section*

and a new file, in the [working directory](#output-directory), should appear (with the same name).

![](src/docs/GitHub/Blender-muscle-export-2.png)

The export format for the insertion/origin areas is **VTK**, for the volume **OBJ**. 

# Decomposing a model


# Troubleshooting