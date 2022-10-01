# Carggregator


## _Your second-hand car easier than ever_


Carggregator is a second-hand car ads aggregator.


## Tech

Carggregator uses a number of open source projects to work properly:

- [Scrapy] - A fast high-level web crawling and web scraping framework.
- [Elasticsearch] - Distributed, RESTful search and analytics engine at the heart of the Elastic Stack.

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
git flow feature start <FEATURE>
```

Finish a feature:

```sh
git flow feature finish <FEATURE>
```

### Docker

Build the development image:

```sh
make dev/build
```

Connect to the development image:

```sh
make dev/shell
```


## License

GNU General Public License v3.0


**Free Software, Hell Yeah!**




[carggregator]: <https://github.com/eliseobao/carggregator>
[git-repo-url]: <https://github.com/eliseobao/carggregator.git>
[Scrapy]: <https://github.com/scrapy/scrapy>
[Elasticsearch]: <https://github.com/elastic/elasticsearch>
