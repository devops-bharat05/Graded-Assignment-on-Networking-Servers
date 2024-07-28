# Graded-Assignment-on-Networking-Servers

## Introduction:
In this repository we have deployed a website on localhost using either apache2 or Nginx. Created a DNS name for this website as ‘awesomeweb’.

Here's a step-by-step guide to deploy a simple website on localhost using Apache2 and create a DNS entry for it as 'awesomeweb':

### Step 1: Install Apache2

First, ensure Apache2 is installed on your system.

**For Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install apache2
```

**For CentOS/RHEL:**
```bash
sudo yum install httpd
sudo systemctl start httpd
sudo systemctl enable httpd
```

### Step 2: Configure Apache2

Create a new directory for your website content and a simple HTML file.

```bash
sudo mkdir -p /var/www/awesomeweb
echo "<html><body><h1>Welcome to AwesomeWeb!</h1></body></html>" | sudo tee /var/www/awesomeweb/index.html
```

### Step 3: Create Virtual Host Configuration

Create a new virtual host configuration file for `awesomeweb`.

```bash
sudo nano /etc/apache2/sites-available/awesomeweb.conf
```

Add the following content to the file:

```apache
<VirtualHost *:80>
    ServerName awesomeweb
    DocumentRoot /var/www/awesomeweb
    <Directory /var/www/awesomeweb>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/awesomeweb_error.log
    CustomLog ${APACHE_LOG_DIR}/awesomeweb_access.log combined
</VirtualHost>
```

### Step 4: Enable the Virtual Host

Enable the new virtual host configuration.

```bash
sudo a2ensite awesomeweb.conf
sudo systemctl reload apache2
```

### Step 5: Configure DNS Name (Hosts File)

Add the DNS name to your `/etc/hosts` file to resolve `awesomeweb` to `localhost`.

```bash
sudo nano /etc/hosts
```

Add the following line:

```
127.0.0.1 awesomeweb
```

### Step 6: Verify the Setup

Open your web browser and go to `http://awesomeweb`. You should see your simple HTML page with the text "Welcome to AwesomeWeb!".

### Using Nginx (Optional)

If you prefer to use Nginx, follow these steps:

**For Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install nginx
```

**For CentOS/RHEL:**
```bash
sudo yum install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
```

Create a directory and a simple HTML file for your website.

```bash
sudo mkdir -p /var/www/awesomeweb
echo "<html><body><h1>Welcome to AwesomeWeb!</h1></body></html>" | sudo tee /var/www/awesomeweb/index.html
```

Create a new server block configuration file.

```bash
sudo nano /etc/nginx/sites-available/awesomeweb
```

Add the following content:

```nginx
server {
    listen 80;
    server_name awesomeweb;
    root /var/www/awesomeweb;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

Enable the configuration by creating a symbolic link.

```bash
sudo ln -s /etc/nginx/sites-available/awesomeweb /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

Edit your `/etc/hosts` file as described above and test the setup by visiting `http://awesomeweb`.

With these steps, you have successfully deployed a simple website on your localhost using Apache2 or Nginx and created a DNS name for it as 'awesomeweb'.
