#!/bin/bash

sleep 30

status_code=$(curl --write-out %{http_code} --silent --output /dev/null -X PUT "localhost:9200/carggregator-index?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "analysis": {
      "char_filter": {
        "quote": {
          "type": "mapping",
          "mappings": [
            "« => \"",
            "» => \""
          ]
        }
      },
      "normalizer": {
        "my_normalizer": {
          "type": "custom",
          "char_filter": [
            "quote"
          ],
          "filter": [
            "asciifolding"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "brand": {
        "type": "text",
        "fields": {
          "raw": {
            "normalizer": "my_normalizer",
            "type": "keyword"
          }
        }
      },
      "color": {
        "type": "text",
        "fields": {
          "raw": {
            "normalizer": "my_normalizer",
            "type": "keyword"
          }
        }
      },
      "fuel": {
        "type": "text",
        "fields": {
          "raw": {
            "normalizer": "my_normalizer",
            "type": "keyword"
          }
        }
      },
      "hp": {
        "type": "long"
      },
      "image": {
        "type": "keyword"
      },
      "location": {
        "type": "text",
        "fields": {
          "raw": {
            "normalizer": "my_normalizer",
            "type": "keyword"
          }
        }
      },
      "model": {
        "type": "text",
        "fields": {
          "raw": {
            "normalizer": "my_normalizer",
            "type": "keyword"
          }
        }
      },
      "odometer": {
        "type": "long"
      },
      "price_cash": {
        "type": "long"
      },
      "price_financed": {
        "type": "long"
      },
      "publisher": {
        "type": "text",
        "fields": {
          "raw": {
            "normalizer": "my_normalizer",
            "type": "keyword"
          }
        }
      },
      "registration_date": {
        "type": "long"
      },
      "title": {
        "type": "text",
        "fields": {
          "raw": {
            "normalizer": "my_normalizer",
            "type": "keyword"
          }
        }
      },
      "transmission": {
        "type": "text",
        "fields": {
          "raw": {
            "normalizer": "my_normalizer",
            "type": "keyword"
          }
        }
      },
      "url": {
        "type": "keyword"
      }
    }
  }
}
')

if [[ "$status_code" -ne 200 ]] ; then
  echo "Reusing existing index."
else
  echo "New index created."
fi
