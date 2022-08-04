# ft_otp / TOTP Generator

Python implementation of an authenticator, similar to Google authenticator.

<br>

### Before anything

The makefile have many commands to interact and control the pprogram and its container.
With this command you can see all the avaible commands.

````bash
make help
````

## Start
Build the image for docker. This is necessary one single time.

````bash
make build
````



## Run program

Then we can create, run and execute the necessary container running:

````bash
make
````

After this we are in the root directory of a debian container. To find and run 
main program:

````bash
cd home
./totp_gen.py -rg "My super secret master secret key"
````

...

