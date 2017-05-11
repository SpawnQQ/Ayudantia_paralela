echo -e "Instalacion ssh, wakeonlan, mpi4py, python-pip y dependencias"
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install wakeonlan ssh nfs-kernel-server nfs-common build-essential python-mpi4py git  htop mpi libopenmpi-dev python-pip
echo -e "Instalamos con pip"
sudo pip install mpi4py
echo -e "Completada la instalacion de mpi..."