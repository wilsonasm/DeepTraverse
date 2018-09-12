# andy cohen -- sample code fragment for ece203 
# May 2018
# recursive dfs tree travsersal

# dfsTraverse is the recursive function 
def dfsTraverse(path,tree,root):
    if root in tree:
        node=tree[root]
        path=dfsTraverse(path,tree,node[0])
        path=dfsTraverse(path,tree,node[1])
        
    path.append(root)
    return path

# add a single node to node list. used to check for roots
# note -- uses global nodes variables. 
# left this here for "teachable moment". 
# -- Is this a good use of global variables?
# -- how could we get rid of the global?
def addNode(nodeID):
    if nodeID in nodes:
        return
    nodes.append(nodeID) # modifies global nodes in function. unnecessary danger...

# global scope variables
tree=dict() # the binary tree, from the file
parent=dict() # parent node lookup
nodes=[] # list of all nodes

# execution starts here
# read in tree and populate structs
with open('treefile.txt', 'r') as f:
    for line in f:
        line=line.strip()
        line=line.split(',')
        if 3!=len(line):
            # ACK -- need better error handler...
            print("error bad line read: "+str(line))
            continue
        # this is the dfs struct
        tree[line[0]]=line[1:3]
        # set up list and dictionary for finding root nodes
        # note - don't need two structures for this, but 
        # it is handy to keep around the extra info for possible future 
        # questions...
        parent[line[1]]=line[0]
        parent[line[2]]=line[0]
        for id in line:
            addNode(id)
# traverse all nodes
for id in nodes:
    # if node doesn't have a parent
    if id not in parent:
        # then it's a root -- traverse its tree
        path=dfsTraverse([],tree,id)
        print path