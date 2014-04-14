all:

install:
	install -m 0644 pakiti2.py /usr/lib/yum-plugins/
	install -m 0644 pakiti2.conf /etc/yum/pluginconf.d/

.PHONY: all install
