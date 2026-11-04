# Submission — HRC Software Onboarding Fall 2026

**Name:** Niveditha Mallojhala
**Discord handle:** nivedithaa
**Repository:** https://github.com/nmallojh/software_onboarding-fall26
**Date:** 11/4/26

---

## Stage checklist

- [x] **Stage 0** — Setup. `scripts/check_setup.py` exits 0.
- [x] **Stage 1** — MuJoCo + PD controller. Tests green.
- [x] **Stage 2** — JAX exercises. Tests green.
- [x] **Stage 3** — MJX environment. Tests green.
- [x] **Stage 4** — Brax PPO. Trained a policy, exported it, `NumpyPolicy` matches.
- [x] **Stage 5** — ROS 2 sim2sim. Smoke test green, teleop GIF recorded.

## `scripts/progress.py` output

<details>
<summary>paste the full output here</summary>

```
$ uv run python scripts/progress.py --slow

Pup onboarding progress
  ✓ PASSED        Stage 1  MuJoCo + PD controller    12 passed, 0 failed, 0 not started, 0 skipped
  ✓ PASSED        Stage 2  JAX for robotics          9 passed, 0 failed, 0 not started, 0 skipped
  ✓ PASSED        Stage 3  MJX environment           11 passed, 0 failed, 0 not started, 0 skipped
  ✓ PASSED        Stage 4  Brax PPO + export         4 passed, 0 failed, 0 not started, 0 skipped
36 passed, 1 skipped, 2 deselected, 2 warnings in 82.58s (0:01:22)

==============================================================================
PUP ONBOARDING PROGRESS
==============================================================================
✓ PASSED         Stage 1  MuJoCo + PD controller    12 passing
✓ PASSED         Stage 2  JAX for robotics          9 passing
✓ PASSED         Stage 3  MJX environment           11 passing
✓ PASSED         Stage 4  Brax PPO + export         4 passing
◻ CONTAINER      Stage 5  ROS 2 sim2sim             run tests/test_05_ros2_smoke.sh inside docker/ros2
==============================================================================
Every TODO(student) block is written. Nice.
```

</details>

## Stage 4 — training results

**Config used:** `full` &nbsp; **Seed:** 0 &nbsp;
**Where it ran:** Colab T4 &nbsp; **Wall-clock:** ~49 min training

Learning curve: `results/learning_curve.png`
Rollout GIF: `results/training.gif`

```json
{
  "seed": 0,
  "n_episodes": 5,
  "commands": [
    {
      "command": [
        0.5,
        0.0,
        0.0
      ],
      "mean_abs_error": [
        0.057255939897149805,
        0.04121690370196011,
        0.0708523904178699
      ],
      "mean_abs_vy": 0.041216906160116196,
      "mean_speed": 0.5407724380493164,
      "fall_rate": 0.0,
      "mean_episode_length": 1000.0
    },
    {
      "command": [
        1.0,
        0.0,
        0.0
      ],
      "mean_abs_error": [
        0.06501190906763077,
        0.04590879792730557,
        0.07169826642905246
      ],
      "mean_abs_vy": 0.04590879753232002,
      "mean_speed": 1.0215985774993896,
      "fall_rate": 0.0,
      "mean_episode_length": 1000.0
    },
    {
      "command": [
        0.0,
        0.5,
        0.0
      ],
      "mean_abs_error": [
        0.06150038498499198,
        0.055472361747920515,
        0.06228863975853892
      ],
      "mean_abs_vy": 0.457852840423584,
      "mean_speed": 0.4636211395263672,
      "fall_rate": 0.0,
      "mean_episode_length": 1000.0
    },
    {
      "command": [
        0.0,
        0.0,
        1.0
      ],
      "mean_abs_error": [
        0.04825401777239022,
        0.037225472452641406,
        0.07024535683393478
      ],
      "mean_abs_vy": 0.03722546994686127,
      "mean_speed": 0.06643342226743698,
      "fall_rate": 0.0,
      "mean_episode_length": 1000.0
    },
    {
      "command": [
        0.0,
        0.0,
        0.0
      ],
      "mean_abs_error": [
        0.04132749001916527,
        0.038819018652870727,
        0.08807292674673227
      ],
      "mean_abs_vy": 0.03881901875138283,
      "mean_speed": 0.06308122724294662,
      "fall_rate": 0.0,
      "mean_episode_length": 1000.0
    }
  ],
  "walking_passes": true
}
```

Did it meet the acceptance criteria (`"walking_passes": true`)?
Yes, `walking_passes: true`. Forward 1.0 m/s: 1.02 m/s with 0 falls. Turn 1.0 rad/s: error 0.07. Stand still: 0.06 m/s. All episodes ran the full 1000 steps.

## Stage 5 — sim2sim results

Teleop GIF: `results/sim2sim_teleop.gif`

```json
{
  "duration_s": 20.0,
  "min_trunk_height": 0.29093991224488114,
  "fell": false,
  "commands": [
    {
      "command": [0.5, 0.0, 0.0],
      "n_samples": 151,
      "mean_velocity": [0.38479376129890286, 0.0106937827024374, -2.4290995011487333e-05],
      "mean_abs_error": [0.11520623870109714, 0.0106937827024374, 2.4290995011487333e-05],
      "mean_speed": 0.3850314944375795,
      "threshold": 0.25,
      "passed": true
    },
    {
      "command": [1.0, 0.0, 0.0],
      "n_samples": 150,
      "mean_velocity": [0.9571918583430238, -0.004541143192763933, -0.004551534701725785],
      "mean_abs_error": [0.04280814165697622, 0.004541143192763933, 0.004551534701725785],
      "mean_speed": 0.9575321052512068
    },
    {
      "command": [0.0, 0.0, 1.0],
      "n_samples": 150,
      "mean_velocity": [-0.09118876190059248, 0.07304885236797051, 0.9924880609558194],
      "mean_abs_error": [0.09118876190059248, 0.07304885236797051, 0.007511939044180571],
      "mean_speed": 0.11869546617108592
    },
    {
      "command": [0.0, 0.0, 0.0],
      "n_samples": 150,
      "mean_velocity": [-0.001134103018101549, -3.926425226513982e-05, 0.000648867990458022],
      "mean_abs_error": [0.001134103018101549, 3.926425226513982e-05, 0.000648867990458022],
      "mean_speed": 0.002677799633654086
    }
  ],
  "passed": true
}
```

Measured `/pup/joint_command` rate from `ros2 topic hz`: ~50.0 Hz (average rate 50.006)

Sim2sim gap: At a 0.5 m/s command, the reference policy walked 0.385 m/s through ROS, but the doc reports it reaches 0.52 m/s in MJX (my own policy reached 0.54 m/s in MJX in Stage 4). The same policy gets a different result because the two simulators handle ground contact and motor control differently.

## Escape hatches used

- [x] I used `checkpoints/pup_joystick_flat_reference.npz` for Stage 5 instead
      of my own policy.
- [ ] Other (describe):

*(Using one is fine. Not declaring one is not.)*

## Reflection — Stage 5

**List two ways sim2sim can pass while real hardware still fails, and what you
would add to the sim node to catch each.**

> 1. Motor delay: the sim applies commands instantly, but real motors lag about 5–15 ms. I'd add a short delay to commands in sim_node.
> 2. IMU errors: the sim gives perfect IMU readings, but a real IMU drifts and has noise. I'd add drift and noise to the IMU data sim_node publishes.

## What was hardest?

> The hardest part was understanding what was actually going on, not just writing the code. Things like what kernels and biases are, why the observation needs to be normalized, and why the policy has to be exported to numpy for the robot took me a while to get. Once I understood the big picture, the TODOs made a lot more sense.

## Time spent

| Stage | Hours |
|---|---|
| 0 Setup | 0.5 |
| 1 MuJoCo + PD | 3 |
| 2 JAX | 4 |
| 3 MJX env | 7 |
| 4 Brax + export | 3 |
| 5 ROS 2 | 3 |
| **Total** | 20.5 |

---

**Then DM the software lead (Henry Tsay) on Discord or show during a meeting.**
