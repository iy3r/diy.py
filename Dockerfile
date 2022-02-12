FROM python:3.10.2-bullseye

LABEL maintainer="Vashistha Iyer <iy3rvashistha@gmail.com>" \
      description="Python data lab"

WORKDIR /lab

ENV PYTHONPATH="$PYTHONPATH:/lab"

ENV SHELL="/bin/bash"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN ipython profile create && \ 
    sed -i 's/# c.InteractiveShellApp.extensions = \[\]/c.InteractiveShellApp.extensions = ["autoreload"]/g' /root/.ipython/profile_default/ipython_config.py && \
    sed -i 's/# c.InteractiveShellApp.exec_lines = \[\]/c.InteractiveShellApp.exec_lines = ["%autoreload 2"]/g' /root/.ipython/profile_default/ipython_config.py

EXPOSE 8888

CMD jupyter lab --ip="*" --port=8888 --no-browser --allow-root --NotebookApp.token="" --NotebookApp.password=""