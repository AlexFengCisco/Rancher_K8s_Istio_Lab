## Docker base image build

    mkdir alex_yocto_img

    #cp yocto build/tmp/deployment/images/qemux86_64/alex_layer.xxxxxxx.tar.bz2 ~/alex_yocto_img/alex_yocto_os.tar.bz2
    # yocto build ,refer to traing_B/yocto/yocto_lab logging file


    Dockerfile

    FROM scratch
    ADD alex_yocto_os.tar.bz2 ./
    CMD ["sh"]

### build docker base image
    sudo docker build --tag alex_yocto_base -f ./Dockerfile .


### upload to dockerhub

    docker login #alexfengcisco password

### make dockerhub repository alex_yocto_base

    docker tag alex_yocto_base:latest  alexfengcisco/alex_yocto_base:latest

    docker push alexfengcisco/alex_yocto_base:latest