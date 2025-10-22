import time

import cflib.crtp
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
import sys

from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.mem import MemoryElement
from cflib.crazyflie.mem import Poly4D
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.utils import uri_helper

# Change uris and sequences according to your setup
# URIs in a swarm using the same radio must also be on the same channel
URI1 = 'radio://0/80/2M/E7E7E7E7E6'
URI2 = 'radio://0/80/2M/E7E7E7E7E8'
URI3 = 'radio://0/80/2M/E7E7E7E7E9'
URI4 = 'radio://0/70/2M/E7E7E7E704'
URI5 = 'radio://0/70/2M/E7E7E7E705'
URI6 = 'radio://0/70/2M/E7E7E7E706'
URI7 = 'radio://0/70/2M/E7E7E7E707'
URI8 = 'radio://0/70/2M/E7E7E7E708'
URI9 = 'radio://0/70/2M/E7E7E7E709'
URI10 = 'radio://0/70/2M/E7E7E7E70A'

# duration,x^0,x^1,x^2,x^3,x^4,x^5,x^6,x^7,y^0,y^1,y^2,y^3,y^4,y^5,y^6,y^7,z^0,z^1,z^2,z^3,z^4,z^5,z^6,z^7,yaw^0,yaw^1,yaw^2,yaw^3,yaw^4,yaw^5,yaw^6,yaw^7
figure8_1=[[4.200000,0.436550,0.000000,-0.000000,-2.277598,2.417960,-0.939501,0.158453,-0.009823,0.311736,-0.000000,0.000000,0.476357,-0.902670,0.491394,-0.105320,0.007874,0.012440,0.000000,0.000000,0.024346,-0.011788,0.001352,0.000174,-0.000032,-0.000000,-0.000000,-0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,-0.449914,-0.591868,1.167036,0.428802,-0.821013,0.293713,-0.039549,0.001711,0.350495,-1.085656,-0.955792,1.689428,-0.508620,-0.034156,0.030546,-0.003008,0.138603,0.042894,0.000991,-0.023569,0.022652,-0.008848,0.001572,-0.000105,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,0.153817,1.172877,-0.368171,-1.524995,1.140982,-0.286509,0.026121,-0.000409,-0.492381,0.358045,1.206577,-0.381156,-0.628342,0.390619,-0.078624,0.005336,0.280522,0.038524,-0.001517,-0.019376,0.021795,-0.009124,0.001682,-0.000115,-0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,0.157916,-1.126525,-0.383039,1.358529,-0.487612,-0.014777,0.026655,-0.002821,0.495634,0.369808,-1.220220,-0.415446,0.992911,-0.401340,0.062324,-0.003324,0.420385,0.037325,-0.001635,-0.021711,0.025916,-0.011212,0.002101,-0.000144,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,-0.448708,0.673386,1.166163,-0.667801,-0.617346,0.492188,-0.114053,0.008755,-0.349299,-1.059790,0.951562,1.612399,-1.886081,0.721903,-0.120441,0.007494,0.556822,0.040816,0.006547,-0.022889,0.015628,-0.004142,0.000423,-0.000010,0.000000,-0.000000,0.000000,-0.000000,-0.000000,-0.000000,0.000000,-0.000000]]

# duration,x^0,x^1,x^2,x^3,x^4,x^5,x^6,x^7,y^0,y^1,y^2,y^3,y^4,y^5,y^6,y^7,z^0,z^1,z^2,z^3,z^4,z^5,z^6,z^7,yaw^0,yaw^1,yaw^2,yaw^3,yaw^4,yaw^5,yaw^6,yaw^7
figure8_2=[[4.200000,-0.471752,-0.000000,0.000000,0.595609,-0.269521,-0.025472,0.025312,-0.002842,0.217864,0.000000,-0.000000,-2.184605,2.517760,-1.048368,0.187965,-0.012319,0.012440,0.000000,0.000000,0.024346,-0.011788,0.001352,0.000174,-0.000032,-0.000000,-0.000000,-0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,-0.082751,1.299652,0.252624,-1.871082,1.041823,-0.192679,0.006772,0.000850,-0.560866,0.027058,1.482017,-0.462755,-0.461839,0.272382,-0.049549,0.002979,0.138603,0.042894,0.000991,-0.023569,0.022652,-0.008848,0.001572,-0.000105,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,0.349529,-0.857538,-0.865010,0.937296,0.151919,-0.272765,0.069952,-0.005474,0.384026,0.834986,-0.936943,-1.147598,1.342722,-0.465127,0.066542,-0.003368,0.280522,0.038524,-0.001517,-0.019376,0.021795,-0.009124,0.001682,-0.000115,-0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,-0.499447,0.325268,1.213440,-0.588514,-0.299504,0.218569,-0.041593,0.002503,-0.110997,-1.121363,0.277035,1.284570,-0.821648,0.150444,-0.001560,-0.001207,0.420385,0.037325,-0.001635,-0.021711,0.025916,-0.011212,0.002101,-0.000144,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,0.527012,0.705317,-1.405269,-1.433743,2.310812,-1.015074,0.186501,-0.012518,-0.215677,1.131724,0.542490,-1.441558,0.458577,0.046808,-0.035424,0.003635,0.556822,0.040816,0.006547,-0.022889,0.015628,-0.004142,0.000423,-0.000010,0.000000,-0.000000,0.000000,-0.000000,-0.000000,-0.000000,0.000000,-0.000000]]
# duration,x^0,x^1,x^2,x^3,x^4,x^5,x^6,x^7,y^0,y^1,y^2,y^3,y^4,y^5,y^6,y^7,z^0,z^1,z^2,z^3,z^4,z^5,z^6,z^7,yaw^0,yaw^1,yaw^2,yaw^3,yaw^4,yaw^5,yaw^6,yaw^7
figure8_3=[[
4.200000,0.056843,0.000000,0.000000,1.509020,-1.939282,0.872433,-0.166030,0.011420,-0.517725,-0.000000,0.000000,1.598631,-1.477476,0.494441,-0.070416,0.003573,0.012440,0.000000,0.000000,0.024346,-0.011788,0.001352,0.000174,-0.000032,-0.000000,-0.000000,-0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,0.528116,-0.621776,-1.411938,1.179380,0.041830,-0.205471,0.051479,-0.003815,0.212412,1.125581,-0.531663,-1.434257,1.188722,-0.327127,0.035165,-0.001066,0.138603,0.042894,0.000991,-0.023569,0.022652,-0.008848,0.001572,-0.000105,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,-0.504017,-0.258351,1.230672,0.370698,-1.050595,0.455294,-0.076337,0.004497,0.110583,-1.140318,-0.276769,1.326154,-0.485893,-0.023229,0.030509,-0.003253,0.280522,0.038524,-0.001517,-0.019376,0.021795,-0.009124,0.001682,-0.000115,-0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,0.350814,0.902702,-0.868152,-1.104835,1.176956,-0.371210,0.046451,-0.001870,-0.383360,0.837707,0.929134,-1.151584,0.142727,0.117905,-0.035851,0.002804,0.420385,0.037325,-0.001635,-0.021711,0.025916,-0.011212,0.002101,-0.000144,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000,0.000000,-0.000000],
[4.200000,-0.078281,-1.226482,0.241546,1.647455,-1.242652,0.347122,-0.041685,0.001746,0.567450,0.056101,-1.500073,-0.539457,1.797675,-0.913592,0.181273,-0.012797,0.556822,0.040816,0.006547,-0.022889,0.015628,-0.004142,0.000423,-0.000010,0.000000,-0.000000,0.000000,-0.000000,-0.000000,-0.000000,0.000000,-0.000000
]]



seq_args_ = {
    URI1: [1,figure8_1],
    URI2: [2,figure8_2],
   # URI3: [3,figure8_3],
   # URI4: [sequence4],
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
    #URI3,
   # URI4,
   # URI5,
   # URI6,
   # URI7,
   # URI8,
   # URI9,
   # URI10
}

#######
def activate_mellinger_controller(cf):
    cf.param.set_value('stabilizer.controller', '2')


def upload_trajectory(cf, trajectory_id, trajectory):
    try:
        print('hello')
        trajectory_mem = cf.cf.mem.get_mems(MemoryElement.TYPE_TRAJ)[0]
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

        upload_result = trajectory_mem.write_data_sync()
        print('Uploaded')
        if not upload_result:
            print('Upload failed, aborting!')
            sys.exit(1)
        cf.cf.high_level_commander.define_trajectory(trajectory_id, 0, len(trajectory_mem.trajectory))
        print(total_duration)
        return total_duration
    except Exception as e:
        print(e)

#####
def activate_led_bit_mask(scf):
    scf.cf.param.set_value('led.bitmask', 255)

def deactivate_led_bit_mask(scf):
    scf.cf.param.set_value('led.bitmask', 0)

def light_check(scf):
    activate_led_bit_mask(scf)
    time.sleep(2)
    deactivate_led_bit_mask(scf)

def wait_for_param_download(scf):
    while not scf.cf.param.is_updated:
        time.sleep(1.0)
    print('Parameters downloaded for', scf.cf.link_uri)


def arm(scf):
    scf.cf.platform.send_arming_request(True)
    time.sleep(1.0)


def take_off(cf, position):
    take_off_time = 1.0
    sleep_time = 0.1
    steps = int(take_off_time / sleep_time)
    vz = position[2] / take_off_time

    print(vz)

    for i in range(steps):
        cf.commander.send_velocity_world_setpoint(0, 0, vz, 0)
        time.sleep(sleep_time)


def land(cf, position):
    landing_time = 1.0
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
        cf=scf.cf

        take_off(scf, sequence[0])
        for position in sequence:
            print('Setting position {}'.format(position))
            end_time = time.time() + position[3]
            while time.time() < end_time:
                cf.commander.send_position_setpoint(position[0],
                                                    position[1],
                                                    position[2], 0)
                time.sleep(0.1)
        land(scf, sequence[-1])
    except Exception as e:
        print(e)

def run_sequencee(scf, trajectory_id,figure8):
    try:
        print('run function')
        commander = scf.cf.high_level_commander
        relative_yaw=False
        print('second print')
        duration=21
        #duration = upload_trajectory(cf, trajectory_id, figure8)
        print(duration)
        print('The sequence is {:.1f} seconds long'.format(duration))
        # Arm the Crazyflie
        #cf.platform.send_arming_request(True)
        print('third print')
        time.sleep(1.0)

        takeoff_yaw = 3.14 / 2 if relative_yaw else 0.0
        commander.takeoff(0.5, 2.0, yaw=takeoff_yaw)
        time.sleep(3.0)
        commander.start_trajectory(trajectory_id, 1.0, True)
        time.sleep(duration)
        commander.land(0.0, 2.0)
        time.sleep(2)
        commander.stop()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    cflib.crtp.init_drivers()

    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        try:
            # If the copters are started in their correct positions this is
            # probably not needed. The Kalman filter will have time to converge
            # any way since it takes a while to start them all up and connect. We
            # keep the code here to illustrate how to do it.
            

            # The current values of all parameters are downloaded as a part of the
            # connections sequence. Since we have 10 copters this is clogging up
            # communication and we have to wait for it to finish before we start
            # flying.
            swarm.parallel_safe(light_check)

            durat=swarm.parallel_safe(upload_trajectory,args_dict=seq_args_)
            
            print(durat)
            #swarm.parallel(wait_for_param_download)
            time.sleep(5)

            swarm.reset_estimators()
        
        

            swarm.parallel_safe(activate_mellinger_controller)
            
            
        
            
            
            swarm.parallel_safe(arm)
            #swarm.parallel(run_sequence,args_dict=seq_args_)
            swarm.parallel_safe(run_sequencee,args_dict=seq_args_)

        # swarm.parallel(run_sequence, args_dict=seq_args)
        except Exception as e:
                print(f"Error occurred: {e}")
                swarm.parallel_safe(emergency_land)

