# Introduction
This guide will help you to guide to install VM VirtualBox

### Step 1: Install Oracle VirtualBox
1. **Download VirtualBox:**
   - Go to the [official VirtualBox website](https://www.virtualbox.org/).
   - Click on the "Downloads" link in the top navigation menu.

2. **Choose the Correct Package:**
   - Select the appropriate package for your OS (Windows, macOS, or Linux).

3. **Install VirtualBox:**
   - **For Windows:**
     - Download the installer for Windows and double-click on the downloaded file.
     - Follow the on-screen instructions and accept the license agreement.
     - Choose the components and installation path.
     - Complete the installation process.
   - **For macOS:**
     - Download the macOS version of VirtualBox.
     - Double-click on the downloaded DMG file.
     - Double-click on the VirtualBox package icon and follow the on-screen instructions.
   - **For Linux:**
     - Download the appropriate package for your Linux distribution.
     - For example, for Ubuntu, use the following command:
       ```bash
       sudo dpkg -i <VirtualBox_package_name>.deb
       ```
     - Install additional dependencies if prompted.

4. **Post-installation Configuration:**
   - Add your user account to the "vboxusers" group (Linux) or "VirtualBox Users" group (Windows) to grant permissions to manage VMs.

5. **Launch VirtualBox:**
   - Open VirtualBox from your application menu (Windows and Linux) or from the Applications folder (macOS).

### Step 2: Download and Configure Ubuntu 22.04 in VirtualBox
1. **Download Ubuntu 22.04 Image:**
   - Visit [OSBoxes](https://www.osboxes.org/ubuntu/) and download the Ubuntu 22.04 image.

2. **Import Ubuntu Image into VirtualBox:**
   - Open VirtualBox.
   - Click on "New" to create a new virtual machine.
   - Name your VM and select "Linux" and "Ubuntu (64-bit)".
   - Allocate memory (e.g., 2048 MB) and create a virtual hard disk using the downloaded Ubuntu image.

3. **Start the VM:**
   - Select your newly created VM and click "Start".
   - Follow the on-screen instructions to set up Ubuntu.

### Step 3: Install Nginx in the Ubuntu VM
1. **Open Terminal in Ubuntu VM:**
   - Update package lists:
     ```bash
     sudo apt update
     ```
   - Install Nginx:
     ```bash
     sudo apt install nginx
     ```
   - Start Nginx:
     ```bash
     sudo systemctl start nginx
     ```
   - Enable Nginx to start at boot:
     ```bash
     sudo systemctl enable nginx
     ```

2. **Verify Nginx Installation:**
   - Open a browser in the VM and go to `http://localhost`. You should see the Nginx welcome page.

3. **Configure Firewall (if needed):**
   - Allow HTTP traffic:
     ```bash
     sudo ufw allow 'Nginx HTTP'
     ```

### Step 4: Scan the Virtual Machine Using Nmap
1. **Find the IP Address of the Ubuntu VM:**
   - In the Ubuntu VM terminal, run:
     ```bash
     ip a
     ```
   - Note the IP address assigned to the VM (usually something like `192.168.x.x`).

2. **Install Nmap on Your Host Machine:**
   - **For Windows:**
     - Download the Nmap installer from the [official website](https://nmap.org/download.html) and follow the installation instructions.
   - **For macOS:**
     - Use Homebrew to install Nmap:
       ```bash
       brew install nmap
       ```
   - **For Linux:**
     - Use the package manager to install Nmap:
       ```bash
       sudo apt install nmap
       ```

3. **Scan the Ubuntu VM Using Nmap:**
   - Open a terminal on your host machine and run:
     ```bash
     nmap <Ubuntu_VM_IP_address>
     ```
   - For a more detailed scan:
     ```bash
     nmap -A <Ubuntu_VM_IP_address>
     ```

This process will check the status of open ports and services running on your Ubuntu VM. You should see that port 80 (HTTP) is open and Nginx is running on it.

By following these steps, you’ll have a VM with Ubuntu 22.04 running Nginx, and you’ll be able to scan it from your host machine using Nmap.
