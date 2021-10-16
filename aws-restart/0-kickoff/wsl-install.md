# Install WSL2
1. `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
2. Yes to restart
3. Enable Windows virtualization features
    * Hyper-V
    * Virtual Machine Platform
    * Windows Hypervisor Platform
4. Install Ubuntu from the Microsoft Store



# VMWare

VMWare automatically configures NAT. In VirtualBox, you need to manually edit `/etc/dhcpcd.conf` file.

Turn off ICMP as DDoS prevention
