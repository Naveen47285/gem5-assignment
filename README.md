# gem5 Hello World Simulation

**Student:** Naveen Nallani  
**Course:** Computer Architecture  
**Date:** October 28, 2025  

This project demonstrates running a simple “Hello, World!” program using the gem5 simulator with the X86 CPU model in syscall emulation (SE) mode.

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

