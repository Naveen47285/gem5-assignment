# gem5 Hello World Simulation

This repository contains my Week 3 Assignment for **MSCS-531: Exploring Memory Hierarchy Design in gem5.**

---

## 🧠 Overview
This project demonstrates a simple x86 "Hello World" program executed in the **gem5** simulator to analyze memory hierarchy, cache configurations, and virtual memory design.  
The experiment validates CPU–memory interaction and helps understand cache performance in system architecture.

---

## ⚙️ Setup Instructions

### 1️⃣ Build gem5
```bash
cd ~/gem5
scons build/X86/gem5.opt -j4
