1  apt install sendmail
2  apt-get install software-properties-common
3  add-apt-repository universe
4  apt install certbot
5  certbot certonly --standalone
6  certbot renew --dry-run
7  sh -c 'printf "#!/bin/sh\n/opt/lra/bin/supervisorctl  stop nginx\n" > /etc/letsencrypt/renewal-hooks/pre/nginx.sh'
8  sh -c 'printf "#!/bin/sh\n/opt/lra/bin/supervisorctl  start nginx\n" > /etc/letsencrypt/renewal-hooks/post/nginx.sh'
9  aduser www
10  adduser www
11  cd opt
12  ls -la
13  cd /opt/
14  ls
15  mkdir buildout-cache
16  cd buildout-cache/
17  mkdir eggs
18  mkdir downloads
19  mkdir extends
20  cd ..
21  ls
22  chown -R www:www buildout-cache/
23  exit
24  cd /etc/letsencrypt/
25  ls
26  cd renewal-hooks/
27  ls
28  cd pre/
29  ls
30  chmod 755 nginx.sh
31  cd ..
32  cd post/
33  chmod 755 nginx.sh
34  cd ..
35  exit
36  apt update
37  apt install python3-venv python3-pip libpython3-dev python3-docutils python3-sphinx
38  apt install libz-dev libjpeg-dev libssl-dev libxml2-dev libreadline-dev wv libxslt1-dev libffi-dev
39  apt install git rsync certbot poppler-utils vim screen build-essential libpcre3-dev mlocates