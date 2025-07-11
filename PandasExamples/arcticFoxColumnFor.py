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
with open('C:/Users/littl/Code/GitHub/ArcticFoxExamples/PandasExamples/.af/analyzedvariables/columnfor.analyzedvariables.json', 'r') as _af_dataSave:
    _af_existingData = json.load(_af_dataSave)
    _af_existingData = dictToDefaultdict(_af_existingData)
    for key in _af_existingData:
        _af_arcticFoxDataDictionary[key] = _af_existingData[key]

def variables(values):
    return [value for value in values if not value.startswith('__') and value != 'af']

def analyzeVariables(variables):
    for (variableName, variableValue) in variables:

        _af_arcticFoxDataDictionary[r'PandasExamples_ColumnFor.py']['variables'][variableName]['type'] = 'None'
        variableType = str(type(variableValue))
        if variableType.startswith("<class '") and variableType.endswith("'>"):
            variableType = variableType.replace("<class '", "")
            variableType = variableType.replace("'>", "")
        _af_arcticFoxDataDictionary[r'PandasExamples_ColumnFor.py']['variables'][variableName]['type'] = variableType
        
        import pandas as pd
        import json
        from pandas.api.types import is_datetime64_any_dtype as is_datetime
        
        if isinstance(variableValue, pd.DataFrame):
        
            dataColumns = []
            for column in variableValue.columns:
                try:
                    if variableValue[column].dtype == 'object':
                        variableValue[column] = str(pd.to_datetime(variableValue[column]))
                except Exception as e:
                    pass
        
            for index, dataType in enumerate(variableValue.dtypes):
                columnTypeForEnum = 0
                if 'int' in str(dataType):
                    columnTypeForEnum = 1
                elif 'float' in str(dataType):
                    columnTypeForEnum = 2
                elif 'bool' in str(dataType):
                    columnTypeForEnum = 3
                elif 'date' in str(dataType):
                    columnTypeForEnum = 6
                elif 'timedelta' in str(dataType):
                    columnTypeForEnum = 0
                elif 'category' in str(dataType):
                    columnTypeForEnum = 4
        
                dataColumns.append({
                    'Name': variableValue.columns[index],
                    'ColumnType': columnTypeForEnum #,
                    #'Categories': None
                })
        
            _af_arcticFoxDataDictionary[r'PandasExamples_ColumnFor.py']['variables'][variableName]['columns'] = dataColumns
        
        

    saveAnalyzedVariables()
    print("Arctic Fox finished analyzing variables")

def saveAnalyzedVariables():
    with open('C:/Users/littl/Code/GitHub/ArcticFoxExamples/PandasExamples/.af/analyzedvariables/columnfor.analyzedvariables.json', 'w') as _af_dataSave:
        _af_dataSave.write(json.dumps(_af_arcticFoxDataDictionary, indent=4))
