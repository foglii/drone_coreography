# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2017-2018 Bitcraze AB
#
#  Crazyflie Nano Quadcopter Client
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
Version of the AutonomousSequence.py example connecting to 10 Crazyflies.
The Crazyflies go straight up, hover a while and land but the code is fairly
generic and each Crazyflie has its own sequence of setpoints that it files
to.

The layout of the positions:
    x2      x1      x0

y3  10              4

            ^ Y
            |
y2  9       6       3
            |
            +------> X

y1  8       5       2



y0  7               1

"""
import time

import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm

# Change uris and sequences according to your setup
# URIs in a swarm using the same radio must also be on the same channel
URI1 = 'radio://0/80/2M/E7E7E7E7E6'
URI2 = 'radio://0/80/2M/E7E7E7E7E7'
URI3 = 'radio://0/80/2M/E7E7E7E7E8'
URI4 = 'radio://0/80/2M/E7E7E7E7E9'
#URI5 = 'radio://0/70/2M/E7E7E7E705'
#URI6 = 'radio://0/70/2M/E7E7E7E706'
#URI7 = 'radio://0/70/2M/E7E7E7E707'
#URI8 = 'radio://0/70/2M/E7E7E7E708'
#URI9 = 'radio://0/70/2M/E7E7E7E709'
#URI10 = 'radio://0/70/2M/E7E7E7E70A'
import numpy as np
import math
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
for it in np.arange(0,2*math.pi,math.pi/8):
            list1.append((0.6*math.cos(it),0.6*math.sin(it),0.5,0.75));
            list2.append((0.6*math.cos(it+math.pi*2/3),0.6*math.sin(it+math.pi*2/3),0.5,0.75))
            list3.append((0.6*math.cos(it+math.pi*4/3),0.6*math.sin(it+math.pi*4/3),0.5,0.75))
            list4.append((0.3*math.cos(it),0.3*math.sin(-it*math.pi*1/3),1,0.75));
            list5.append((0.3*math.cos(it+math.pi*3/3),0.3*math.sin(-it+math.pi*2/3),1,0.75))
            list6.append((0.3*math.cos(it+math.pi*5/3),0.3*math.sin(-it+math.pi*4/3),1,0.75))
for it in np.arange(0,2*math.pi,math.pi/8):
            list1.append((0.6*math.cos(it),0.6*math.sin(it),0.75,0.75));
            list2.append((0.6*math.cos(it+math.pi*2/3),0.6*math.sin(it+math.pi*2/3),0.75,0.75))
            list3.append((0.6*math.cos(it+math.pi*4/3),0.6*math.sin(it+math.pi*4/3),0.75,0.75))
            list4.append((0.6*math.cos(it+math.pi*1/3),0.6*math.sin(it),1,0.75));
            list5.append((0.6*math.cos(it+math.pi*3/3),0.6*math.sin(it+math.pi*2/3),0.75,0.75))
            list6.append((0.6*math.cos(it+math.pi*5/3),0.6*math.sin(it+math.pi*4/3),0.75,0.75))
it=0
list2.append((-0.6+0.4*math.cos(it),0,0.8+0.4*math.sin(it),1.5));
list5.append((-0.6+0.4*math.cos(it+math.pi*2/3),0,0.8+0.4*math.sin(it+math.pi*2/3),1.5))
list3.append((-0.6+0.4*math.cos(it+math.pi*4/3),0,0.8+0.4*math.sin(it+math.pi*4/3),1.5))
list1.append((0.6+0.4*math.cos(it),0,0.8+0.4*math.sin(it),1.5));
list4.append((0.6+0.4*math.cos(it+math.pi*2/3),0,0.8+0.4*math.sin(it+math.pi*2/3),1.5))
list6.append((0.6+0.4*math.cos(it+math.pi*4/3),0,0.8+0.4*math.sin(it+math.pi*4/3),1.5))         
for it in np.arange(0,2*math.pi,math.pi/8):
            list2.append((-0.6+0.4*math.cos(-it),0,0.8+0.4*math.sin(it),1));
            list5.append((-0.6+0.4*math.cos(-it+math.pi*2/3),0,0.8+0.4*math.sin(it+math.pi*2/3),0.75))
            list3.append((-0.6+0.4*math.cos(-it+math.pi*4/3),0,0.8+0.4*math.sin(it+math.pi*4/3),0.75))
            list1.append((0.6+0.4*math.cos(it),0,0.8+0.4*math.sin(it),0.75));
            list4.append((0.6+0.4*math.cos(it+math.pi*2/3),0,0.8+0.4*math.sin(it+math.pi*2/3),0.75))
            list6.append((0.6+0.4*math.cos(it+math.pi*4/3),0,0.8+0.4*math.sin(it+math.pi*4/3),0.75))
            


z0 = 0.4
z = 1.0

x0 = 0.2
x1 = 0
x2 = -0.7

y0 = -0.1
y1 = 0.4
y2 = 0.4
y3 = 1.0

#    x   y   z  time
sequence1 = [
    (x0, y0, z0, 5.0),
    (x0, y0, z, 5.0),
    (x0, y0, z0, 5.0),
]
sequence1 =list1

sequence2 = [
    (x0, y1, z0, 5.0),
    (x0, y1, z, 5.0),
    (x0, y1, z0, 5.0),
]
sequence2=list5

sequence3 = [
    (x0, y2, z0, 3.0),
    (x0, y2, z, 30.0),
    (x0, y2, z0, 3.0),
]


sequence4 = [
    (x0, y3, z0, 3.0),
    (x0, y3, z, 30.0),
    (x0, y3, z0, 3.0),
]
sequence3=list2
sequence4=list4

sequence5 = [
    (x1, y1, z0, 3.0),
    (x1, y1, z, 30.0),
    (x1, y1, z0, 3.0),
]

sequence6 = [
    (x1, y2, z0, 3.0),
    (x1, y2, z, 30.0),
    (x1, y2, z0, 3.0),
]

sequence7 = [
    (x2, y0, z0, 3.0),
    (x2, y0, z, 30.0),
    (x2, y0, z0, 3.0),
]

sequence8 = [
    (x2, y1, z0, 3.0),
    (x2, y1, z, 30.0),
    (x2, y1, z0, 3.0),
]

sequence9 = [
    (x2, y2, z0, 3.0),
    (x2, y2, z, 30.0),
    (x2, y2, z0, 3.0),
]

sequence10 = [
    (x2, y3, z0, 3.0),
    (x2, y3, z, 30.0),
    (x2, y3, z0, 3.0),
]

seq_args = {
    URI1: [sequence1],
    URI2: [sequence2],
    URI3: [sequence3],
    URI4: [sequence4],
    #URI5: [sequence5],
    #URI6: [sequence6],
    #URI7: [sequence7],
    #URI8: [sequence8],
    #URI9: [sequence9],
    #URI10: [sequence10],
}

# List of URIs, comment the one you do not want to fly
uris = {
    URI1,
    URI2,
    URI3,
    URI4,
    #URI5,
    #URI6,
    #URI7,
    #URI8,
    #URI9,
    #URI10
}


def wait_for_param_download(scf):
    while not scf.cf.param.is_updated:
        time.sleep(1.0)
    print('Parameters downloaded for', scf.cf.link_uri)


def arm(scf):
    scf.cf.platform.send_arming_request(True)
    time.sleep(1.0)


def take_off(cf, position):
    take_off_time = 2.0
    sleep_time = 0.1
    steps = int(take_off_time / sleep_time)
    vz = position[2] / take_off_time

    print(vz)

    for i in range(steps):
        cf.commander.send_velocity_world_setpoint(0, 0, vz, 0)
        time.sleep(sleep_time)


def land(cf, position):
    landing_time = 3.0
    sleep_time = 0.1
    steps = int(landing_time / sleep_time)
    vz = -position[2] / landing_time

    print(vz)

    for _ in range(steps):
        cf.commander.send_velocity_world_setpoint(0, 0, vz, 0)
        time.sleep(sleep_time)

    cf.commander.send_stop_setpoint()
    # Hand control over to the high level commander to avoid timeout and locking of the Crazyflie
    cf.commander.send_notify_setpoint_stop()

    # Make sure that the last packet leaves before the link is closed
    # since the message queue is not flushed before closing
    time.sleep(0.1)


def run_sequence(scf, sequence):
    try:
        print('hello')
        cf = scf.cf
        
        arm(scf)
        print('hellopt2')
        take_off(cf, sequence[0])
        for position in sequence:
            print('Setting position {}'.format(position))
            end_time = time.time() + position[3]
            while time.time() < end_time:
                cf.commander.send_position_setpoint(position[0],
                                                    position[1],
                                                    position[2], 0)
                time.sleep(0.1)
        land(cf, sequence[-1])
    except Exception as e:
        print('exception errro')
        print(e)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    cflib.crtp.init_drivers()

    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        # If the copters are started in their correct positions this is
        # probably not needed. The Kalman filter will have time to converge
        # any way since it takes a while to start them all up and connect. We
        # keep the code here to illustrate how to do it.
        swarm.reset_estimators()

        # The current values of all parameters are downloaded as a part of the
        # connections sequence. Since we have 10 copters this is clogging up
        # communication and we have to wait for it to finish before we start
        # flying.
        print('Waiting for parameters to be downloaded...')
        swarm.parallel(wait_for_param_download)

        swarm.parallel(run_sequence, args_dict=seq_args)
