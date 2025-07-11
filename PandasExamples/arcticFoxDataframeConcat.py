import json
from collections import defaultdict
import os
import warnings
warnings.simplefilter("ignore")

def _af_recursive_defaultdict():
    return defaultdict(_af_recursive_defaultdict)

def dictToDefaultdict(dictionary):
    if not isinstance(dictionary, dict):
        return dictionary
    return defaultdict(lambda: defaultdict(dict), {
        k: dictToDefaultdict(v)
        for k, v in dictionary.items()
    })

_af_arcticFoxDataDictionary = defaultdict(_af_recursive_defaultdict)
with open('C:/Users/littl/Code/GitHub/ArcticFoxExamples/PandasExamples/.af/analyzedvariables/dataframeconcat.analyzedvariables.json', 'r') as _af_dataSave:
    _af_existingData = json.load(_af_dataSave)
    _af_existingData = dictToDefaultdict(_af_existingData)
    for key in _af_existingData:
        _af_arcticFoxDataDictionary[key] = _af_existingData[key]

def variables(values):
    return [value for value in values if not value.startswith('__') and value != 'af']

def analyzeVariables(variables):
    for (variableName, variableValue) in variables:

        _af_arcticFoxDataDictionary[r'PandasExamples_DataframeConcat.py']['variables'][variableName]['type'] = 'None'
        variableType = str(type(variableValue))
        if variableType.startswith("<class '") and variableType.endswith("'>"):
            variableType = variableType.replace("<class '", "")
            variableType = variableType.replace("'>", "")
        _af_arcticFoxDataDictionary[r'PandasExamples_DataframeConcat.py']['variables'][variableName]['type'] = variableType
        

    saveAnalyzedVariables()
    print("Arctic Fox finished analyzing variables")

def saveAnalyzedVariables():
    with open('C:/Users/littl/Code/GitHub/ArcticFoxExamples/PandasExamples/.af/analyzedvariables/dataframeconcat.analyzedvariables.json', 'w') as _af_dataSave:
        _af_dataSave.write(json.dumps(_af_arcticFoxDataDictionary, indent=4))
