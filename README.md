# WiFi Penetration Testing Automation Tool

This project contains two scripts to automate the process of performing penetration testing on WiFi networks (WPA and WEP). The scripts are designed for educational and authorized testing purposes only. Unauthorized use is illegal and unethical.

## Prerequisites

- Kali Linux (or a similar penetration testing distribution)
- Installed tools: `xdotool`, `aircrack-ng`, `airodump-ng`, `aireplay-ng`, `airmon-ng`
- Root privileges (required for most operations)
- A compatible wireless adapter (supports monitor mode)

## Scripts

1. **WPA Hack (`wpa_hack.cpp`)**  
    Automates the process of capturing a WPA handshake and performing a deauthentication attack.
2. **WEP Hack (`wep_hack.cpp`)**  
    Automates the process of cracking a WEP-encrypted network.

---

## Usage

### WPA Hack

#### Compilation

bash g++ wpa_hack.cpp -o wpa_hack -lstdc++

#### Execution

bash ./wpa_hack

#### Arguments (Hardcoded in the Script)

- `bssid`: Replace `(bssid)` in the script with the target AP's BSSID (MAC address).
- `channel`: Replace `(2)` with the target AP's channel.
- `output_file`: Replace `(hack1)` with the desired filename for the captured handshake.

#### Steps Automated:

1. Opens a terminal and escalates to root.
2. Enables monitor mode on `wlan0`.
3. Performs a deauthentication attack on the target AP.
4. Captures the WPA handshake.
5. Scans for nearby WiFi networks.

---

### WEP Hack

#### Compilation

bash g++ wep_hack.cpp -o wep_hack -lstdc++

#### Execution

bash ./wep_hack

#### Arguments (Hardcoded in the Script)

- `bssid`: Replace `(bssid)` with the target AP's BSSID.
- `channel`: Replace `(2)` with the target AP's channel.
- `output_file`: Replace `./wep.cap` with the desired filename for the captured packets.

#### Steps Automated:

1. Opens a terminal and escalates to root.
2. Enables monitor mode on `wlan0`.
3. Captures packets from the target WEP network.
4. Uses `besside-ng` to automate the cracking process.
5. Scans for nearby WEP-encrypted networks.

---

## Ethical Considerations

- **Authorization**: Use these scripts only on networks you own or have explicit permission to test.
- **Legal Compliance**: Unauthorized access to computer networks is illegal in most jurisdictions.
- **Educational Purpose**: This project is intended for learning and ethical hacking practices.

## Disclaimer

The author is not responsible for any misuse of this tool. Always ensure you have proper authorization before performing any penetration testing activities.

---

## Contributing

Feel free to fork this project and submit pull requests for improvements or additional features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
