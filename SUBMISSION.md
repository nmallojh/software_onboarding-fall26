# Submission — HRC Software Onboarding Fall 2026

**Name:**
**Discord handle:**
**Repository:**
**Date:**

---

## Stage checklist

- [ ] **Stage 0** — Setup. `scripts/check_setup.py` exits 0.
- [ ] **Stage 1** — MuJoCo + PD controller. Tests green.
- [ ] **Stage 2** — JAX exercises. Tests green.
- [ ] **Stage 3** — MJX environment. Tests green.
- [x] **Stage 4** — Brax PPO. Trained a policy, exported it, `NumpyPolicy` matches.
- [ ] **Stage 5** — ROS 2 sim2sim. Smoke test green, teleop GIF recorded.

## `scripts/progress.py` output

<details>
<summary>paste the full output here</summary>

```
$ uv run python scripts/progress.py --slow

(paste)
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
(paste results/eval_sim2sim.json)
```

Measured `/pup/joint_command` rate from `ros2 topic hz`:

## Escape hatches used

- [ ] I used `checkpoints/pup_joystick_flat_reference.npz` for Stage 5 instead
      of my own policy.
- [ ] Other (describe):

*(Using one is fine. Not declaring one is not.)*

## Reflection — Stage 5

**List two ways sim2sim can pass while real hardware still fails, and what you
would add to the sim node to catch each.**

>

## What was hardest?

One paragraph. This is will help us improve onboarding.

>

## Time spent

| Stage | Hours |
|---|---|
| 0 Setup | |
| 1 MuJoCo + PD | |
| 2 JAX | |
| 3 MJX env | |
| 4 Brax + export | |
| 5 ROS 2 | |
| **Total** | |

---

**Then DM the software lead (Henry Tsay) on Discord or show during a meeting.**
