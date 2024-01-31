# 删除所有satellite-monitor的容器
docker rm -f `docker ps -a | grep satellite | awk '{print $1}'`
docker stop  `docker ps -a | grep ground | awk '{print $1}'`
# 删除所有satellite-monitor的容器
docker rm -f `docker ps -a | grep ground | awk '{print $1}'`
docker network rm `docker network ls | grep Network | awk '{print $1}'`