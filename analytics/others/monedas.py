"""
(base) xuwira30@026P235C:~$ ssh turing
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-94-generic x86_64)
(base) xuwira30@turing:~$ ssh turing
The authenticity of host 'turing (10.52.178.250)' can't be established.
(base) xuwira30@turing:~$ ls
DATASETS  miniconda3  README  start.jupyter.server.sh  works
(base) xuwira30@turing:~$ cd DATASETS
(base) xuwira30@turing:~/DATASETS$ cd D
Data/ Docs/
(base) xuwira30@turing:~/DATASETS$ cd Data/
(base) xuwira30@turing:~/DATASETS/Data$ cd cvat/
(base) xuwira30@turing:~/DATASETS/Data/cvat$ cd Coins/
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ pwd
/home/alumnado/xuwira30/DATASETS/Data/cvat/Coins
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ ll
total 48K
drwxr-xr-x 1 pcjf docentes   98 feb 20 16:26 data/
drwxr-xr-x 1 pcjf docentes  624 feb 20 16:19 runs/
drwxr-xr-x 1 pcjf docentes  110 feb 20 16:26 src/
drwx------ 1 pcjf docentes  142 feb 20 16:26 tmp/
lrwxrwxrwx 1 pcjf docentes   19 feb 16 17:44 activate -> .coins/bin/activate
-rw-r--r-- 1 pcjf docentes  35K feb 20 13:26 LICENSE
-rw-r--r-- 1 pcjf docentes  390 feb 20 16:26 README.md
-rw-r--r-- 1 pcjf docentes 1,1K feb 20 16:26 requirements.txt
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ cd data/
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins/data$ tree -d
.
└── obj_Train_data
    └── Coins
        └── data

(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ cd tmp
-bash: cd: tmp: Permission denied
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ cd ..
(base) xuwira30@turing:~/DATASETS/Data/cvat$ cd src
-bash: cd: src: No such file or directory
(base) xuwira30@turing:~/DATASETS/Data/cvat$ cd Coins/
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ cd src/
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins/src$ ls
best.pt  log.txt  preprocess.py  train.py  yolov8n.pt  yolov8x.pt
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins/src$ joe preprocess.py
"""

# joe preprocess.py

"""

Windows PowerShell
Copyright (C) Microsoft Corporation. Todos los derechos reservados.

Instale la versión más reciente de PowerShell para obtener nuevas características y mejoras. https://aka.ms/PSWindows

PS C:\Users\maria.teresa.llamasg> wsl
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.15.133.1-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

This message is shown once a day. To disable it please create the
/home/xuwira30/.hushlogin file.
(base) xuwira30@026P235C:/mnt/c/Users/maria.teresa.llamasg$ cd
(base) xuwira30@026P235C:~$ ssh turing
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-94-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

  System information as of mar 20 feb 2024 20:33:42 CET

  System load:                      1.2353515625
  Usage of /home:                   5.1% of 43.49TB
  Memory usage:                     12%
  Swap usage:                       0%
  Temperature:                      39.0 C
  Processes:                        1014
  Users logged in:                  8
  IPv4 address for bond0:           10.52.178.250
  IPv4 address for bond1:           192.168.0.2
  IPv4 address for br-4ea7c9bab50c: 172.20.0.1
  IPv4 address for br-bdc0e596e171: 172.18.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for tun0:            192.168.255.1

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

El mantenimiento de seguridad expandido para Applications está activado.

Se pueden aplicar 9 actualizaciones de forma inmediata.
1 de estas actualizaciones es una actualización de seguridad ESM Apps.
Para ver estas actualizaciones adicionales, ejecute: apt list --upgradable


Last login: Fri Feb 16 17:00:25 2024 from 10.52.178.235
HISTFILE2000: command not found
(base) xuwira30@turing:~$ ssh turing
The authenticity of host 'turing (10.52.178.250)' can't be established.
ED25519 key fingerprint is SHA256:ssmGTiZqw9BrBQOp6EcNU4sD7Pw4j7srnJ4kHbvdR24.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'turing' (ED25519) to the list of known hosts.
xuwira30@turing's password:
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-94-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

  System information as of mar 20 feb 2024 20:34:45 CET

  System load:                      1.1787109375
  Usage of /home:                   5.1% of 43.49TB
  Memory usage:                     12%
  Swap usage:                       0%
  Temperature:                      37.0 C
  Processes:                        1056
  Users logged in:                  12
  IPv4 address for bond0:           10.52.178.250
  IPv4 address for bond1:           192.168.0.2
  IPv4 address for br-4ea7c9bab50c: 172.20.0.1
  IPv4 address for br-bdc0e596e171: 172.18.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for tun0:            192.168.255.1

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

El mantenimiento de seguridad expandido para Applications está activado.

Se pueden aplicar 9 actualizaciones de forma inmediata.
1 de estas actualizaciones es una actualización de seguridad ESM Apps.
Para ver estas actualizaciones adicionales, ejecute: apt list --upgradable


Last login: Tue Feb 20 20:34:41 2024 from 10.52.178.235
HISTFILE2000: command not found
(base) xuwira30@turing:~$ ls
DATASETS  miniconda3  README  start.jupyter.server.sh  works
(base) xuwira30@turing:~$ cs DATASETS
Command 'cs' not found, but can be installed with:
apt install csound
Please ask your administrator.
(base) xuwira30@turing:~$ ls
DATASETS  miniconda3  README  start.jupyter.server.sh  works
(base) xuwira30@turing:~$ cd DATASETS
(base) xuwira30@turing:~/DATASETS$ cd D
Data/ Docs/
(base) xuwira30@turing:~/DATASETS$ cd Data/
(base) xuwira30@turing:~/DATASETS/Data$ cd cvat/
(base) xuwira30@turing:~/DATASETS/Data/cvat$ cd Coins/
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ pwd
/home/alumnado/xuwira30/DATASETS/Data/cvat/Coins
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ ll
total 48K
drwxr-xr-x 1 pcjf docentes   98 feb 20 16:26 data/
drwxr-xr-x 1 pcjf docentes  624 feb 20 16:19 runs/
drwxr-xr-x 1 pcjf docentes  110 feb 20 16:26 src/
drwx------ 1 pcjf docentes  142 feb 20 16:26 tmp/
lrwxrwxrwx 1 pcjf docentes   19 feb 16 17:44 activate -> .coins/bin/activate
-rw-r--r-- 1 pcjf docentes  35K feb 20 13:26 LICENSE
-rw-r--r-- 1 pcjf docentes  390 feb 20 16:26 README.md
-rw-r--r-- 1 pcjf docentes 1,1K feb 20 16:26 requirements.txt
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ cd data/
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins/data$ tree -d
.
└── obj_Train_data
    └── Coins
        └── data

3 directories
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins/data$ cd ..
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ cd tmp/
-bash: cd: tmp/: Permission denied
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ cd tmp
-bash: cd: tmp: Permission denied
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ cd ..
(base) xuwira30@turing:~/DATASETS/Data/cvat$ cd src
-bash: cd: src: No such file or directory
(base) xuwira30@turing:~/DATASETS/Data/cvat$ cd Coins/
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins$ cd src/
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins/src$ ls
best.pt  log.txt  preprocess.py  train.py  yolov8n.pt  yolov8x.pt
(base) xuwira30@turing:~/DATASETS/Data/cvat/Coins/src$ joe preprocess.py

    I A  preprocess.py (python)(Read only)                                                             Row 186  Col 1
    else:
       return filename;

################################################################################
if __name__ == "__main__":

   source = Path(ORIGIN);
   txt_list = list(source.glob("*.txt"));
   img_list = [];

   txt_list=[fn for fn in txt_list if os.path.getsize(fn)>0];

   for txt_filename in txt_list:
       base, ext = os.path.splitext(txt_filename);
       assert ext==".txt";
       if os.path.isfile(f"{base}.png"): img_filename=f"{base}.png";
       else:                             img_filename=img2png(f"{base}.jpg");
       assert os.path.isfile(img_filename);
       img_list.append(img_filename);
       assert img_list.index(img_filename)==txt_list.index(txt_filename);

   trainset, testset = split_and_rotate(source=(txt_list,img_list), origin=ORIGIN, target=TARGET);

   with open(os.path.join(TARGET,"trainset.json"),"wt") as fd:
        json.dump(trainset, fp=fd);

   with open(os.path.join(TARGET,"testset.json"),"wt") as fd:
        json.dump(testset, fp=fd);

"""