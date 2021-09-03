IMAGE=katerynatkachenko/selenium-perseus:latest

if [ $# -eq 0 ]; then
  docker run -d --rm --name selenium-debug -p 4444:4444 -v /home/artgoe/Projects/Selenium/pylenium:/app -w /app -p 5900:5900 --shm-size=2g $IMAGE
fi;

function docker-exec() {
  docker exec -it selenium-debug bash
}

function build-image(){
    docker build -t katerynatkachenko/selenium-perseus:latest .
}

function push-image(){
 docker image push katerynatkachenko/selenium-perseus:latest
}

case "$1" in
    e) docker-exec ;;
    b) build-image ;;
    p) push-image ;;
    *) echo 'fallback' ;;
esac
