#!/bin/bash
set -e

echo "append config to yaml"
source_file="/opt/opensearch-dashboards/extra_config/osd_config.yaml"
target_file="/usr/share/opensearch-dashboards/config/opensearch_dashboards.yml"

cat $source_file >> $target_file
