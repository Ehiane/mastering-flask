## Steps to configure this app

### Dev POV

### Initialize Virtual environment "env"
```
python -m venv env
```

### Activate the virtual environment
## Powershell
```
 `env\Scripts\Activate.ps1`
```
OR

## Command Prompt
```
env\Scripts\activate
```

OR

## Linux
```
source env/bin/activate
```

### To deactivate the virtual environment 

```
deactivate
```

### To check installations 
```
pip list
```

### Install dependencies
```
 pip install Flask Flask-Scss Flask-SQLAlchemy
```

### to generate the 'requiremnts.txt' file
```
pip freeze > requirements.txt
```