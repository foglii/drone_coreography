# import numpy as np

# numRobots = 3

# r = 0.5
# height = 1
# w = 2 * np.pi / numRobots
# T = 7 * 2 * np.pi / w

# # horizontal circles
# for i in range(0, numRobots):
#     phase = 2 * np.pi / numRobots * i

#     with open("timed_waypoints_circle{}.csv".format(i), "w") as f:
#         f.write("t,x,y,z,yaw\n")

#         for t in np.linspace(0, T, 100):
#             f.write("{},{},{},{},{}\n".format(t, r * np.cos(w * t + phase), r * np.sin(w * t + phase), height*(1.2-(T-t)/T), 0))



import numpy as np
import math
import csv
from animate_points_3d import animate_trajectories

# Initialize waypoint lists for 6 robots
list1, list2, list3, list4, list5, list6 = [[] for _ in range(6)]
list=[list1,list2,list3,list4,list5,list6]
# max_it=9*math.pi
# half=4.5*math.pi
# it_vector = np.concatenate((
#     np.zeros(36), 
#     np.arange(0, max_it, math.pi/27)
# ))
# # print(len(it_vector)) 
# for it in np.arange(0, max_it, math.pi / 27):
#     if it<=4.5*math.pi:
#         list[0].append((((it/max_it+0.5)*1* math.cos(it)+(it/max_it-0.25)/1)*(1/1),(it/max_it+0.5)*(1/1) * math.sin(it), (it/max_it)*1.5+0.4, 0.1))
#     else: 
#         list[0].append((((-(it-half)/max_it+1)*1* math.cos(it)+((max_it-it)/max_it-0.25)/1),((-(it-half)/max_it+1)*1 * math.sin(it))/1, (it/max_it)*1.5+0.4, 0.1))
#     for i in range(1,6):
#             if len(list[i-1])>6:
#                 list[i].append(list[i-1][-7])
#             else:
#                  list[i].append(((0.5 * math.cos(it - math.pi * i / 3)-0.25)/1.5, 0.5 * math.sin(it - math.pi * i / 3)/1.5, 0.4, 0.1)) 

# dx=0.05
# j=0
# x=0.75
# #each drone separated by 30cm, each it=3cm
# #drone 1 at 0.75, drone 6 at -0.75
# for x in np.arange(-0.75,0.75,dx):
    
#     list[0].append((x,0,1.9,0.1))
#     for i in range(1,6):
        
#         list[i].append(list[i-1][-7])
# #CIRCLE STRAIGHT SESSION
# # #from 0.4 to 1.9: 1.5/6=0.25 ogni 5 step 
# list[0].append((x,0,1.9,1))
# list[1].append((x-0.3,0,1.9,1))
# list[2].append((x-0.6,0,1.9,1))
# list[3].append((x-0.9,0,1.9,1))
# list[4].append((x-1.2,0,1.9,1))
# list[5].append((x-1.5,0,1.9,1))
#PRIMA PARTE FINITAA
# #        
# list[0].append((x,0,1.9,0.2))
# list[1].append((x-0.3,0,1.6,0.8))
# list[2].append((x-0.6,0,1.3,1.4))
# list[3].append((x-0.9,0,1,2))
# list[4].append((x-1.2,0,0.7,2.6))
# list[5].append((x-1.5,0,0.4,3.2))
# #tutti fermi  posizione con tempi complementari  da rifare con i pezzi PIU distanziati
# for _ in range(38):
#     list[0].append((x,0,1.9,0.1))
# for _ in range(32):
#     list[1].append((x-0.3,0,1.6,0.1))
# for _ in range(26):
#     list[2].append((x-0.6,0,1.3,0.1))
# for _ in range(20):
#     list[3].append((x-0.9,0,1,0.1))
# for _ in range(14):
#     list[4].append((x-1.2,0,0.7,0.1))
# for _ in range(8):
#     list[5].append((x-1.5,0,0.4,0.1))

# #poi tornano su al contrario
# list[0].append((x,0,1.3,1.4))
# list[0].append((x,0,0.4,1.8)) #spezzettato i segmenti più lunghi così che interpolino bene
# list[1].append((x-0.3,0,0.7,2))
# list[2].append((x-0.6,0,1,0.8))
# list[3].append((x-0.9,0,1.3,0.8))
# list[4].append((x-1.2,0,1.6,2))
# list[5].append((x-1.5,0,1.3,2))
# list[5].append((x-1.5,0,1.9,1.2))
# #di nuovo fermi
# for _ in range(8):
#     list[0].append((x,0,0.4,0.1))
# for _ in range(20):
#     list[1].append((x-0.3,0,0.7,0.1))
# for _ in range(32):
#     list[2].append((x-0.6,0,1,0.1))
# for _ in range(32):
#     list[3].append((x-0.9,0,1.3,0.1))
# for _ in range(20):
#     list[4].append((x-1.2,0,1.6,0.1))
# for _ in range(8):
#     list[5].append((x-1.5,0,1.9,0.1))


#poi 3 cerchia h 1.3,0.7,0.4
# for _ in range(40):
#     list[0].append((x,0,0.4,0.1))
#     list[1].append((x-0.3,0,0.7,0.1))
#     list[2].append((x-0.6,0,1.1,0.1))

# list[3].append((x-0.9,0,1.1,0.8))
# list[4].append((x-1.2,0,0.7,2))
# list[5].append((x-1.5,0,1.15,1.6))
# list[5].append((x-1.5,0,0.4,1.6))
# for _ in range(32):
#     list[3].append((x-0.9,0,1.1,0.1))
# for _ in range(20):
#     list[4].append((x-1.2,0,0.7,0.1))
# for _ in range(8):
#     list[5].append((x-1.5,0,0.4,0.1))
#c'è il drone 6 stortoooo, da rifare
#iniziano a girare
x=0.75
for it in np.arange(0,4*math.pi,math.pi/16):
    list[0].append(((x) * math.cos(it), (x) * math.sin(it), 0.4, 0.1))
    list[1].append(((x-0.3) * math.cos(it), (x-0.3) * math.sin(it), 0.7, 0.1))
    list[2].append(((x-0.5) * math.cos(it), (x-0.6) * math.sin(it), 1.1, 0.1))
    list[3].append(((x-0.5) * math.cos(it+math.pi), (x-0.6) * math.sin(it+math.pi), 1.1, 0.1))
    list[4].append(((x-0.3) * math.cos(it+math.pi), (x-0.3) * math.sin(it+math.pi), 0.7, 0.1))
    list[5].append(((x) * math.cos(it+math.pi), (x) * math.sin(it+math.pi),0.4, 0.1))
it=4*math.pi
list[0].append(((x) * math.cos(it), (x) * math.sin(it), 0.4, 0.3))
list[1].append(((x-0.3) * math.cos(it), (x-0.3) * math.sin(it), 0.7, 0.3))
list[2].append(((x-0.5) * math.cos(it), (x-0.6) * math.sin(it), 1.1, 0.3))
list[3].append(((x-0.5) * math.cos(it+math.pi), (x-0.6) * math.sin(it+math.pi), 1.1, 0.3))
list[4].append(((x-0.3) * math.cos(it+math.pi), (x-0.3) * math.sin(it+math.pi), 0.7, 0.3))
list[5].append(((x) * math.cos(it+math.pi), (x) * math.sin(it+math.pi),0.4, 0.3))

# # # # #2 giri
it=0
 #cambia 2 con 5
list[0].append((x * math.cos(it), x * math.sin(it), 0.7, 1))
list[1].append((x * math.cos(it + math.pi * 2 / 3), x * math.sin(it + math.pi * 2 / 3), 0.7, 1))
list[5].append((x * math.cos(it + math.pi * 4 / 3), x * math.sin(it + math.pi * 4 / 3), 0.7, 1))
list[3].append(((x-0.3) * math.cos(it+math.pi*1/3), (x-0.3) * math.sin(it * math.pi * 1 / 3), 1.1, 1))
list[4].append(((x-0.3)  * math.cos(it + math.pi * 3 / 3), (x-0.3) * math.sin(it + math.pi * 3 / 3), 1.1, 1))
list[2].append(((x-0.3) * math.cos(it + math.pi * 5 / 3), (x-0.3)  * math.sin(it + math.pi * 5 / 3), 1.1, 1))
list[0].append((x * math.cos(it), x * math.sin(it), 0.7, 0.1))
list[1].append((x * math.cos(it + math.pi * 2 / 3), x * math.sin(it + math.pi * 2 / 3), 0.7, 0.1))
list[5].append((x * math.cos(it + math.pi * 4 / 3), x * math.sin(it + math.pi * 4 / 3), 0.7, 0.1))
list[3].append(((x-0.3) * math.cos(it+math.pi*1/3), (x-0.3) * math.sin(it * math.pi * 1 / 3), 1.1, 0.1))
list[4].append(((x-0.3)  * math.cos(it + math.pi * 3 / 3), (x-0.3) * math.sin(it + math.pi * 3 / 3), 1.1, 0.1))
list[2].append(((x-0.3) * math.cos(it + math.pi * 5 / 3), (x-0.3)  * math.sin(it + math.pi * 5 / 3), 1.1, 0.1))

for it in np.arange(0, 6 * math.pi, math.pi /16): 
    list[0].append((x * math.cos(it), x * math.sin(it), 0.7, 0.1))
    list[1].append((x * math.cos(it + math.pi * 2 / 3), x * math.sin(it + math.pi * 2 / 3), 0.7, 0.1))
    list[5].append((x * math.cos(it + math.pi * 4 / 3), x * math.sin(it + math.pi * 4 / 3), 0.7, 0.1))
    list[3].append(((x-0.3) * math.cos(it+math.pi*1/3), (x-0.3) * math.sin(it * math.pi * 1 / 3), 1.1, 0.1))
    list[4].append(((x-0.3)  * math.cos(it + math.pi * 3 / 3), (x-0.3) * math.sin(it + math.pi * 3 / 3), 1.1, 0.1))
    list[2].append(((x-0.3) * math.cos(it + math.pi * 5 / 3), (x-0.3)  * math.sin(it + math.pi * 5 / 3), 1.1, 0.1))
#0.9 turni del loop sopra poi 12 turni del loop dopo
#0.2 di transizione
#altrimenti, easier fix, list che lagga in alto rimane un po in alto 
#dA RIFARE 1 e 3
it=0
list[0].append((1.0 * math.cos(it), 0.9 * math.sin(it), 0.75, 1))
list[1].append((1.0 * math.cos(it + math.pi * 2 / 3), 0.9 * math.sin(it + math.pi * 2 / 3), 0.75, 1))
list[5].append((1.0 * math.cos(it + math.pi * 4 / 3), 0.9 * math.sin(it + math.pi * 4 / 3), 0.75, 1))
list[3].append((1.0 * math.cos(it + math.pi * 1 / 3), 0.9 * math.sin(it+math.pi*1/3), 0.75, 1))
list[4].append((1.0 * math.cos(it + math.pi * 3 / 3), 0.9 * math.sin(it + math.pi * 3 / 3), 0.75, 1))
list[2].append((1.0 * math.cos(it + math.pi * 5 / 3), 0.9 * math.sin(it + math.pi * 5 / 3), 0.75, 1))
list[0].append((1.0 * math.cos(it), 0.9 * math.sin(it), 0.75, 0.1))
list[1].append((1.0 * math.cos(it + math.pi * 2 / 3), 0.9 * math.sin(it + math.pi * 2 / 3), 0.75, 0.1))
list[5].append((1.0 * math.cos(it + math.pi * 4 / 3), 0.9 * math.sin(it + math.pi * 4 / 3), 0.75, 0.1))
list[3].append((1.0 * math.cos(it + math.pi * 1 / 3), 0.9 * math.sin(it+math.pi*1/3), 0.75, 0.1))
list[4].append((1.0 * math.cos(it + math.pi * 3 / 3), 0.9 * math.sin(it + math.pi * 3 / 3), 0.75, 0.1))
list[2].append((1.0 * math.cos(it + math.pi * 5 / 3), 0.9 * math.sin(it + math.pi * 5 / 3), 0.75, 0.1))


for it in np.arange(0, 4 * math.pi, math.pi / 32):
    list[0].append((1.0 * math.cos(it), 0.9 * math.sin(it), 0.75, 0.1))
    list[1].append((1.0 * math.cos(it + math.pi * 2 / 3), 0.9 * math.sin(it + math.pi * 2 / 3), 0.75, 0.1))
    list[5].append((1.0 * math.cos(it + math.pi * 4 / 3), 0.9 * math.sin(it + math.pi * 4 / 3), 0.75, 0.1))
    list[3].append((1.0 * math.cos(it + math.pi * 1 / 3), 0.9 * math.sin(it+math.pi*1/3), 0.75, 0.1))
    list[4].append((1.0 * math.cos(it + math.pi * 3 / 3), 0.9 * math.sin(it + math.pi * 3 / 3), 0.75, 0.1))
    list[2].append((1.0 * math.cos(it + math.pi * 5 / 3), 0.9 * math.sin(it + math.pi * 5 / 3), 0.75, 0.1))
#stai un secondo fermo
list[0].append((1.0 * math.cos(it), 0.9 * math.sin(it), 0.75, 0.1))
list[1].append((1.0 * math.cos(it + math.pi * 2 / 3), 0.9 * math.sin(it + math.pi * 2 / 3), 0.75, 0.1))
list[5].append((1.0 * math.cos(it + math.pi * 4 / 3), 0.9 * math.sin(it + math.pi * 4 / 3), 0.75, 0.1))
list[3].append((1.0 * math.cos(it + math.pi * 1 / 3), 0.9 * math.sin(it+math.pi*1/3), 0.75, 0.1))
list[4].append((1.0 * math.cos(it + math.pi * 3 / 3), 0.9 * math.sin(it + math.pi * 3 / 3), 0.75, 0.1))
list[2].append((1.0 * math.cos(it + math.pi * 5 / 3), 0.9 * math.sin(it + math.pi * 5 / 3), 0.75, 0.1))
# #prima parte finita (48.2 secondi)
it = 0
list[1].append((-0.6 + 0.4 * math.cos(-it), 0, 0.6 + 0.4 * math.sin(-it), 1.5))
list[4].append((-0.6 + 0.4 * math.cos(-it + math.pi * 2 / 3), 0, 0.6 + 0.4 * math.sin(-it + math.pi * 2 / 3), 1.5))
list[5].append((-0.6 + 0.4 * math.cos(-it + math.pi * 4 / 3), 0, 0.6 + 0.4 * math.sin(-it + math.pi * 4 / 3), 1.5))
list[0].append((0.6 + 0.4* math.cos(it), 0, 0.6 + 0.4 * math.sin(it), 1.5))
list[3].append((0.6 + 0.4 * math.cos(it + math.pi * 2 / 3), 0, 0.6 + 0.4 * math.sin(it + math.pi * 2 / 3), 1.5))
list[2].append((0.6 + 0.4 * math.cos(it + math.pi * 4 / 3), 0, 0.6 + 0.4 * math.sin(it + math.pi * 4 / 3), 1.5))
for it in np.arange(0, 6 * math.pi, math.pi / 16):
    list[1].append((-0.6 + 0.4 * math.cos(-it), 0, 0.6 + 0.4 * math.sin(-it), 0.1))
    list[4].append((-0.6 + 0.4 * math.cos(-it + math.pi * 2 / 3), 0, 0.6 + 0.4 * math.sin(-it + math.pi * 2 / 3), 0.1))
    list[5].append((-0.6 + 0.4 * math.cos(-it + math.pi * 4 / 3), 0, 0.6 + 0.4 * math.sin(-it + math.pi * 4 / 3), 0.1))
    list[0].append((0.6 + 0.4 * math.cos(it), 0, 0.6 + 0.4 * math.sin(it), 0.1))
    list[3].append((0.6 + 0.4 * math.cos(it + math.pi * 2 / 3), 0, 0.6 + 0.4 * math.sin(it + math.pi * 2 / 3), 0.1))
    list[2].append((0.6 + 0.4 * math.cos(it + math.pi * 4 / 3), 0, 0.6 + 0.4 * math.sin(it + math.pi * 4 / 3), 0.1)) 


#parte transitoria pre figure 8
it=6*math.pi
list[1].append((-0.6 + 0.4 * math.cos(-it), 0, 0.6 + 0.4 * math.sin(-it), 0.1))
list[4].append((-0.6 + 0.4 * math.cos(-it + math.pi * 2 / 3), 0, 0.6 + 0.4 * math.sin(-it + math.pi * 2 / 3), 0.1))
list[5].append((-0.6 + 0.4 * math.cos(-it + math.pi * 4 / 3), 0, 0.6 + 0.4 * math.sin(-it + math.pi * 4 / 3), 0.1))
list[0].append((0.6 + 0.4 * math.cos(it), 0, 0.6 + 0.4 * math.sin(it), 0.1))
list[3].append((0.6 + 0.4 * math.cos(it + math.pi * 2 / 3), 0, 0.6 + 0.4 * math.sin(it + math.pi * 2 / 3), 0.1))
list[2].append((0.6 + 0.4 * math.cos(it + math.pi * 4 / 3), 0, 0.6 + 0.4 * math.sin(it + math.pi * 4 / 3), 0.1)) 
it=0
phase=[math.pi*4/3+math.pi*2,math.pi*2, math.pi * 2/ 3+math.pi*2, math.pi*4, math.pi * 4 / 3, math.pi * 2 / 3]
pmod=phase
for i in range(6):

    pmod[i] =pmod[i]+math.pi/27;
    if(pmod[i]>(2*math.pi) and pmod[i]<=(4*math.pi)):
        list[i].append((0.6+0.4*math.cos(pmod[i]+math.pi),0.3*math.cos(pmod[i]/2),0.6 + 0.4 * math.sin(pmod[i]+math.pi), 1))
    elif (pmod[i]>(4*math.pi)):
        pmod[i]=pmod[i]-(4*math.pi)
        list[i].append((-0.6+0.4*math.cos(pmod[i]),0.3*math.cos(pmod[i]/2),0.6 + 0.4 * math.sin(pmod[i]+math.pi), 1))
    elif(pmod[i]<=(2*math.pi)):
        list[i].append((-0.6+0.4*math.cos(pmod[i]),0.3*math.cos(pmod[i]/2),0.6 + 0.4 * math.sin(pmod[i]+math.pi), 1))
##PARTE FIGURE 8
it=0
# #phase=[math.pi*1/3,0, math.pi * 4 / 3, math.pi, math.pi * 2 / 3, math.pi * 5 / 3]
# phase=[math.pi*1/3,0, math.pi * 5 / 3, math.pi, math.pi * 2 / 3, math.pi * 4 / 3]
#phase=[math.pi*4/3+math.pi*2,math.pi*2, math.pi * 2/ 3+math.pi*2, math.pi*4, math.pi * 4 / 3, math.pi * 2 / 3]
pmod=phase
phase_z=phase
side=[False,True,False,False,True,True] #0 dx 1 sx
for it in np.arange(0, 6*math.pi, math.pi / 27):
   # print((phase[1]/math.pi))
    for i in range(6):

        pmod[i] =pmod[i]+math.pi/27;
        if(pmod[i]>(2*math.pi) and pmod[i]<=(4*math.pi)):
             list[i].append((0.6+0.4*math.cos(pmod[i]+math.pi),0.2*math.cos(pmod[i]/2),0.6 + 0.4 * math.sin(pmod[i]+math.pi), 0.1))
        elif (pmod[i]>(4*math.pi)):
            pmod[i]=pmod[i]-(4*math.pi)
            list[i].append((-0.6+0.4*math.cos(pmod[i]),0.2*math.cos(pmod[i]/2),0.6 + 0.4 * math.sin(pmod[i]+math.pi), 0.1))
        elif(pmod[i]<=(2*math.pi)):
            list[i].append((-0.6+0.4*math.cos(pmod[i]),0.2*math.cos(pmod[i]/2),0.6 + 0.4 * math.sin(pmod[i]+math.pi), 0.1))

    






    # for i in range(6):
    #     pmod = math.remainder(phase_z[i] / math.pi, 2)
       
    #     if ((math.isclose(abs(pmod), 1.0, abs_tol=1e-3) and not side[i]) or 
    #         (math.isclose((pmod), 0.0, abs_tol=1e-3) and side[i])):

    #         side[i]=not side[i]
    #         phase[i]=phase[i]+(math.pi*(not side[i])-math.pi*side[i])

    #         #phase[i]=phase[i]+math.pi
    #     #phase_wrapped = phase[i] % (2 * math.pi)

    #     if not side[i]:
    #         list[i].append((0.5+0.5*math.cos(phase[i]),0.2*math.sin(phase[i]/2),0.8 + 0.4 * math.sin(phase[i]), 0.1))
    #         phase[i]=phase[i]+(math.pi/36)
    #         phase_z[i]=phase_z[i]+(math.pi/36)

            
            
            
    #     if side[i]: 
    #         list[i].append((-0.5+0.5*math.cos(phase[i]),0.2*math.cos(phase[i]/2),0.8 + 0.4 * math.sin(phase[i]), 0.1))
    #         phase[i]=phase[i]-(math.pi/36)
    #         phase_z[i]=phase_z[i]-(math.pi/36)

            

           
   # print(phase[3]/math.pi)

#=== Helper: compute cumulative time based on distance ===
def compute_cumulative_time(waypoints, speed=1.0):
    times = [0.0]
    for i in range(1, len(waypoints)):
        x1, y1, z1, _ = waypoints[i - 1]
        x2, y2, z2, _ = waypoints[i]
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        times.append(times[-1] + dist / speed)
    return times

# === Write each robot's waypoints with cumulative time ===
#all_lists = [list1, list2, list3, list4, list5, list6]
all_trajs = [list[0],list[1],list[2],list[3],list[4],list[5]]
""" 
for i, waypoints in enumerate(all_lists):
    times = compute_cumulative_time(waypoints)
    filename = f"timed_waypoints_circle{i+1}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["t", "x", "y", "z", "yaw"])
        for t, (x, y, z, yaw) in zip(times, waypoints):
            writer.writerow([t*3, x, y, z, yaw])
    print(f" Saved {filename} with {len(waypoints)} waypoints (final time {times[-1]:.2f}s).") """

for i, waypoints in enumerate(all_trajs):
    time=0
    times = compute_cumulative_time(waypoints)
    filename = f"timed_waypoints_circle{i+1}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["t", "x", "y", "z", "yaw"])
        for  (x, y, z, t) in waypoints:
            time=time+t
            writer.writerow([time, x, y, z,0])
    print(f" Saved {filename} with {len(waypoints)} waypoints (final time {time:.2f}s).")

print(np.shape(list[0]))

# Call the animation
animate_trajectories(all_trajs, out_name='output_.mp4', fps=20,xlim=(-1,1), ylim=(-1,1), zlim=(0,2))
