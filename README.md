## ft_otp / TOTP Generator

Python implementation of an authenticator.

#### Before anything

The makefile have many commands to interact and control the pprogram and its container.
With this command you can see all the avaible commands.

````Makefile
make help
````

### Start
Build the image for docker. This is necessary only single time.

````Makefile
make build
````



### Run program

Then we can create, run and execute the necessary container running:

````Makefile
make
````

After this we are in the root directory of a debian container. To find  and run 
main program:

````bash
cd home
````

...

not finish