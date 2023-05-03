# Setting up PHP Server

Setting up a php server for running php files without XAMPP.

## Step 1

- First we have to install PHP, so go to the following site and download the php zip file.

[Download PHP](https://windows.php.net/downloads/releases/php-8.2.3-Win32-vs16-x64.zip)

- Now open make a folder named `phpwebserver` and extract all the contents of the zip file inside it. Now move that folder to C drive.
- Now press start and search `Edit System Environment Variables` the click `Environmental Variables`, now in System Variables, select path and add new path mentioned below.

```bash
C:\phpwebserver
```

Now download the file [`php.ini`](https://raw.githubusercontent.com/Nitesh-13/WT-Assignments/main/Assignment%207/php.ini) and copy and paste it inside the phpwebserver folder.

## Step 2

- Open VSCode and in extensions panel search `@builtin php`.
- Now select the `PHP Language Features` and click disable.
- Now Search and Install two extensions :
  - PHP Intelephense
  - PHP Server

## Step 3

Open any php file and right click and press `PHP Server: serve project` to start the server and to stop the server just do right click and press `PHP Server: serve project`.

After server has started, you can view your application at `http://localhost:3000/`
