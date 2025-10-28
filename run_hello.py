from m5.objects import System, SrcClockDomain, VoltageDomain, TimingSimpleCPU, MemCtrl, DDR3_1600_8x8, AddrRange, SystemXBar, Root, Process, SEWorkload
import m5

# Create the system
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()

# Memory configuration
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]

# CPU and bus setup

# CPU and bus setup
system.cpu = TimingSimpleCPU()
system.membus = SystemXBar()

# Connect CPU ports
system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.dcache_port = system.membus.cpu_side_ports

# Create and connect interrupt controller (required for X86 CPUs)
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

# Connect memory
system.mem_ctrl.port = system.membus.mem_side_ports


# ---- Workload setup ----
binary_path = '/home/naveen/gem5/hello'
system.workload = SEWorkload.init_compatible(binary_path)

process = Process()
process.executable = binary_path
process.cmd = [binary_path]
process.cwd = '/home/naveen/gem5'

system.cpu.workload = process
system.cpu.createThreads()

# Root and simulation
root = Root(full_system=False, system=system)
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()
print("Exiting @ tick {} because {}".format(m5.curTick(), exit_event.getCause()))

