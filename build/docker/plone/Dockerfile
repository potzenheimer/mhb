FROM plone:latest

COPY site.cfg /plone/instance/
RUN gosu plone buildout -c site.cfg