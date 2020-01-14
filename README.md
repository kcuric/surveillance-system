# DIY Surveillance System 👁️
DIY surveillance system. Made as a team project for Information Systems Security course at the Faculty of Organization and Informatics, Varaždin, Croatia.

## 📕 Description
🇬🇧 ENG:
"Do it yourself" surveillance system with face detection implemented with Python and mostly OpenCV was a team project for a "Information Systems Security" course at the Faculty of Organization. In short, the client script rapidly records images and sends them via the UDP to the server. The server scripts receives the images, detects the faces inside them using OpenCV and notifies the user with an email if any faces were detected in the images. Camera stream can be observed in real time inside a simple Flask web app. There is still a lot room for improvement, because the development so far was a sort of "proof of concept" so some of the code wasn't quite written with PIP-8 in mind etc.. Development is still taking place, on the weekends of course - so this will get better as time goes by (hopefully)!

🇭🇷 CRO:
"Učini sam" nadzorni sustav s detekcijom lica implementiran pomoću programskog jezika Python i u velikoj većini uz pomoć OpenCV-a bio je timski projekt za kolegij "Sigurnost informacijskih sustava" na Fakultetu organizacije i informatike u Varaždinu. Ukratko, klijentska skripta učestalo snima fotografije te iste šalje UDP protokolom do servera. Serverska skripta detektira lica u zaprimljenim fotografijama pomoću OpenCV-a te obavještava korisnika elektroničkom poštom ukoliko detektira lice/a u nekoj od zaprimljenih fotografija. Fotografije pristižu zaista učestalo te se dobiva dojam strujanja videa koji se može gledati u pravome vremenu pomoću jednostavne Flaskom pogonjene web aplikacije. Postoji još poprilično mnogo mjesta za poboljšanja s obzirom da je cijeli projekt bio izrađen samo kao "dokaz konceptom", dijelovi koda tako nisu pisani u skladu s PIP-8 standardom i sl.. Razvoj je još u tijeku i to isključivo vikendima - tako da će sam projekt postati bolji s vremenom! (nadamo se)!

## How to run this? 🏁
### Dependencies
Install all the dependencies with pipenv. A list of dependencies can be found inside the _Pipfile_.
```
pipenv install
pipenv shell
```

### Server
```
python -m flask run --host=0.0.0.0
```

### Client
```
python app.py port --cam cam_num
ex. python app.py 5005 --cam 0
```
Currently only available ports (hardcoded in the server script) for UDP are: 5005, 5006. Of course you can change this in the code. To check available connected camera devices with Linux use:
```
v4l2-ctl --list-devices
```

## Contributors 👥
- Maja Benkus
- Krešimir Ćurić
- Igor Košmerl
- Miro Krištofić

A huge thanks to our mentors  Doc. dr. sc. Petra Grd and Doc. dr. sc. Igor Tomičić and the FOI Centre for forensics, biometry and privacy, for all the guidelines, equipment, etc..
