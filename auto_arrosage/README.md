

## Wiring

## Crontab

Mettre ```arrosage.py``` & ```reset-reboot.py``` dans le dossier commun /home/*<nom d'utilisateur>*

```sudo crontab -e``` 

    @reboot python3 /home/<nom d'utilisateur>/reset_pin.py
    00 14 * * 1,3,5 python3 /home/<nom d'utilisateur>/arrosage.py

