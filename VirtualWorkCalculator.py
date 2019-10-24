def is_valid(member,force):
    '''
    while len(member)!=len(force):
        (member,force)=float(input("Invalid! Please re-enter length of member and force acting:"))
        is_valid(member,force)
    '''
    if len(member)!=len(force):
        return 0
    return 1
def virtual_work(member,force,area,modulus):
    for i in range(member):
        deform[i]=(force[i]*member[i])/(modulus*area[i])
    #if we could change kevin's program and make them return values this part would be easy to apply truss analysis
    