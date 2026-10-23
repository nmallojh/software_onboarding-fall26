"""Show that MuJoCo's built-in position actuator is the same as my PD controller."""

import mujoco 
import numpy as np 
from pup.envs.constants import MJX_SCENE 
from pup.sim.pd import PDController, joint_state 
from pup.sim.viewer import load_scene 

model, data = load_scene(MJX_SCENE)
q, qd = joint_state(model, data)

target = q + 0.5 
data.ctrl[:] = target 

mujoco.mj_forward(model, data)
mujoco_torques = data.actuator_force

my_controller = PDController(25, 0.5)
my_torques = my_controller(q, qd, target)

print("Biggest difference:", np.max(np.abs(mujoco_torques - my_torques)))