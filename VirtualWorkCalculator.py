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

#I wrote this function that directly gives the displacement for when people want it
def displacement(forces, dummy_forces, areas, lengths):
  """
  (list, list, list, list) -> num
  Given a list of corresponding forces, dummy forces, areas, and lengths, calculates the displacement of the middle joint.
  """
  count = 0
  for i in range(len(forces)):
    count += forces[i] / areas[i] / 200000 * lengths[i] * dummy_forces[i]
  return count

def dummy_forces(joints_number, deg1, deg2, orientation = "top"):
  """
  (num, num, num, string) -> list
  Given a truss, finds the dummy forces for the method of virtual work.
  """
  ten = []
  com = []
  if orientation == "top":
    a = 1
    b = -1
  else:
    a = -1
    b = 1
  theta1 = radians(deg1)
  theta2 = radians(deg2)
  if joints_number % 2 == 0:
    n = joints_number / 2 - 1
    ran = (joints_number + 1) // 4
    error = 1
  else:
    n = (joints_number - 3) / 2
    ran = (joints_number + 1) // 4
    error = joints_number % 4 - 1
  rxn = 1 / 2
  f1 = rxn / sin(theta1)
  if b == 1:
    ten.append(f1)
  else:
    com.append(f1)
  f2 = rxn / sin(theta1) * cos(theta1)
  if a == 1:
    ten.append(f2)
  else:
    com.append(f2)
  f3 = f1 * sin(theta1) / sin(theta2)
  if a == 1:
    ten.append(f3)
  else:
    com.append(f3)
  f4 = f1 * cos(theta1) + f3 * cos(theta2)
  if b == 1:
    ten.append(f4)
  else:
    com.append(f4)
  for i in range(ran-1):
    f1 = f3 * sin(theta2) / sin(theta1)
    if b == 1:
      ten.append(f1)
    else:
      com.append(f1)
    f2 = f2 + f3 * cos(theta2) + f1 * cos(theta1)
    if a == 1:
      ten.append(f2)
    else:
      com.append(f2)
    f3 = f1 * sin(theta1) / sin(theta2)
    if a == 1:
      ten.append(f3)
    else:
      com.append(f3)
    f4 = f4 + f1 * cos(theta1) + f3 * cos(theta2)
    if b == 1:
      ten.append(f4)
    else:
      com.append(f4)
  if joints_number % 2 == 0:
    com.pop()
    ten.pop()
    if a == 1:
      ten.append(1)
    else:
      com.append(1)
  else:
    if error == 2:
      com.pop()
      ten.pop()
  return [com, ten]
