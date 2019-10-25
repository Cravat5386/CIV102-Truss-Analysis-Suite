from math import *
"""
Functions list:
truss_analysis
virtual_work (in progress)
force_and_length
displacement
max_force
lengths
hss_constraints
is_valid
dummy_forces
"""
#_______________________________________________________________________________________________________________________________________________#

def truss_analysis(joints_number, joint_load, deg1, deg2, orientation = "top"):
  """
  (number, number, number, number, string) -> list
  Takes the number of joints, the joint load, the two bottom angles of the truss, and whether the truss is above or below the deck of the bridge. Prints forces in the members in the order below.
      ________________
     /\  4   /\  8 
    /  \    /  \     ...
  1/   3\ 5/   7\
  /______\/______\____
     2       6
  Returns the list [list of compression forces, list of tension forces]
  Ex. (CIV102 Problem Set 5 questions 2 and 3)
  >>>truss_analysis(13, 10, 60, 60)
  -28.86751345948129
  14.433756729740649
  28.86751345948129
  -28.86751345948129
  -17.320508075688775
  37.527767497325684
  17.320508075688775
  -46.18802153517007
  -5.773502691896258
  49.0747728811182
  5.773502691896258
  -51.96152422706633
  Ignore last 0 value(s).
  Remember slide rule precision!
  [[28.86751345948129, 28.86751345948129, 17.320508075688775, 46.18802153517007, 5.773502691896258, 51.96152422706633], [14.433756729740649, 28.86751345948129, 37.527767497325684, 17.320508075688775, 49.0747728811182, 5.773502691896258]]
  >>>truss_analysis(12, 10, 45, 90, "bottom")
  35.35533905932738
  -25.000000000000004
  -25.0
  25.000000000000004
  21.213203435596427
  -40.00000000000001
  -15.0
  40.00000000000001
  7.0710678118654755
  -45.00000000000001
  -5.0
  45.00000000000001
  Ignore last 1 value(s).
  Multiply second last value by 2.
  Remember slide rule precision!
  [[25.000000000000004, 25.0, 40.00000000000001, 15.0, 45.00000000000001, 10], [35.35533905932738, 25.000000000000004, 21.213203435596427, 40.00000000000001, 7.0710678118654755]]
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
  rxn = joint_load * n / 2
  f1 = rxn / sin(theta1)
  print(b*f1)
  if b == 1:
    ten.append(f1)
  else:
    com.append(f1)
  f2 = rxn / sin(theta1) * cos(theta1)
  if a == 1:
    ten.append(f2)
  else:
    com.append(f2)
  print(a*f2)
  f3 = f1 * sin(theta1) / sin(theta2)
  if a == 1:
    ten.append(f3)
  else:
    com.append(f3)
  print(a*f3)
  f4 = f1 * cos(theta1) + f3 * cos(theta2)
  if b == 1:
    ten.append(f4)
  else:
    com.append(f4)
  print(b*f4)
  for i in range(ran-1):
    f1 = (f3 * sin(theta2) - joint_load) / sin(theta1)
    if b == 1:
      ten.append(f1)
    else:
      com.append(f1)
    print(b*f1)
    f2 = f2 + f3 * cos(theta2) + f1 * cos(theta1)
    if a == 1:
      ten.append(f2)
    else:
      com.append(f2)
    print(a*f2)
    f3 = f1 * sin(theta1) / sin(theta2)
    if a == 1:
      ten.append(f3)
    else:
      com.append(f3)
    print(a*f3)
    f4 = f4 + f1 * cos(theta1) + f3 * cos(theta2)
    if b == 1:
      ten.append(f4)
    else:
      com.append(f4)
    print(b*f4)
  print("Ignore last", error, "value(s).")
  if joints_number % 2 == 0:
    com.pop()
    ten.pop()
    if a == 1:
      ten.append(joint_load)
    else:
      com.append(joint_load)
    print("Multiply second last value by 2.")
  else:
    if error == 2:
      com.pop()
      ten.pop()
  print("Remember slide rule precision!")
  return [com, ten]

def virtual_work(joints_number, joint_load, deg1, deg2, length, orientation = "top", modulus = 200000):

def force_and_length(joints_number, joint_load, deg1, deg2, length, orientation = "top"):
  """
  (num, num, num, num, num, string) -> (list, list)
  Does a truss_analysis, and returns both a list of forces and the lengths of the members that are subjected by them.
  """
  ls = truss_analysis(joints_number, joint_load, deg1, deg2, orientation)
  cplace = []
  tplace = []
  lengths = lengths(joints_number, length, deg1, deg2)
  if joints_number % 2 == 0:
    n = joints_number / 2 - 1
    ran = (joints_number + 1) // 4
    error = 1
  else:
    n = (joints_number - 3) / 2
    ran = (joints_number + 1) // 4
    error = joints_number % 4 - 1
  if orientation == "top":
    for i in range(ran-1):
      cplace.append(lengths[1])
      tplace.append(lengths[0])
      tplace.append(lengths[2])
      cplace.append(lengths[0])
    if joints_number % 2 == 0:
      cplace.pop()
    else:
      if error == 1:
        cplace.pop()
      else:
        cplace.pop()
        tplace.pop()
        tplace.pop()
      cnew = cplace.pop()
      cplace.append(cnew/2)
  else:
    for i in range(ran-1):
      tplace.append(lengths[1])
      cplace.append(lengths[0])
      cplace.append(lengths[2])
      tplace.append(lengths[0])
    if joints_number % 2 == 0:
      tplace.pop()
    else:
      if error == 1:
        tplace.pop()
      else:
        tplace.pop()
        cplace.pop()
        cplace.pop()
      tnew = tplace.pop()
      tplace.append(tnew)
  return ls, [cplace, tplace]

def displacement(member, force, area, dummy_forces, modulus = 200000):

    '''
    Uses the length of the member (member), the force acting on it (force),
    the member's Young's modulus, and the dummy forces on each member to
    Calculate the vertical deformation of the bridge (total)
    '''
    total = 0
    for i in range(len(member)):
        total += dummy_forces[i]*(force[i]*member[i])/(modulus*area[i])
    return total

def max_force(ls, orientation = "top"):
  """
  (list, string) -> list
  Given a list of the compression and tension values, and whether the truss is above or below the deck, returns a list of the maximum tension and compression forces, as well as the members they act upon as per the ascii drawing in truss_analysis() in the format [highest compression force, member that the compression acts on, highest tension force, member that the tension acts on].
  Ex. (CIV102 Problem Set 5 questions 2 and 3)
  >>>max_force([[28.86751345948129, 28.86751345948129, 17.320508075688775, 46.18802153517007, 5.773502691896258, 51.96152422706633], [14.433756729740649, 28.86751345948129, 37.527767497325684, 17.320508075688775, 49.0747728811182, 5.773502691896258]])
  [51.96152422706633, 12], [49.0747728811182, 10]
  >>>max_force([[25.000000000000004, 25.0, 40.00000000000001, 15.0, 45.00000000000001, 10], [35.35533905932738, 25.000000000000004, 21.213203435596427, 40.00000000000001, 7.0710678118654755]], "bottom")
  [45.00000000000001, 10, 40.00000000000001, 8]
  """
  c = ls[0]
  t = ls[1]
  com = 0
  ten = 0
  cplace = 0
  tplace = 0
  if orientation == "top":
    for i in range(len(c)):
      if c[i] > com:
        com = c[i]
        if i % 2 == 0:
          cplace = 2*i + 1
        else:
          cplace = 2*i + 2
    for j in range(len(t)):
      if t[j] > ten:
        ten = t[j]
        if j % 2 == 0:
          tplace = 2*j + 2
        else:
          tplace = 2*j + 1
  else:
    for i in range(len(c)):
      if c[i] > com:
        com = c[i]
        if i % 2 == 0:
          cplace = 2*i + 2
        else:
          cplace = 2*i + 1
    for j in range(len(t)):
      if t[j] > ten:
        ten = t[j]
        if j % 2 == 0:
          tplace = 2*j + 1
        else:
          tplace = 2*j + 2
  return [com, cplace, ten, tplace]

def lengths(joints_number, length, deg1, deg2):
  """
  (number, number, number, number) -> list
  Given the number of joints in a bridge, its length, and the bottom two angles of the truss, this function calculates the member lengths in a truss of each orientation.
  Ex. (CIV102 Problem Set 5 questions 2 and 3)
  >>>lengths(13, 30, 60, 60)
  [5.0, 5.0, 5.0, 5.0]
  >>>lengths(12, 30, 45, 90)
  [5.0, 7.071067811865455, 5.0]
  """
  ls = []
  num = joints_number // 2
  bot = length/num
  topa = 180 - deg1 - deg2
  out = sin(radians(deg2)) * bot / sin(radians(topa))
  inner = sin(radians(deg1)) * bot / sin(radians(topa))
  ls.extend([bot, out, inner])
  if joints_number % 4 == 1:
    spec = 180 - 2 * deg2
    special = sin(radians(spec)) * inner / sin(radians(deg2))
    ls.append(special)
  elif joints_number % 4 == 3:
    spec = 180 - 2 * deg1
    special = sin(radians(spec)) * out / sin(radians(deg1))
    ls.append(special)
  return ls

def hss_constraints(force, length, direction = "tension"):
  """
  (num, num, string) -> None
  Given force in kN, length in m, and whether the force is compression or tension; prints the minimum area and inertia requirements.
  Ex.
  >>>hss_constraints(406, 3.75, "compression")
  A > 2320 mm2
  I > 8.677*10^6 mm4
  >>>hss_constraints(500, 10)
  A > 1428 mm2
  """
  if direction == "tension":
    print("A >" + str(trunc(force * 1000 / 350)) + " mm2")
  else:
    print("A > " + str(trunc(2 * force * 1000 / 350)) + " mm2")
    print("I > " + str(trunc(3 * 1000000 * force*length**2/(200000*pi**2)) / 1000) + "*10^6 mm4")

def is_valid(member,force):
    '''
    check if input is valid
    (list,list)->boolean
    is_valid([1,2,3,4],[5,6,6])
    >>>0
    '''
    if len(member)!=len(force):
        return 0
    return 1

def dummy_forces(joints_number, deg1, deg2, orientation = "top"):
#Still have to check to see if it works.
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
