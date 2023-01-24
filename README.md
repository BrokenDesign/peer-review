Here's links for all of the things I'm asking you to install</br>
https://github.com/pyenv-win/pyenv-win</br>
https://python-poetry.org/</br>
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy

Note for the commands below you may have to update your execution policy. This can be done for each of the particular commands, or you can do it globally with: 

```
Set-ExecutionPolicy <policy> 
```
Possible values include: 
- `Restricted` — blocks any script from running.
- `RemoteSigned` — allows scripts created on the computer. However, scripts created on another device won’t run unless they have a trusted signature.
- `AllSigned` — allows all scripts to run. However, only if a trusted publisher has included a signature.
- `Unrestricted` — runs any script without restrictions.

## Install git CLI 

I personally have it set to unrestricted because I write scripts and I don't want to have to sign them all before I run them. It's less secure, probably either RemoteSigned or AllSigned is permissive enough. But if there's an error running any of the .ps1 files then it is likely related to this policy. 

## Install Pyenv
1. Install pyenv-win in PowerShell: 
```shell 
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```
2. Reopen PowerShell
3. Check that pyenv is installed and found on your pathy by running: 
```shell
pyenv --version
```
4. Install the shim for python 3.10 by running: 
```shell
pyenv install 3.10.0
```
5. Set this to be your default by running: 
```shell
pyenv global 3.10.0
```
6. Check which Python version you are using and its path by running: 
```shell
pyenv version
```
7. Check that python is working by running: 
```shell
 python -c "import sys; print(sys.executable)"
```

## Installing Poetry
This will update the packages installed within the python 3.10 instance that you installed per the earlier step, or within your existing instance if you did not follow that. 

1. Upgrade to the latest version of pip
```shell 
python -m pip install -U pip
```
2. Install Poetry: 
```shell 
pip install poetry
```


## Create Virtual Environment
Open PowerShell and navigate to he project that was cloned from Git. 
Run the command:
```shell
poetry install
```
This will create a virtual environment including all of the dependencies included in pyproject.toml 

## Running
Then you can either run it from source using the venv created in the last step, or you can build it and run it in another python instance. To build you would just run: 
```shell
poetry build
```

Which will generate the .whl in `./dists`
