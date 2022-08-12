# ft_otp / TOTP Generator

Python implementation of a two factor authentication program.

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

Put a password for generate a token to encript master key, and now we can create a temporary one time password. 

## Generate temporary password

With `-v` flag you turn on verbose mode, where shows generated password and the original tool "oathtool" that the password must match.

````bash
./totp_gen.py -k -v modules/key/ft_otp.key
````
