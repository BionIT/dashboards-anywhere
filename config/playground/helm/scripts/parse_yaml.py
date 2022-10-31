#! /usr/bin/python

import os

if __name__ == "__main__":
    print("hey")
    with open("config/playground/helm/dev/helm-opensearch-dashboards.yaml", "r") as f:
        for r in f:
            print(r)
    print(os.environ['SOME_OTHER'])