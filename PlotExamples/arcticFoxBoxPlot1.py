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
with open('X:/Code/GitHub/ArcticFoxExamples/PlotExamples/.af/analyzedvariables/boxplot1.analyzedvariables.json', 'r') as _af_dataSave:
    _af_existingData = json.load(_af_dataSave)
    _af_existingData = dictToDefaultdict(_af_existingData)
    for key in _af_existingData:
        _af_arcticFoxDataDictionary[key] = _af_existingData[key]

def variables(values):
    return [value for value in values if not value.startswith('__') and value != 'af']

def analyzeVariables(variables):
    for (variableName, variableValue) in variables:

        _af_arcticFoxDataDictionary[r'PlotExamples_BoxPlot1.py']['variables'][variableName]['type'] = 'None'
        variableType = str(type(variableValue))
        if variableType.startswith("<class '") and variableType.endswith("'>"):
            variableType = variableType.replace("<class '", "")
            variableType = variableType.replace("'>", "")
        _af_arcticFoxDataDictionary[r'PlotExamples_BoxPlot1.py']['variables'][variableName]['type'] = variableType
        
        import pandas as pd
        import json
        from pandas.api.types import is_datetime64_any_dtype as is_datetime
        
        if isinstance(variableValue, pd.DataFrame):
        
            dataColumns = []
            for column in variableValue.columns:
                try:
                    if variableValue[column].dtype == 'object':
                        variableValue[column] = pd.to_datetime(variableValue[column])
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
                elif 'str' in str(dataType): #TODO
                    columnTypeForEnum = 4 #TODO
        
                dataColumns.append({
                    'Name': variableValue.columns[index],
                    'ColumnType': columnTypeForEnum,
                    'Categories': None
                })
        
            _af_arcticFoxDataDictionary[r'PlotExamples_BoxPlot1.py']['variables'][variableName]['columns'] = dataColumns
        
        elif isinstance(variableValue, pd.Series):
            dataColumns = []
        
            columnTypeForEnum = 0
            if 'int' in str(variableValue.dtype):
                columnTypeForEnum = 1
            elif 'float' in str(variableValue.dtype):
                columnTypeForEnum = 2
            elif 'bool' in str(variableValue.dtype):
                columnTypeForEnum = 3
            elif 'date' in str(variableValue.dtype):
                columnTypeForEnum = 6
            elif 'timedelta' in str(variableValue.dtype):
                columnTypeForEnum = 0
            elif 'category' in str(variableValue.dtype):
                columnTypeForEnum = 4
            elif 'str' in str(variableValue.dtype): #TODO
                columnTypeForEnum = 4 #TODO
        
            dataColumns.append({
                'Name': variableValue.name,
                'ColumnType': columnTypeForEnum,
                'Categories': None
            })
        
            _af_arcticFoxDataDictionary[r'PlotExamples_BoxPlot1.py']['variables'][variableName]['columns'] = dataColumns
        
        
        
        import pandas as pd
        import json
        from pandas.api.types import is_datetime64_any_dtype as is_datetime
        
        if isinstance(variableValue, pd.DataFrame):
        
            dataColumns = []
            for column in variableValue.columns:
                try:
                    if variableValue[column].dtype == 'object':
                        variableValue[column] = pd.to_datetime(variableValue[column])
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
                elif 'str' in str(dataType): #TODO
                    columnTypeForEnum = 4 #TODO
        
                dataColumns.append({
                    'Name': variableValue.columns[index],
                    'ColumnType': columnTypeForEnum,
                    'Categories': None
                })
        
            _af_arcticFoxDataDictionary[r'PlotExamples_BoxPlot1.py']['variables'][variableName]['columns'] = dataColumns
        
        elif isinstance(variableValue, pd.Series):
            dataColumns = []
        
            columnTypeForEnum = 0
            if 'int' in str(variableValue.dtype):
                columnTypeForEnum = 1
            elif 'float' in str(variableValue.dtype):
                columnTypeForEnum = 2
            elif 'bool' in str(variableValue.dtype):
                columnTypeForEnum = 3
            elif 'date' in str(variableValue.dtype):
                columnTypeForEnum = 6
            elif 'timedelta' in str(variableValue.dtype):
                columnTypeForEnum = 0
            elif 'category' in str(variableValue.dtype):
                columnTypeForEnum = 4
            elif 'str' in str(variableValue.dtype): #TODO
                columnTypeForEnum = 4 #TODO
        
            dataColumns.append({
                'Name': variableValue.name,
                'ColumnType': columnTypeForEnum,
                'Categories': None
            })
        
            _af_arcticFoxDataDictionary[r'PlotExamples_BoxPlot1.py']['variables'][variableName]['columns'] = dataColumns
        
        

    saveAnalyzedVariables()
    print("Arctic Fox finished analyzing variables")

def saveAnalyzedVariables():
    with open('X:/Code/GitHub/ArcticFoxExamples/PlotExamples/.af/analyzedvariables/boxplot1.analyzedvariables.json', 'w') as _af_dataSave:
        _af_dataSave.write(json.dumps(_af_arcticFoxDataDictionary, indent=4))
