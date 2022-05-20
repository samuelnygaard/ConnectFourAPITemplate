
#!/bin/bash

echo "This script may possibly need to restart the system."
echo "Please rerun this script after a potential restart to finish deployment."

EMILY_DIST_DIRNAME=linux
CONFIGURATION_DIR=./configurations/dev
RUNTIME=$(grep -oP '(?<=RUNTIME=).*' "$CONFIGURATION_DIR/.env")

if [ ! -f "./$EMILY_DIST_DIRNAME.zip" ]; then

  sudo apt-get install curl
  sudo apt-get install unzip

  curl -L https://github.com/amboltio/emily-cli/releases/download/Release-v3.0.2/$EMILY_DIST_DIRNAME.zip -O
  unzip $EMILY_DIST_DIRNAME.zip

  if [ "$RUNTIME" = "nvidia" ]; then
    ./$EMILY_DIST_DIRNAME/emily doctor --no-update --silent --fix docker docker-compose nvidia-docker nvidia-driver
  else
    ./$EMILY_DIST_DIRNAME/emily doctor --no-update --silent --fix docker docker-compose
  fi

fi

rm -f $EMILY_DIST_DIRNAME.zip
rm -rf $EMILY_DIST_DIRNAME

sudo touch "./emily.log"
sudo chmod 666 "./emily.log"


sudo docker-compose --project-directory $CONFIGURATION_DIR -f "./configurations/dev/docker-compose.emily.yml" -f "./configurations/dev/docker-compose.mounts.yml" build
sudo docker-compose --project-directory $CONFIGURATION_DIR -f "./configurations/dev/docker-compose.emily.yml" -f "./configurations/dev/docker-compose.mounts.yml" down

if [ -f "$CONFIGURATION_DIR/nginx/.docker-compose.certbot.yml" ]; then
  echo "Emily: Verifying and updating SSL certificates..."
  sudo docker-compose --project-directory $CONFIGURATION_DIR -f $CONFIGURATION_DIR/nginx/.docker-compose.certbot.yml up
  sudo docker-compose --project-directory $CONFIGURATION_DIR -f $CONFIGURATION_DIR/nginx/.docker-compose.certbot.yml down
fi

sudo docker-compose --project-directory $CONFIGURATION_DIR -f "./configurations/dev/docker-compose.emily.yml" -f "./configurations/dev/docker-compose.mounts.yml" up -d
