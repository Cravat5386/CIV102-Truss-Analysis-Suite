def is_valid(member,force):
    '''
    while len(member)!=len(force):
        (member,force)=float(input("Invalid! Please re-enter length of member and force acting:"))
        is_valid(member,force)
    '''
    '''
    check if input is valid
    (list,list)->boolean
    is_valid([1,2,3,4],[5,6,6])
    >>>0
    '''
    if len(member)!=len(force):
        return 0
    return 1

def virtual_work(member,force,area,modulus,dummy_forces):
    work=[0 for i in range(len(member))]
    for i in range(member):
        deform[i]=(force[i]*member[i])/(modulus*area[i])
         #if we could change kevin's program and make them return values this part would be easy to apply truss analysis
        work[i]=dummy_forces[i]*deform[i]
    for j in range(work):
        total+=work[i]
    ver_deform=total
    return ver_deform
        
    