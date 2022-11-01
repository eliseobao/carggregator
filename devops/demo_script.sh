make down && make up/minimal && sleep 30

make crawl-motor.es items=30

python3 -m webbrowser http://localhost:3000

cd third-party/carggregator-web && make down && make up
