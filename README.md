# carggregator

<p align="center">
    <a href="https://github.com/eliseobao/carggregator/" alt="carggregator">
        <img src="https://github.com/eliseobao/carggregator/blob/develop/images/corporate/carggregator_logo_1.svg" />
    </a>
</p>


<p align="center">
    <a href="https://github.com/eliseobao/carggregator/blob/develop/LICENSE" alt="License">
        <img src="https://img.shields.io/github/license/eliseobao/carggregator" />
    </a>
    <a href="https://github.com/eliseobao/carggregator/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/github/contributors/eliseobao/carggregator" />
    </a>
    <a href="https://github.com/eliseobao/carggregator/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/eliseobao/carggregator" />
    </a>
    <a href="#stars" alt="Stars">
        <img src="https://img.shields.io/github/stars/eliseobao/carggregator" />
    </a>
</p>


This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png

## _Your second-hand car easier than ever_


Carggregator is a second-hand car ads aggregator.


## Tech

Carggregator uses a number of open source projects to work properly:

- [Black] - An uncompromising Python code formatter.
- [Scrappy] - A fast high-level web crawling and web scraping framework.
- [user_agent] - A module for generating random, valid web user agents.
- [Elasticsearch] - Distributed, RESTful search and analytics engine at the heart of the Elastic Stack.
- [dejavu] - The Missing Web UI for Elasticsearch: Import, browse and edit data with rich filters and query views, create search UIs visually.
- [ScrapyElasticSearch] - An Scrapy pipeline which allows you to store scrapy items in Elasticsearch.

And of course Carggregator itself is open source with a [public repository][carggregator] on GitHub.


## Development

Want to contribute? Great!


### Git-Flow

Carggregator uses git-flow to structure its repository! Open your favorite Terminal and run these commands.

Initialize git-flow:
```sh
bash .bin/git_gitflow.sh init
```

Start a new feature:
```sh
git flow feature start Issue-X
```

Finish a feature:
```sh
git flow feature finish Issue-X
```

### Docker

Build the development image:
```sh
make build
```

Connect to the development image:
```sh
make shell
```

Format source code:
```sh
make black
```


## Usage

### Docker

Deploy Elasticsearch and dejavu services:
```sh
make up
```

Deploy only Elasticsearch service:
```sh
make up/minimal
```

Stop deployed services:
```sh
make down
```

Crawl and index ~_n_ items from [motor.es](https://www.motor.es/coches-segunda-mano/).
If not specified, all the webspace:
```sh
make crawl-motor.es [items=n]
```

Crawl and index ~_n_ items from [autoscout24](https://www.autoscout24.es/lst?sort=standard&desc=0&ustate=N,U&atype=C&cy=E).
If `items` not specified, all the webspace:
```sh
make crawl-autoscout24 [items=n]
```

Crawl and index ~_n_ items from [autocasion](https://www.autocasion.com/coches-ocasion).
If `items` not specified, all the webspace:
```sh
make crawl-autocasion [items=n]
```

Crawl and index ~_n_ items from [motor.es](https://www.motor.es/coches-segunda-mano/),
[autoscout24](https://www.autoscout24.es/lst?sort=standard&desc=0&ustate=N,U&atype=C&cy=E) and
[autocasion](https://www.autocasion.com/coches-ocasion). If `items` not specified, all the webspace:
```sh
make crawl-all [items=n]
```
## License

GNU General Public License v3.0


**Free Software, Hell Yeah!**




[carggregator]: <https://github.com/eliseobao/carggregator>
[git-repo-url]: <https://github.com/eliseobao/carggregator.git>

[Black]: <https://github.com/psf/black>
[Scrappy]: <https://github.com/scrapy/scrapy>
[user_agent]: <https://github.com/lorien/user_agent>
[Elasticsearch]: <https://github.com/elastic/elasticsearch>
[dejavu]: <https://github.com/appbaseio/dejavu>
[ScrapyElasticSearch]: <https://github.com/jayzeng/scrapy-elasticsearch>
