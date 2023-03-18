# Rotations for Robotics
This repo contains the plots that serve as visualizations for my blog series on rotations for robotics.

## Setup
### MAC OS
1. Run the following commands to install the dependencies for this repo:
    ```bash
    brew install py3cairo ffmpeg pango scipy pkg-config
    brew install --cask mactex-no-gui
    python3 -m venv rot-env
    source rot-env/bin/activate
    pip3 install --no-cache-dir --upgrade pip
    pip3 install -r requirements.txt
    ```
2. In order to use Latex, I also had to add the following to my `.bashrc`
    ```
    export PATH="$PATH:/usr/local/texlive/2022/bin/universal-darwin"
    ```

This repo uses manim. For MAC install instructions, see [Manim Install - MAC](https://docs.manim.community/en/stable/installation/macos.html).

### Linux
[Manim Install - Linux](https://docs.manim.community/en/stable/installation/linux.html)
### Windows
Get a different OS.

## Usage
Generate plots for Quaternions for Robotics
```bash
# QuatDefinition.png
manim -qh src/quat_anim.py QuatDefinition

# ActiveTransformation
manim -qh src/quat_anim.py ActiveTransformation

# PassiveTransformation
manim -qh src/quat_anim.py PassiveTransformation

# QuatConj
manim -qh src/quat_anim.py QuatConj

# FramesAB
manim -qh src/quat_anim.py FramesAB

# VecB
manim -qh src/quat_anim.py VecB
```

Note that the following sets of flags may be used instead:
- `-ql` generate a low quality render (faster)
- `-pql` generate a low quality render and play it (open it) immediately


## Manim Resources
- [Example gallery](https://docs.manim.community/en/stable/examples.html)
- [Manim tutorials](https://docs.manim.community/en/stable/tutorials/index.html)