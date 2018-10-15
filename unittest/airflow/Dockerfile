FROM ubuntu:16.04

ENV PATH "/root/miniconda3/bin/:$PATH"
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV PROJ_LIB /root/miniconda3/share/proj

# Install script dependance avaible on apt source
RUN /bin/bash -c "apt-get update && apt-get install -y --allow-unauthenticated \
                wget vim \
                zip bzip2 \
                gcc g++ gfortran \
                build-essential mysql-client locales localepurge axel pngquant && \
                /usr/share/locales/install-language-pack en_US.UTF-8 && \
                dpkg-reconfigure locales && \
                # install miniconda
                wget https://repo.continuum.io/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O /tmp/Miniconda3-latest-Linux-x86_64.sh && \
                rm -rf /root/miniconda3 && \
                bash /tmp/Miniconda3-latest-Linux-x86_64.sh  -b && \
                export PATH="/root/miniconda3/bin/:$PATH" && \
                rm  -rf /tmp/Miniconda3-latest-Linux-x86_64.sh && \
                # install package for meteorologist
                conda install -y -c conda-forge iris && \
                conda install -y -c conda-forge cdo && \
                conda install -y -c conda-forge nco && \
                conda install -y -c conda-forge wgrib2 && \
                conda install -y -c eumetsat wgrib && \
                conda install -y -c conda-forge gdal && \
                conda install -y pymysql sqlalchemy requests BeautifulSoup4 && \
                conda install -y -c conda-forge basemap && \
                pip install mkl-random==1.0.1 cf-units==2.0.1 && \
                cd /root/miniconda3/lib && \
                ln -s libncursesw.so.6.1 libncurses.so.6 && \
                ln -s libtinfo.so libtinfo.so.6 && \
                apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* " 

VOLUME /opt/
WORKDIR /opt/
