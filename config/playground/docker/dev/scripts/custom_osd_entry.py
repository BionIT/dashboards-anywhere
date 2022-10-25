#!/usr/bin/python

import os
import sys

def run():
    source_file="/opt/opensearch-dashboards/extra_config/osd.yml"
    target_file="/usr/share/opensearch-dashboards/config/opensearch_dashboards.yml"

    s_kv = {}
    nc = []
    with open(source_file, "r") as s:
        for r in s:
            kv = r.split(":")
            if len(kv) < 2 or r.strip().startswith("#"):
                nc += [r]
                continue
            s_kv[kv[0]] = kv

    nt = []
    with open(target_file, "r") as t:
        for r in t:
            kv = r.split(":")
            if len(kv) < 2 or r.strip().startswith("#"):
                nt += [r]
            elif kv[0] in nc:
                #override
                nt += nc[kv[0]]
            else:
                nt += [r]

    with open(target_file, "w") as f:
        f.write("\n".join(nt + nc))

    print "finished updating config file"

    for i in range(1, len(sys.argv)):
        os.system("/opt/opensearch-dashboards/scripts/install-plugin.sh " + sys.argv[i])

    os.system("./opensearch-dashboards-docker-entrypoint.sh opensearch-dashboards")

if __name__ == "__main__":
    run()