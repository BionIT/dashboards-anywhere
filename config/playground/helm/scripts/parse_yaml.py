#! /usr/bin/python

import os

if __name__ == "__main__":
    print("hey")
    with open("config/playground/helm/dev/helm-opensearch-dashboards.yaml", "r") as f:
        for r in f:
            if "G-0SHJ0Q9ZBY" in r:
                print("yes have it")
            print(r)
    print(os.environ['SOME_OTHER'])