import time

import numpy as np
import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
import sys
import uav_trajectory
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.mem import MemoryElement
from cflib.crazyflie.mem import Poly4D
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.utils import uri_helper

# Change uris and sequences according to your setup
# URIs in a swarm using the same radio must also be on the same channel
URI1 = 'radio://0/100/2M/E7E7E7E7E6'
URI2 = 'radio://0/100/2M/E7E7E7E7E8'
URI3 = 'radio://0/100/2M/E7E7E7E7E9'
#URI4 = 'radio://0/100/2M/E7E7E7E7E9'
URI5 = 'radio://0/100/2M/E7E7E7E7E5'
#URI6 = 'radio://0/100/2M/E7E7E7E7E4'

global iterr
iterr= 1
# dronee1= uav_trajectory.Trajectory()
# dronee1.loadcsv('drone1.csv')
# dronee2= uav_trajectory.Trajectory()
# dronee2.loadcsv('drone2.csv')
# dronee3= uav_trajectory.Trajectory()
# dronee3.loadcsv('drone3.csv')
# dronee4= uav_trajectory.Trajectory()
# dronee4.loadcsv('drone4.csv')
# dronee5= uav_trajectory.Trajectory()
# dronee5.loadcsv('drone5.csv')
# dronee6= uav_trajectory.Trajectory()
# dronee6.loadcsv('drone6.csv')
drone1_txt = np.loadtxt('part1.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone1=drone1_txt[:len(drone1_txt)//2].tolist()
drone1_2=drone1_txt[len(drone1_txt)//2+1:].tolist()
drone1_duration = [np.sum(np.array(drone1)[:,0]), np.sum(np.array(drone1_2)[:,0])]
drone2_txt = np.loadtxt('part2.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone2=drone2_txt[:len(drone2_txt)//2].tolist()
drone2_2=drone2_txt[len(drone2_txt)//2+1:].tolist()
drone2_duration = [np.sum(np.array(drone2)[:,0]), np.sum(np.array(drone2_2)[:,0])]
drone3_txt = np.loadtxt('part3.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone3=drone3_txt[:len(drone3_txt)//2].tolist()
drone3_2=drone3_txt[len(drone3_txt)//2:].tolist()
drone3_duration = [np.sum(np.array(drone3)[:,0]), np.sum(np.array(drone3_2)[:,0])]
drone4_txt = np.loadtxt('part4.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone4=drone4_txt[:len(drone4_txt)//2].tolist()
drone4_2=drone4_txt[len(drone4_txt)//2+1:].tolist()
drone4_duration = [np.sum(np.array(drone4)[:,0]), np.sum(np.array(drone4_2)[:,0])]
drone5_txt = np.loadtxt('part5.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone5=drone5_txt[:len(drone5_txt)//2].tolist()
drone5_2=drone5_txt[len(drone5_txt)//2+1:].tolist()
drone5_duration = [np.sum(np.array(drone5)[:,0]), np.sum(np.array(drone5_2)[:,0])]
drone6_txt = np.loadtxt('part6.csv', delimiter=",", skiprows=1, usecols=range(33), ndmin=2)
drone6=drone6_txt[:len(drone6_txt)//2].tolist()
drone6_2=drone6_txt[len(drone6_txt)//2+1:].tolist()
drone6_duration = [np.sum(np.array(drone6)[:,0]), np.sum(np.array(drone6_2)[:,0])]

seq_args_ = {
    URI1: [1,drone1],
    URI2: [2,drone2],
    URI3: [3,drone3],
    #URI4: [4,drone4],
    URI5: [5,drone5],
    #URI6: [6,drone6],
    
}
seq_args_2 = {
     URI1: [1,drone1_2],
     URI2: [2,drone2_2],
     URI3: [3,drone3_2],
     #URI4: [4,drone4_2],
     URI5: [5,drone5_2],
    #URI6: [6,drone6_2],
    
}
seq_argss_ = {
    URI1: [1,drone1_duration[0]],
    URI2: [2,drone2_duration[0]],
    URI3: [3,drone3_duration[0]],
    #URI4: [4,drone4_duration[0]],
    URI5: [5,drone5_duration[0]],
    #URI6: [6,drone6_duration[0]],

}
seq_argss_2 = {
    URI1: [1,drone1_duration[1]],
    URI2: [2,drone2_duration[1]],
    URI3: [3,drone3_duration[1]],
    #URI4: [4,drone4_duration[1]],
    URI5: [5,drone5_duration[1]],
    #URI6: [6,drone6_duration[1]],

}

# List of URIs, comment the one you do not want to fly
uris = {
   URI1,
    URI2,
    URI3,
    #URI4,
    URI5,
   # URI6,

}

#######
def activate_mellinger_controller(scf):
    scf.cf.param.set_value('stabilizer.controller', '2')


def upload_trajectory(scf, trajectory_id, trajectory):
    """Upload one trajectory to one Crazyflie"""
    try:
        mems = scf.cf.mem.get_mems(MemoryElement.TYPE_TRAJ)
        if not mems:
            print(f"[{scf.cf.link_uri}] No trajectory memory found!")
            if iterr==2:
                commander.land(0.0, 2.0)
            return
        trajectory_mem = mems[0]
        trajectory_mem.trajectory = []

        total_duration = 0
        for row in trajectory:
            duration = row[0]
            x = Poly4D.Poly(row[1:9])
            y = Poly4D.Poly(row[9:17])
            z = Poly4D.Poly(row[17:25])
            yaw = Poly4D.Poly(row[25:33])
            trajectory_mem.trajectory.append(Poly4D(duration, x, y, z, yaw))
            total_duration += duration

        if not trajectory_mem.write_data_sync():
            print(f"[{scf.cf.link_uri}] Upload failed.")
            print(trajectory)
            return

        scf.cf.high_level_commander.define_trajectory(trajectory_id, 0, len(trajectory))
        print(f"[{scf.cf.link_uri}] Trajectory uploaded ({len(trajectory)} segments, {total_duration:.1f}s)")
        print(total_duration)
        return total_duration

    except Exception as e:
        print(f"[{scf.cf.link_uri}] ERROR uploading trajectory: {e}")
        print(trajectory)
        

def landd(scf):
    commander = scf.cf.high_level_commander
    commander.land(0.0,4.0)
    time.sleep(4.0)
    commander.stop()
def run_trajectory(scf, trajectory_id, duration):
    try:
        print('run_trajectory function')
        """Execute a defined trajectory"""
        commander = scf.cf.high_level_commander
        if iterr==1:
            commander.takeoff(0.5, 2.0)
            time.sleep(3.0)
        commander.start_trajectory(trajectory_id, 2.5, False)
        duration_=duration*2.5
        print(f"[{scf.cf.link_uri}] Running trajectory {trajectory_id} for {duration_:.1f}s")
        time.sleep(duration*2.5)
       
        if iterr==2:
                commander.land(0.0, 2.0)
                time.sleep(3.0)
                commander.stop()
        else:  commander.go_to(0, 0, 0.01, 0, 0.5, relative=True, linear=True)
             
    except Exception as e:
        print(f"[{scf.cf.link_uri}] ERROR uploading trajectory: {e}")
        commander.land(0.0, 2.0)


def wait_for_param_download(scf):
    while not scf.cf.param.is_updated:
        time.sleep(0.5)
    print(f"[{scf.cf.link_uri}] Parameters ready")


def light_check(scf):
    scf.cf.param.set_value('led.bitmask', 255)
    time.sleep(1)
    scf.cf.param.set_value('led.bitmask', 0)


# --- Swarm execution ---
if __name__ == '__main__':
    cflib.crtp.init_drivers()

    factory = CachedCfFactory(rw_cache='./cache')

    with Swarm(uris, factory=factory) as swarm:
        try:
            swarm.parallel_safe(wait_for_param_download)
            swarm.parallel_safe(light_check)
            swarm.reset_estimators()
            #swarm.parallel_safe(activate_mellinger_controller)

            # Upload trajectories to each Crazyflie
            durations = swarm.parallel_safe(upload_trajectory, args_dict=seq_args_)
           # durations=[30.3,30.3,30.3,30.3]
           # print("Durations:", durations)
              
            # Wait before flight
            time.sleep(3.0)

            # Run trajectories
            #run_args = {uri: [seq_args_[uri][0], durations[uri]] for uri in seq_args_}
            print("ciao0")
            swarm.parallel_safe(run_trajectory, args_dict=seq_argss_)
            print("ciao")
            iterr= iterr+1
            durations = swarm.parallel_safe(upload_trajectory, args_dict=seq_args_2)
            swarm.parallel_safe(run_trajectory, args_dict=seq_argss_2)
        except KeyboardInterrupt:
            print("Emergency stop triggered by user.")
            swarm.parallel_safe(landd)
        except Exception as e:
            print(f"Errorr: {e}")
            swarm.parallel_safe(landd)
