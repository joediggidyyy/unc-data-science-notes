# Secure SSH Access Guide

**Objective:** Establish a secure, encrypted command channel between the Windows Workstation and the Ubuntu Edge Router.

## 1. Enable SSH on Ubuntu (Edge Router)

If you haven't already, run the helper script on the Ubuntu machine:

```bash
cd services/network_router/deployment/ubuntu_2404
chmod +x enable_ssh.sh
./enable_ssh.sh
```

This will:
1.  Install `openssh-server`.
2.  Open Port 22 in the firewall.
3.  Display your IP address.

## 2. Connect from Windows

Open your PowerShell terminal in VS Code and run:

```powershell
ssh <ubuntu_username>@<ubuntu_ip_address>
# Example: ssh joediggidyyy@192.168.68.62
```

## 3. SEAM-Tight Security: SSH Keys (Recommended)

To avoid typing passwords and prevent brute-force attacks, use SSH Keys.

### Step A: Generate Key Pair (On Windows)
Run this in PowerShell:
```powershell
ssh-keygen -t ed25519 -C "oracl_admin@windows"
# Press Enter to accept defaults
```

### Step B: Copy Key to Ubuntu
Since Windows doesn't have `ssh-copy-id` by default, use this command (replace user/IP):

```powershell
type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh <ubuntu_user>@<ubuntu_ip> "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Step C: Disable Password Login (On Ubuntu)
**WARNING:** Only do this AFTER confirming key-based login works.

Edit the SSH config:
```bash
sudo nano /etc/ssh/sshd_config
```
Find and change these lines:
```text
PasswordAuthentication no
PermitRootLogin no
```
Restart SSH:
```bash
sudo systemctl restart ssh
```

## 4. Running Remote Diagnostics
Once connected, you can run hardware checks directly:

```bash
lsusb
dmesg | grep usb
```
