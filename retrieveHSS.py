import pandas as pd

def retrieveHSS(requiredA, requiredI, requiredR, path = "HSSProperties.csv"):
    df = pd.read_csv(path)
    areaCol = df.loc[:, 'Area']
    ICol = df.loc[:, 'I']
    rCol = df.loc[:, 'r']
    leastMass = 1000
    idealHSS = 0
    print(df)
    for i, (a, inert, r) in enumerate(zip(areaCol, ICol, rCol)):
        print("{}, {}, {}".format(a, inert, r))
        if a > requiredA and inert > requiredI and r > requiredR:
            if df.loc[i, 'Mass'] < leastMass:
                idealHSS = i
         
    print("Ideal HSS Designation is: {}".format(str(df.loc[idealHSS, 'Designation'])+' '+str(df.loc[idealHSS, 'Size'])))
    
    return str(df.loc[idealHSS, 'Designation'])+' '+str(df.loc[idealHSS, 'Size'])
