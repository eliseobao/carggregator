# Carggregator

<p align="center">
  <img src="https://github.com/eliseobao/carggregator/blob/develop/images/carggregator_logo.svg" alt="Sublime's custom image"/>
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
    <a href="#forks" alt="Forks">
        <img src=https://img.shields.io/github/forks/eliseobao/carggregator" />
    </a>
</p>


This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg


## _Your second-hand car easier than ever_


Carggregator is a second-hand car ads aggregator.


## Tech

Carggregator uses a number of open source projects to work properly:

- [Scrappy] - A fast high-level web crawling and web scraping framework.
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
[Scrappy]: <https://github.com/scrapy/scrapy>
[Elasticsearch]: <https://github.com/elastic/elasticsearch>
