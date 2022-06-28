# LogBasedDebianSecurity

Debian security based on log tracking

- Display of failed login attempts to ssh-ftp-http services from the web interface.

- Failed login records on local server.

- Determining the maximum number of requests and blocking them with blocking programs.

## Installation

- Tested on Ubuntu 20.04 LTS.

- UFW is used in the application.

  `sudo ufw enable`
  
  `sudo ufw allow 21`
  
  `sudo ufw allow 22`
  
  `sudo ufw allow 80`

- Installing necessary python modules: 

  `pip install -r requirements.txt`


## Usage
- The sudo password must be entered in the terminal where the applications will be run.

- Run this command. (python or python3) 

  `python manage.py runserver`

- You can use the application by entering the address http://127.0.0.1:8000/

- Use of blocking programs (python or python3):

  `python manage.py shell < protection/ssh.py`
  
  `python manage.py shell < protection/ftp.py`
  
  `python manage.py shell < protection/httplogin.py`
  
  `python manage.py shell < protection/httpfuzzing.py`
