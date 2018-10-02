# pyqt5_bootstrap

## How-to install

### Ubuntu 18.04

~~~bash
sudo apt-get update
sudo apt-get install git -y
sudo apt-get install python3-venv -y
git clone https://gitlab.com/Nyafazz/pyqt5_bootstrap.git
cd pyqt5_bootstrap
python3 -m venv venv
source venv/bin/activate
pip --no-cache-dir install -r requirements.txt
chmod u+x ./helpers/generate_ui.sh
python3 ./run_dev.py
~~~

## Change app name

~~~shell
~/pyqt5_bootstrap$ find . -type f \  
    -exec sed -i 's/pyqt5_bootstrap/NEW_NAME/g' {} +  
~~~
~~~shell
~/pyqt5_bootstrap$ cd ../ 
~~~ 
~~~shell
~$ find . -depth -name '*pyqt5_bootstrap*' -execdir  \  
    bash -c 'mv "$0" "${0//pyqt5_bootstrap/NEW_NAME}"' {} \;  
~~~
~~~shell
~$ cd NEW_NAME  
~~~
~~~shell
~/NEW_NAME$ python3 ./run_dev.py  
~~~
