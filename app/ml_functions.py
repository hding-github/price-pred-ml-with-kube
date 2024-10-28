import json
import pandas as pd
import pickle

def load_model(file_name):
    # load
    tModel = pickle.load(open(file_name, "rb"))
    return tModel

strPath = "./results/"
strFile = "xgboost_optimal.pickle"
model_xgboost = load_model(strPath+strFile)

strFile = "randomforest_optimal.pickle"
model_randomforest = load_model(strPath+strFile)

def is_number(strValue):
    try:
        float(strValue)
        return True
    except ValueError:
        return False

def str_2_pd(strD):
    strIncorrectFormat = "Incorrect data format."
    try:
        tD = json.loads(strD)
    except ValueError as e:
        return [strIncorrectFormat, None]
    
    Str_Template = '{"CRIM": [0.09178], "ZN": [0.0], "INDUS": [4.05], "CHAS": [0.0], "NOX": [0.51], "RM": [6.416], "AGE": [84.1], "DIS": [2.6463], "RAD": [5.0], "TAX": [296.0], "PTRATIO": [16.6], "B": [395.5], "LSTAT": [9.04]}'
    tD_Template = json.loads(Str_Template)

    if len(tD) != len(tD_Template):
        return [strIncorrectFormat, None]

    for tName in tD:
        if tName not in tD_Template:
            return [strIncorrectFormat, None]
        if isinstance(tD[tName], list) == False:
            return [strIncorrectFormat, None]
        if len(tD[tName]) != 1:
            return [strIncorrectFormat, None]
        tStr = str(tD[tName][0])
        if is_number(tStr) == False:
            return [strIncorrectFormat, None]
    tDF = pd.DataFrame(tD)
    return ["ok", tDF]

def prediction(strD, strModel):
    [strMSG, tDF] = str_2_pd(strD)
    tValue = 0
    tPred = None
    if strMSG == "ok":
        if strModel == "xgboost":
            tPred = model_xgboost.predict(tDF)
            tValue =tPred.item()  
        if strModel == "randomforest":
            tPred = model_randomforest.predict(tDF)
            tValue =tPred.item() 
        strMSG = "Please input model: xgboost or randomforest"
    strResults = json.dumps({"msg": strMSG, "pred": tValue})
    return strResults

def test():
    strD = '{"CRIM": [0.09178], "ZN": [0.0], "INDUS": [4.05], "CHAS": [0.0], "NOX": [0.51], "RM": [6.416], "AGE": [84.1], "DIS": [2.6463], "RAD": [5.0], "TAX": [296.0], "PTRATIO": [16.6], "B": [395.5], "LSTAT": [9.04]}'
    strResults = prediction(strD, "xgboost")
    strResults = prediction(strD, "randomforest")