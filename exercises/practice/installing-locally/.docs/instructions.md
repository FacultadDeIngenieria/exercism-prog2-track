## Exercism's local installation

We don't want you to use the **online** editor available on exercism. The idea of this project is 
for you to be able to use your own IDE to solve the proposed exercises.

Please read sections:

- Installation (either Mac OS, Windows or Linux)
- Configuration (same for everyone)
- Usage (same for everyone)


### Mac OS installation

_For the installation, we will use **brew**. This is a very handy 
package manager for Mac OS. You can learn how to install it here: https://brew.sh/_


Open up your terminal and run the following commands:

- `brew update`

- `brew install exercism`

- `exercism version`

After this last command, you should see an output similar to this one:

`exercism version 3.0.13`

Seeing the version of the package as an output means that you 
now have the CLI (command line interface) version of exercism
installed. Congratulations.


### Windows installation

For the installation of the Windows CLI (commanad line interface), please follow
the following instructions:

https://github.com/exercism/windows-installer/releases/tag/v1.5.3

### Linux installation

Open up your terminal and run the following commands:

- `sudo snap install exercism`
- `exercism version`

After this last command, you should see an output similar to this one:

`exercism version 3.0.13`

Seeing the version of the package as an output means that you
now have the CLI (command line interface) version of exercism
installed. Congratulations.


## Exercism Local Configuration

Now that we have isntalled the CLI on our machines, we need to configure it.

We need to tell the CLI tool: 

- Who we are
- What exercism instance we are using

### Personal Token

In order for the CLI to know who we are, we need to provide our personal
access token to it. 

To retrieve the access token you need to access this link:

http://facultaddeingenieria.duckdns.org:3020/settings/api_cli

You should see a CLI token there. Save it

### Exercism Instance

As we told you, we are using a custum Exercism instance for this class.
That instance is hosted under the following URL: 

`http://facultaddeingenieria.duckdns.org:3020/settings/api_cli`

### Configuration

To configure Exercism, run the following command replacing the access token placeholder
with your access token

`exercism configure --token=YOUR_TOKEN_GOES_HERE -a http://facultaddeingenieria.duckdns.org:3020/api/v1`

After running that command you should see an output similar to:

`You have configured the Exercism command-line client:`

## Using the CLI

### Download

To download a new exercise, you will see a suggested command on the Exercism's web page.
You can copy that command and run it directly on your terminal.

For example, the download command for the hello world exercise is:

`exercism download --exercise=hello-world --track=python`

Running this command downloads the exercise for you, and tells you
were the exercise was downloaded. You can now solve that exercise using 
your IDE.

### Submit

Instead of copying and pasting the solution into the online editor, we will
submit it using the same CLI.

To submit an exercise you need to be inside the directory where the exercise
was downloaded and run the following command:


`exercism submit hello_world.py`

For other exercises, replace the `hello_world.py` reference to the reference
of the file where you solved the exercise.




