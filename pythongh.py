import ghpythonlib.treehelpers as th
import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

# definitions
def vec2pt(vec1,vec2):
    '''
    Calculates the vector between point 1 and point 2
    '''
    newVec=[vec2[0]-vec1[0],vec2[1]-vec1[1],vec2[2]-vec1[2]]
    return newVec

def vecMidpt(vec1,vec2):
    '''
    Computes the midpoint between two vectors
    '''
    newVec=[(vec1[0]+vec2[0])/2,(vec1[1]+vec2[1])/2,(vec1[2]+vec2[2])/2]
    return newVec

def vecAdd(vec1,vec2):
    newVec=[vec1[0]+vec2[0],vec1[1]+vec2[1],vec1[2]+vec2[2]]
    return newVec

def tree2list(tree):
    '''
    Creates a list based on a tree and a list of lists based on indices.
    Tested with {x;x} input type
    '''
    branches=0; newList=[]
    
    for i in range(0,tree.BranchCount):
        
        # look for the first item in a tree branch
        if ";0}" in str(tree.Path(i)):
            #skip appending in first instance of {x;0}
            if i>0:
                newList.append(tempList)
            tempList=[]
        #append to temp list
        tempList.append(tree.Branch(i))
        
        #finish of the list when getting to last item
        if i==tree.BranchCount-1:
            newList.append(tempList)
    
    return newList
    print("Created a new list with "+str(len(newList))+" branches")
