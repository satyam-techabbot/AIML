# **Deploy a FastAPI App**

## **Deploying FastAPI on Apache Server**

> To deploy a FastAPI application on an Apache server, you must configure Apache as a Reverse Proxy.

> Because FastAPI is an asynchronous ASGI framework, Apache cannot run it directly via traditional methods like . Instead, an ASGI server like Uvicorn runs the application locally, while Apache intercepts public requests and forwards them to Uvicorn.


1. **Enable Apache Proxy Modules** 
    
    You must first enable the necessary proxy modules so Apache can route network traffic to your ASGI server. Run the following commands on your Linux server: 

    ```bash
    sudo a2enmod proxy
    sudo a2enmod proxy_http
    sudo a2enmod headers
    sudo systemctl restart apache2
    ```

2. **Create a Systemd Service for Uvicorn**

    To keep your app running in the background, set up systemd to manage Uvicorn. 

    1. Create a service file () with appropriate user, directory, and  command paths. 
    2. Ensure you use the  flag for proper header handling from Apache. 
    3. Start and enable the service: 
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start fastapi.service
    sudo systemctl enable fastapi.service
    ```

3. **Configure Apache as a Reverse Proxy**

    Modify your Apache virtual host file to route traffic to the  port where Uvicorn is listening. 

    1. Edit your config file (e.g., ) to include  and  directives pointing to the local Uvicorn instance. 
    2. Enable the site and reload Apache:
    ```bash
    sudo a2ensite fastapi.conf
    sudo systemctl reload apache2
    ```

Your FastAPI application is now live behind Apache.

--- 

## 






