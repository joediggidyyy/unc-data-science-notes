# Connecting to SEAMEdge-AP Secure Network

**Quick Reference Guide for Administrators**

---

## Connection Information

| Setting | Value |
|---------|-------|
| **SSID** | SEAMEdge-AP |
| **Security** | WPA2-Personal |
| **Password** | <REDACTED_SEAMEDGE_AP_PSK> |
| **Network** | <REDACTED_IPV4>/24 |
| **Gateway** | <REDACTED_IPV4> |
| **DNS** | <REDACTED_IPV4>, <REDACTED_IPV4> |
| **IP Assignment** | **Static** (DHCP disabled) |

---

## Windows Connection

### Step 1: Connect to WiFi
1. Click WiFi icon in system tray
2. Select **SEAMEdge-AP**
3. Click **Connect**
4. Enter password: `<REDACTED_SEAMEDGE_AP_PSK>`
5. Click **Next**

**Note**: Windows will show "No internet, secured" - this is expected. Proceed to Step 2.

### Step 2: Configure Static IP

Open PowerShell **as Administrator** and run:

```powershell
# Set static IP (replace XX with your assigned number)
netsh interface ip set address "Wi-Fi" static 192.168.10.XX <REDACTED_IPV4> <REDACTED_IPV4>

# Set DNS
netsh interface ip set dns "Wi-Fi" static <REDACTED_IPV4>
netsh interface ip add dns "Wi-Fi" <REDACTED_IPV4> index=2
```

**Common Assignments**:
- Admin workstation: `<REDACTED_IPV4>`
- Check [Static IP Allocation](../operations/SECURE_SUBNET_STATIC_IP_ALLOCATION.md) for available addresses

### Step 3: Verify Connection

```powershell
# Check IP configuration
ipconfig

# Test gateway connectivity (ICMP disabled, try SSH)
ssh oracode@<REDACTED_IPV4>
# Password: (from CIDS vault)

# Test internet (if routing enabled)
ping <REDACTED_IPV4>
```

### Troubleshooting Windows
- **"No internet" notification**: Normal - static IP doesn't auto-detect internet
- **Cannot ping gateway**: Try SSH instead (ICMP disabled per SEAM policy)
- **WiFi keeps disconnecting**: Forget network and reconnect from scratch
- **Wrong IP shown**: Rerun netsh commands, verify interface name is "Wi-Fi"

---

## Linux Connection (NetworkManager)

### One-Command Setup

```bash
# Create and configure connection
sudo nmcli con add type wifi ifname wlp4s0 con-name SEAMEdge-AP ssid SEAMEdge-AP
sudo nmcli con mod SEAMEdge-AP ipv4.method manual
sudo nmcli con mod SEAMEdge-AP ipv4.addresses 192.168.10.XX/24
sudo nmcli con mod SEAMEdge-AP ipv4.gateway <REDACTED_IPV4>
sudo nmcli con mod SEAMEdge-AP ipv4.dns "<REDACTED_IPV4> <REDACTED_IPV4>"
sudo nmcli con mod SEAMEdge-AP wifi-sec.key-mgmt wpa-psk
sudo nmcli con mod SEAMEdge-AP wifi-sec.psk "<REDACTED_SEAMEDGE_AP_PSK>"
sudo nmcli con up SEAMEdge-AP
```

**Replace**:
- `wlp4s0` with your WiFi interface name (check `ip link`)
- `XX` with your assigned IP number

### Verify Connection

```bash
# Check IP
ip addr show wlp4s0 | grep inet

# Test gateway
ssh oracode@<REDACTED_IPV4>

# Check routing
ip route
```

### Troubleshooting Linux
- **"No IP assigned"**: Check NetworkManager managing interface: `nmcli device status`
- **Connection timeout**: Check hostapd logs on Edge: `ssh oracode@<REDACTED_IPV4> "sudo journalctl -u hostapd -f"`
- **Interface name wrong**: List interfaces: `ip link show | grep wl`

---

## Linux Connection (Manual - BRAIN Node)

For systems without NetworkManager (minimal installs, embedded systems):

### Create wpa_supplicant config

```bash
# /etc/wpa_supplicant/wpa_supplicant-wlp4s0.conf
sudo tee /etc/wpa_supplicant/wpa_supplicant-wlp4s0.conf << 'EOF'
ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=wheel
update_config=1

network={
    ssid="SEAMEdge-AP"
    psk="<REDACTED_SEAMEDGE_AP_PSK>"
    key_mgmt=WPA-PSK
}
EOF

sudo chmod 600 /etc/wpa_supplicant/wpa_supplicant-wlp4s0.conf
```

### Create systemd-networkd config

```bash
# /etc/systemd/network/10-wlp4s0.network
sudo tee /etc/systemd/network/10-wlp4s0.network << 'EOF'
[Match]
Name=wlp4s0

[Network]
Address=<REDACTED_IPV4>/24
Gateway=<REDACTED_IPV4>
DNS=<REDACTED_IPV4>
DNS=<REDACTED_IPV4>
EOF
```

### Enable services

```bash
# Enable wpa_supplicant for interface
sudo systemctl enable wpa_supplicant@wlp4s0
sudo systemctl start wpa_supplicant@wlp4s0

# Enable systemd-networkd
sudo systemctl enable systemd-networkd
sudo systemctl start systemd-networkd

# Check status
sudo systemctl status wpa_supplicant@wlp4s0
sudo systemctl status systemd-networkd
```

---

## macOS Connection

### Step 1: Connect to WiFi
1. Click WiFi icon in menu bar
2. Select **SEAMEdge-AP**
3. Enter password: `<REDACTED_SEAMEDGE_AP_PSK>`
4. Click **Join**

### Step 2: Configure Static IP
1. System Preferences → Network
2. Select **Wi-Fi** in left panel
3. Click **Advanced...**
4. Go to **TCP/IP** tab
5. Configure IPv4: **Manually**
6. IPv4 Address: `192.168.10.XX`
7. Subnet Mask: `<REDACTED_IPV4>`
8. Router: `<REDACTED_IPV4>`
9. Go to **DNS** tab
10. Add DNS: `<REDACTED_IPV4>` and `<REDACTED_IPV4>`
11. Click **OK** then **Apply**

### Step 3: Verify
```bash
# Check IP
ifconfig en0

# Test connectivity
ssh oracode@<REDACTED_IPV4>
```

---

## Android/iOS (Mobile Devices)

### Android
1. Settings → Wi-Fi
2. Select **SEAMEdge-AP**
3. Enter password
4. Tap **Advanced options**
5. IP settings: **Static**
6. IP address: `192.168.10.XX`
7. Gateway: `<REDACTED_IPV4>`
8. Network prefix length: `24`
9. DNS 1: `<REDACTED_IPV4>`
10. DNS 2: `<REDACTED_IPV4>`
11. Tap **Connect**

### iOS
1. Settings → Wi-Fi
2. Select **SEAMEdge-AP**
3. Enter password
4. Tap **(i)** icon next to network name
5. Configure IP: **Manual**
6. IP Address: `192.168.10.XX`
7. Subnet Mask: `<REDACTED_IPV4>`
8. Router: `<REDACTED_IPV4>`
9. DNS: `<REDACTED_IPV4>, <REDACTED_IPV4>`
10. Tap **Save**

---

## Why Static IPs?

**Technical Reason**: The Edge node's WiFi adapter (RTL8852BE) has a firmware issue that prevents DHCP broadcast frames from reaching the DHCP server. Static IPs bypass this limitation.

**See**: [Incident Report - DHCP Broadcast Failure](../reports/INCIDENT_2025-12-12_DHCP_BROADCAST_FAILURE.md)

**Status**: Permanent solution for prototype phase. Hardware upgrade planned for production.

---

## IP Address Assignment

**Before connecting**, check available IPs:
1. See [Static IP Allocation Table](../operations/SECURE_SUBNET_STATIC_IP_ALLOCATION.md)
2. Pick an available address from your device category:
   - Admin workstations: .50-.69
   - Client devices: .70-.99
3. Update the allocation table after connecting (git commit)

**Common Assignments**:
- `<REDACTED_IPV4>` - Edge gateway (reserved)
- `<REDACTED_IPV4>` - BRAIN node (reserved)
- `<REDACTED_IPV4>` - Primary admin workstation
- `<REDACTED_IPV4>+` - Available

---

## Security Notes

- **Password Rotation**: WiFi password changed quarterly
- **Access Control**: MAC filtering not enabled (static IPs provide tracking)
- **Encryption**: WPA2-PSK (WPA3 fallback configured)
- **Firewall**: Edge node filters all inbound traffic except SSH, dashboard, DNS
- **Monitoring**: Connection attempts logged in hostapd journal

---

## Support

**Connection Issues**:
1. Check [Troubleshooting](#troubleshooting-windows) section above
2. Verify Edge node status from parent network: `ssh oracode@<REDACTED_IPV4>`
3. Check hostapd service: `sudo systemctl status hostapd`
4. Review logs: `sudo journalctl -u hostapd -f`

**Documentation**:
- [Static IP Allocation](../operations/SECURE_SUBNET_STATIC_IP_ALLOCATION.md)
- [CIDS Network Architecture](../architecture/CIDS_NETWORK_ARCHITECTURE.md)
- [Incident Reports](../reports/)

---

**Last Updated**: 2025-12-12  
**Maintained By**: CIDS Network Operations
