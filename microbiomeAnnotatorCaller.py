#Annotator caller
import PySimpleGUI as sg
from microbeAnnotator_condensed import Annotator as ann
from phylotree_maker import TreeMaker as TM
'''
jsondic = sg.popup_get_file("Location of NCBI_Tax_dictionary.json:")
sg.popup('You entered', jsondic)
inputfiles = sg.popup_get_folder("Folder of input bioc files:")
sg.popup("You entered", inputfiles)
outputfiles = sg.popup_get_folder("Directory to contain output json files:")
sg.popup("You entered", outputfiles)
layout = [[sg.Text('Please enter the section title being searched for. Type ALL for all section titles')],
[sg.Text('Section Title', size = (15,1)), sg.InputText()], [sg.Submit(), sg.Cancel()]]
window = sg.Window('Data Entry', layout)
event, values = window.read()
window.close()
result = ann(jsondic, inputfiles, outputfiles, 0, values)
result.initialsteps()
'''

result = ann('NCBI_tax_dictionary8.json', 'Testset', 'results', 0, 'ALL')
result.initialsteps()
'''

object = TM('ALLAnnotated_output_2023-08-12_15-04-07', 'NCBI_tax_dictionary8.json')
object.dictionary_to_lineage()
'''