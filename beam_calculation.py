def centroidal_and_2nd_moment(beam_type, l1, l2, l3=0 , l4=0, l5=0, l6=0) :
    '''
    input: 'w','t','i'
    |--------[L1]--------|
    ======================
    |                    |  [L2]
    ======================
        |    |   |      
        |    |   |
       [L3]  |   |
        |    |   |
        |  ->|   |<- [L4]
    ======================
    |                    | [L5]
    ======================
    |--------[L6]--------|
    
    for rectangular beam: only L1 and L2
    for T-beam, only L1,L2,L3 or L3,L4,L5
    for I-beam, all L are used
    
    All units are in mm
    '''
    if beam_type=='w':
        y_bar=l2/2
        I=l1*(l2**3)/12
    if beam_type=='t':
        y2= l3/2
        y1=l3+l2/2
        a1=l1*l2
        a2= l4*l3        
        y_bar=(a1*y1+a2*y2)/(a1+a2)
        I=l4*(l3**3)/12+a2*(y_bar-y2)**2+l1*(l2**3)/12+a1*(y1-y_bar)**2
    if beam_type=='i':
        y3= l5/2
        y2= l5+l3/2
        y1= l5+l3+l2/2
        a1= l1*l2
        a2= l3*l4
        a3= l5*l6
        y_bar=(a1*y1+a2*y2+a3*y3)/(a1+a2+a3)
        I=l6*(l5**3)/12+a3*(y_bar-y3)**2+l4*(l3**3)/12+a2*(y_bar-y2)**2+l1*(l2**3)/12+a1*(y1-y_bar)**2
    return round(y_bar,2),round(I,3)
    