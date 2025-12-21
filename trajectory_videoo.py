#!/usr/bin/env python

import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import argparse
from animate_points_3d import animate_trajectories 

import uav_trajectory

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  #parser.add_argument("trajectory", type=str, help="CSV files containing trajectory")
  parser.add_argument("--stretchtime", type=float, help="stretch time factor (smaller means faster)")
  args = parser.parse_args()
  trajectory_animate=np.empty((0, 4))
  traj1= uav_trajectory.Trajectory()
  traj1.loadcsv('figure8_1.csv')
  traj2= uav_trajectory.Trajectory()
  traj2.loadcsv('figure8_2.csv')
  traj3= uav_trajectory.Trajectory()
  traj3.loadcsv('figure8_3.csv')
  traj4= uav_trajectory.Trajectory()
  traj4.loadcsv('figure8_4.csv')
  traj5= uav_trajectory.Trajectory()
  traj5.loadcsv('figure8_5.csv')
  traj6= uav_trajectory.Trajectory()
  traj6.loadcsv('figure8_6.csv')
  # traj1=uav_trajectory.Trajectory()
  # traj2=uav_trajectory.Trajectory()
  # traj3=uav_trajectory.Trajectory()
  # traj4=uav_trajectory.Trajectory()
  # traj5=uav_trajectory.Trajectory()
  # traj6=uav_trajectory.Trajectory()


  # with open('drone1.csv', 'r') as f:
  #   reader = csv.reader(f)
  #   drone1 = [
  #       [float(x_clean) for x in row if (x_clean := re.sub(r'[^0-9eE+.\-]', '', x))]
  #       for row in reader if any(row)  # skip completely empty rows
  #   ]
  #   print(drone1)




  # #drone1 = [list(map(float, row)) for row in __import__("csv").reader(open("drone1.csv", encoding="utf-8-sig"))]
  # drone2 = [list(map(float, row)) for row in __import__("csv").reader(open("drone2.csv", encoding="utf-8-sig"))]
  # drone3 = [list(map(float, row)) for row in __import__("csv").reader(open("drone3.csv", encoding="utf-8-sig"))]
  # drone4 = [list(map(float, row)) for row in __import__("csv").reader(open("drone4.csv", encoding="utf-8-sig"))]
  # drone5 = [list(map(float, row)) for row in __import__("csv").reader(open("drone5.csv", encoding="utf-8-sig"))]
  # drone6 = [list(map(float, row)) for row in __import__("csv").reader(open("drone6.csv", encoding="utf-8-sig"))]
  # drone1=[[3.213333,0.263739,-0.000000,-0.000000,-1.074997,0.779330,-0.169312,0.006477,0.001014,0.148271,0.000000,-0.000000,2.170789,-2.910743,1.397820,-0.292176,0.022735,0.416060,0.000000,-0.000000,0.213684,-0.235018,0.106662,-0.022379,0.001791,-0.000000,0.000000,-0.000000,0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.213333,0.397399,1.001530,-0.604390,-0.458644,0.006427,0.191343,-0.060380,0.005223,-0.497694,0.701215,0.689870,0.043407,-0.505577,0.150885,-0.001088,-0.002268,0.690091,0.087554,-0.015080,0.038867,-0.029852,0.010059,-0.001497,0.000075,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.213333,0.403631,1.903122,-0.122754,-1.194231,0.219307,0.161701,-0.056640,0.004966,-1.111871,0.101135,1.792091,-0.060432,-0.723624,0.265654,-0.028691,0.000359,0.986636,0.096910,-0.005844,-0.019260,0.034473,-0.020272,0.005098,-0.000469,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.213333,-0.377392,1.271565,0.752781,-0.731779,-0.243006,0.236592,-0.049231,0.003144,-0.740508,-0.883584,1.221625,0.370234,-0.346539,-0.023503,0.035762,-0.004489,1.283417,0.099026,-0.000821,-0.035326,0.049517,-0.026724,0.006409,-0.000571,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.213333,-0.725646,0.346610,1.032782,-0.361522,-0.178083,0.058255,0.005452,-0.001902,-0.191080,-1.166991,0.418890,0.469011,-0.007197,-0.156225,0.048106,-0.004074,1.580622,0.099539,0.001548,-0.035743,0.045799,-0.024080,0.005830,-0.000538,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.213333,-0.698260,-0.245618,0.877832,-0.115471,-0.390365,0.262328,-0.064759,0.005658,0.201996,-0.695306,0.279757,0.963919,-1.232674,0.593355,-0.129317,0.010647,1.877754,0.079850,-0.044453,-0.073546,0.095251,-0.040639,0.007184,-0.000417,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.050000,0.749903,-0.000000,-0.000000,0.033174,-0.002825,-0.021529,0.009878,-0.001223,0.000000,-0.000000,0.000000,0.000000,0.000000,-0.000000,0.000000,-0.000000,1.898654,0.000000,0.000000,0.301357,0.015127,-0.211621,0.084965,-0.009594,0.000000,-0.000000,0.000000,0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.050000,0.714001,0.042474,0.082028,-0.102384,-0.019768,0.052061,-0.018722,0.002073,-0.000000,-0.000000,-0.000000,-0.000000,-0.000000,-0.000000,0.000000,-0.000000,0.745516,-0.947023,0.672895,-0.043904,0.035408,-0.107020,0.044592,-0.005370,-0.000000,-0.000000,-0.000000,-0.000000,-0.000000,-0.000000,0.000000,-0.000000],


  # [3.213333,0.612586,-0.768786,-1.117109,-0.167465,1.456831,-0.811470,0.170248,-0.012768,0.408892,1.183513,-0.341196,-1.799455,1.141850,-0.174576,-0.014199,0.003719,0.399173,0.005961,0.011480,-0.056496,0.064607,-0.032204,0.007440,-0.000652,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.213333,0.622457,-0.804961,-1.308095,0.098531,1.448389,-0.907587,0.209325,-0.017211,0.438604,1.199152,-0.823857,-0.694534,-0.029479,0.460882,-0.180973,0.020288,0.400389,0.002982,-0.010699,-0.048591,0.132376,-0.106240,0.034092,-0.003769,0.000000,-0.000000,0.000000,-0.000000,0.000000,0.000000,-0.000000,0.000000],
  # [3.213333,0.842295,-0.100142,-0.820031,-0.316879,0.313813,0.075907,-0.061897,0.007880,0.033532,0.504674,0.113272,2.129840,-3.546073,1.889328,-0.421888,0.034358,0.602356,0.398629,-0.120744,-0.757409,0.943031,-0.455134,0.099738,-0.008262,-0.000000,-0.000000,-0.000000,0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.213333,0.735490,0.414418,-1.546790,-0.116463,0.562165,-0.119174,-0.011019,0.003260,-0.206973,1.300202,0.310319,-0.114341,-1.187396,0.833094,-0.201077,0.016667,0.693077,0.040950,0.053272,-0.277900,0.306049,-0.146749,0.032684,-0.002768,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.213333,0.740173,0.415761,-1.552172,-0.343867,0.930394,-0.334426,0.043530,-0.001804,-0.203199,1.379642,0.396593,-0.594426,-0.719627,0.641189,-0.165254,0.014188,0.699565,0.020919,0.003164,-0.135564,0.191954,-0.107216,0.026678,-0.002455,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.213333,0.800320,0.564944,-1.553768,-0.764037,1.064128,-0.220775,-0.017088,0.005834,-0.186814,1.459740,0.620623,-0.354002,-1.528363,1.171979,-0.302138,0.026756,0.719639,0.081920,0.016459,-0.197140,0.204979,-0.091707,0.019251,-0.001552,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
  # [3.213333,0.864701,0.280176,-1.601091,0.547435,-0.825205,0.887796,-0.309424,0.034433,-0.235719,1.521282,0.677328,0.360664,-3.026063,2.179095,-0.580872,0.054106,0.749383,0.007541,0.006515,-0.049444,0.057634,-0.028140,0.006289,-0.000531,0.000000,-0.000000,-0.000000,-0.000000,-0.000000,-0.000000,0.000000,-0.000000]]
  
  # # duration,x^0,x^1,x^2,x^3,x^4,x^5,x^6,x^7,y^0,y^1,y^2,y^3,y^4,y^5,y^6,y^7,z^0,z^1,z^2,z^3,z^4,z^5,z^6,z^7,yaw^0,yaw^1,yaw^2,yaw^3,yaw^4,yaw^5,yaw^6,yaw^7

  # traj1.polynomials = [uav_trajectory.Polynomial4D(row[0], row[1:9], row[9:17], row[17:25], row[25:33]) for row in drone1]
  # traj1.duration = np.sum(np.array(drone1)[:,0])
  # traj2.polynomials = [uav_trajectory.Polynomial4D(row[0], row[1:9], row[9:17], row[17:25], row[25:33]) for row in drone2]
  # traj2.duration = np.sum(np.array(drone2)[:,0])
  # traj3.polynomials = [uav_trajectory.Polynomial4D(row[0], row[1:9], row[9:17], row[17:25], row[25:33]) for row in drone3]  
  # traj3.duration = np.sum(np.array(drone3)[:,0])
  # traj4.polynomials = [uav_trajectory.Polynomial4D(row[0], row[1:9], row[9:17], row[17:25], row[25:33]) for row in drone4]  
  # traj4.duration = np.sum(np.array(drone4)[:,0])
  # traj5.polynomials = [uav_trajectory.Polynomial4D(row[0], row[1:9], row[9:17], row[17:25], row[25:33]) for row in drone5]  
  # traj5.duration = np.sum(np.array(drone5)[:,0])
  # traj6.polynomials = [uav_trajectory.Polynomial4D(row[0], row[1:9], row[9:17], row[17:25], row[25:33]) for row in drone6]  
  # traj6.duration = np.sum(np.array(drone6)[:,0])
  





  #all_traj=[drone1,drone2,drone3,drone4,drone5,drone6]
  # duration=np.empty(len(all_traj))
  # for i in range(len(all_traj)):
  #   duration[i] = sum(row[0] for row in all_traj[i])
  
  all_traj=[traj1,traj2,traj3,traj4,traj5,traj6]
  t_old=0
  trajectory_animate=[np.empty((0, 4)) for _ in range(len(all_traj))]
for ii in range(len(all_traj)):
  t_old=0
  if args.stretchtime:
    all_traj[ii].stretchtime(args.stretchtime)

  ts = np.arange(0, all_traj[ii].duration, 0.01)
  evals = np.empty((len(ts), 15))
  for t, i in zip(ts, range(0, len(ts))):
    e = all_traj[ii].eval(t)
    evals[i, 0:3]  = e.pos
    evals[i, 3:6]  = e.vel
    evals[i, 6:9]  = e.acc
    evals[i, 9:12] = e.omega
    evals[i, 12]   = e.yaw
    evals[i, 13]   = e.roll
    evals[i, 14]   = e.pitch
    #trajectory_animate= np.concatenate(trajectory_animate, np.concatenate(e.pos,t))
    new_row = np.append(e.pos, t-t_old).reshape(1, -1)  # Create a row vector [pos, t]
    trajectory_animate[ii] = np.concatenate([trajectory_animate[ii], new_row], axis=0)
    t_old=t
  


  velocity = np.linalg.norm(evals[:,3:6], axis=1)
  acceleration = np.linalg.norm(evals[:,6:9], axis=1)
  omega = np.linalg.norm(evals[:,9:12], axis=1)

  # print stats
  print("max speed (m/s): ", np.max(velocity))
  print("max acceleration (m/s^2): ", np.max(acceleration))
  print("max omega (rad/s): ", np.max(omega))
  print("max roll (deg): ", np.max(np.degrees(evals[:,13])))
  print("max pitch (deg): ", np.max(np.degrees(evals[:,14])))

  # Create 3x1 sub plots
  gs = gridspec.GridSpec(6, 1)
  fig = plt.figure()

  ax = plt.subplot(gs[0:2, 0], projection='3d') # row 0
 #x,y,z sono le tre colonne di evals
 # #manca modo di considerare il tempo
  
  ax.plot(evals[:,0], evals[:,1], evals[:,2])

  ax = plt.subplot(gs[2, 0]) # row 2
  ax.plot(ts, velocity)                             
  ax.set_ylabel("velocity [m/s]")

  ax = plt.subplot(gs[3, 0]) # row 3
  ax.plot(ts, acceleration)
  ax.set_ylabel("acceleration [m/s^2]")

  ax = plt.subplot(gs[4, 0]) # row 4
  ax.plot(ts, omega)
  ax.set_ylabel("omega [rad/s]")

  ax = plt.subplot(gs[5, 0]) # row 5
  ax.plot(ts, np.degrees(evals[:,12]))
  ax.set_ylabel("yaw [deg]")



  # ax = plt.subplot(gs[6, 0]) # row 5
  # ax.plot(ts, np.degrees(evals[:,13]))
  # ax.set_ylabel("roll [deg]")

  # ax = plt.subplot(gs[7, 0]) # row 5
  # ax.plot(ts, np.degrees(evals[:,14]))
  # ax.set_ylabel("pitch [deg]")

 # plt.show()
  print(np.shape(trajectory_animate[ii]))
  print(trajectory_animate[ii])
print(trajectory_animate)
 # complete=np.append(complete,trajectory_animate)
animate_trajectories(trajectory_animate, out_name='output.mp4', fps=20,xlim=(-2,2), ylim=(-2,2), zlim=(0,2)) 

