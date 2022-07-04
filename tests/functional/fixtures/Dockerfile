ARG GITLAB_IMAGE=get_this_from_env
ARG GITLAB_TAG=get_this_from_env
FROM ${GITLAB_IMAGE}:${GITLAB_TAG}

COPY create_license.rb /
RUN ruby /create_license.rb

CMD ["/assets/wrapper"]
