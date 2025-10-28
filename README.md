# gem5 Hello World Simulation

This repository contains the setup, build, and execution steps for running a simple “Hello, World” program using the gem5 simulator.

---

## Files
- `hello.c` – Source code for the C program.
- `hello` – Compiled static executable.
- `run_hello.py` – gem5 configuration script.

---

## Commands Used
```bash
# Build gem5 (done once)
cd ~/gem5
scons build/X86/gem5.opt -j4

# Compile the hello world binary
gcc hello.c -static -o hello

# Run the gem5 simulation
~/gem5/build/X86/gem5.opt run_hello.py

