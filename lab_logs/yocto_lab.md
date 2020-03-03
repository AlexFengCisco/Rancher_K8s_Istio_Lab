
## Yocto Lab log

	reference link
	https://www.yoctoproject.org/docs/current/brief-yoctoprojectqs/brief-yoctoprojectqs.html

### prepare cent os 7 as build server

	$ sudo yum install -y epel-release
    $ sudo yum makecache
    $ sudo yum install gawk make wget tar bzip2 gzip python unzip perl patch \
     diffutils diffstat git cpp gcc gcc-c++ glibc-devel texinfo chrpath socat \
     perl-Data-Dumper perl-Text-ParseWords perl-Thread-Queue python34-pip xz \
     which SDL-devel xterm
    $ sudo pip3 install GitPython jinja2
    $ sudo yum install docbook-style-dsssl docbook-style-xsl \
     docbook-dtds docbook-utils fop libxslt dblatex xmlto

    # prepare prebuild buildtools

    wget http://downloads.yoctoproject.org/releases/yocto/yocto-3.0.1/buildtools/x86_64-buildtools-nativesdk-standalone-3.0.1.sh
    sh ./x86_64-buildtools-nativesdk-standalone-3.0.1.sh
    $ source /home/your_username/buildtools/environment-setup-i586-poky-linux


#### lab tips 

	1.can not with user root
	2.can not git clone git ,has to git clone https
	3.has to change locale to utf-8
	4.use ack/ack-grep to improve search efficency


#### set up locale to utf-8

	vi /etc/environment

	add these lines...

	LANG=en_US.utf-8
	LC_ALL=en_US.utf-8


#### git clone poky

	git clone https://git.yoctoproject.org/git/poky

#### set up yocto build enviroment

	source ./porky/oe-init-build-env

#### build a simple image ,quite a long time , almost 4~5 hours at least
	
	bitbake core-image-minimal

#### run image with qemu [nographic] menas has no GUI

	runqemu qemux86-64 nographic

	console login as root , no password
    
    Ctrl-A X to quit qemu console

    # or killall from another terminal 
    yum -y install  psmisc
    killall qemu-system-x86_64


#### create your own layer and add layers to bblayers.conf

    bitbake-layers create-layer meta-alexlayer01

    bitbake-layers add-layer meta-alexlayer01

    bitbake-layers -h # get bitbake-layers help

    # make images
    bitbake alexlayer01-image
    runqemu quemux86-64 ./alexlayer01-image.ext4 nographic



#### build with toaster web GUI
	
	pip3 install -r poky/bitbake/toaster-requirements.txt
	source toaster start webport=0.0.0.0:8000

	##sth wrong with SE Lab 58 network , can not git clone git:// ....  

#### make core-minimal image with python3
   
    #edit local.conf and add the followings

    IMAGE_INSTALL_append = " python3"
    IMAGE_INSTALL_append = " python3-pip"


####
419,392,512  gcc python3 pip3 core-minial ext4 size

#### convert img/ext4 to iso 

	wget http://ftp.tu-chemnitz.de/pub/linux/dag/redhat/el7/en/x86_64/rpmforge/RPMS/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm
	sudo rpm -Uvh rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm
	sudo yum install ccd2iso

#### bitbake build to iso format
    
    #edit build/conf/local.conf and add
    IMAGE_FSTYPES = "ext4 tar.bz2 iso"










