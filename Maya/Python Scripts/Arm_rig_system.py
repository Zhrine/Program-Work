'''
import new_arm_rig
reload(new_arm_rig)
new_arm_rig.gui()
'''

import pymel.core as pm
sriptName = __name__
newWindow ='Auto_armRig_Maker'

def gui():
    #checks if window exists then deletes the ui
    if(pm.window(newWindow, q=True, exists=True)):
        pm.deleteUI(newWindow)
    #Creates if preferences exists then deletes the preferences
    if(pm.windowPref(newWindow, q=True, exists=True)):
        pm.windowPref(newWindow, remove=True)

    myWindow = pm.window(newWindow, t='Auto Arm Rig', w=150, h=325)
    main_layout = pm.columnLayout('Main Header')

    # naming options (option menu)
    pm.text('naming_Text', l='Step 1: Set name options')
    pm.rowColumnLayout(nc=4,cw=[(1, 20), (2, 40), (3, 40), (4, 50)])
    pm.text('ori_Txt', label='Ori:')
    pm.optionMenu('ori_Menu')
    pm.menuItem(label='lf_')
    pm.menuItem(label='rt_')
    pm.menuItem(label='ct_')
    pm.text('label_Txt', label='Label:')
    pm.optionMenu('label_Menu')
    pm.menuItem(label='arm')
    pm.menuItem(label='leg')
    pm.setparent(main_layout)
    pm.separator('name_Sep', w=150, h=5)

    # set the rig type (radio button)
    pm.text('rigType_Text', l='Step 2: Set rig type')
    pm.radioButtonGrp('armType_Btn', labelArray3=['IK', 'FK', 'IK/FK'], numberOfRadioButtons=3, columnWidth4=[50, 50, 50,], select=3)
    pm.separator('type_Sep', w=150, h=5)

    # set icon options (option menu)
    pm.text('conset_Text', l='Step 3: Set icon options')
    pm.rowColumnLayout(nc=2, cw=[(1, 660), (2, 60)])
    pm.text('ikStyle_Text',label='Ik Icon Style:')
    pm.optionMenu('ikIcon_Menu')
    pm.menuItem(label="Box")
    pm.menuItem(label="4 Arrows")
    pm.menuItem(label="4 Pin")
    pm.text('fkStyle_Text',label='Fk Icon Style:')
    pm.optionMenu('fkIcon_Menu')
    pm.menuItem(label="Circle")
    pm.menuItem(label="Turn Arrows")
    pm.text('handStyle_Text',label='Hand Icon Style:')
    pm.optionMenu('handIcon_Menu')
    pm.menuItem(label="Cirlce")
    pm.menuItem(label="COG")
    pm.text('pvStyle_Text',label='PV Icon Style:')
    pm.optionMenu('pvIcon_Menu')
    pm.menuItem(label="Dmnd")
    pm.menuItem(label="Arrow")
    pm.setparent(main_layout)
    pm.button('testIcon_Btn', label='Make test icons set to scale', w=150)
    pm.separator('style_Sep', w=150, h=5)

    # pick the color (iconTextButton and colorSlider)
    pm.text('armcolor_Text', l='Step 4: Pick icon color')
    pm.gridLayout(nr=1,nc=5, cellWidthHeight=(30,20))
    pm.icontextButton('darkBlue_Btn',bgc=[.000,.016,.373])
    pm.icontextButton('lightBlue_Btn',bgc=[0,0,1])
    pm.icontextButton('brown_Btn',bgc=[.537,.278,.2])
    pm.icontextButton('Red_Btn',bgc=[.1,0,0])
    pm.icontextButton('yellow_Btn',bgc=[1,1,0])
    pm.setparent(main_layout)
    pm.colorIndexSliderGrp('armColor',w=150, h=20, cw2=(150,0) min=0, max=31, value=7)
    pm.separator('color_Sep', w=150, h=5)

    # pole vector options (radio button)
    pm.text('pv_Text', label='Step 5: Set IK elbow options')
    pm.radioButtonGrp('AddPVElbow_Btn', labelArray2=['twist', 'Pole Vector'], numberOfRadioButtons=2, columnWidth4=[65,85], select=2,)
    pm.separator('pv_Sep', w=150, h=5)
    pm.button('final_Btn', label='Finalize the arm', w=150)

    pm.showWindow()