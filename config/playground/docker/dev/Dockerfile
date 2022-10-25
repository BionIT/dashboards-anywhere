FROM opensearchproject/opensearch-dashboards:latest

COPY . /opt/opensearch-dashboards/

#CMD ["/bin/bash", "-c", "/opt/opensearch-dashboards/scripts/install-plugins.sh https://github.com/BionIT/google-analytics-plugin/releases/download/2.3.0/googleAnalytics-2.3.0.zip;/opt/opensearch-dashboards/scripts/update-config.sh;./opensearch-dashboards-docker-entrypoint.sh opensearch-dashboards"]

#CMD ["python", "/opt/opensearch-dashboards/scripts/custom_osd_entry.py https://github.com/BionIT/google-analytics-plugin/releases/download/2.3.0/googleAnalytics-2.3.0.zip"]