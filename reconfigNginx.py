#!/usr/bin/python

import docker
import jinja2

c = docker.Client(base_url='unix://var/run/docker.sock',  version='1.9', timeout=10)
containers = c.containers()

mappings = {}

for cont in containers:
#	print cont['Id']
	
	container = c.inspect_container(cont['Id'])
	
	allEnv = {}
	
	for env in container["Config"]["Env"] :
		e = env.split("=")
		if len(e) > 1 :
			allEnv[e[0]] = e[1];
		
	if 'vhost' in allEnv :
		hostMapping = {}
		
		if allEnv["vhost"] in mappings :
			hostMapping = mappings[allEnv["vhost"]]
		else :
			hostMapping = []
			mappings[allEnv["vhost"]] = hostMapping
			
		ipAddress = container["NetworkSettings"]["IPAddress"];
		
		if "80/tcp" in container["Config"]["ExposedPorts"] :
			hostMapping.append({'ipaddress': ipAddress, 'internalPort':"80", id:id});
			
		if "8080/tcp" in container["Config"]["ExposedPorts"] :
			hostMapping.append({'ipaddress': ipAddress, 'internalPort':"8080", id:id});
			

# print mappings
templateLoader = jinja2.FileSystemLoader( searchpath="/" )
templateEnv = jinja2.Environment( loader=templateLoader )
TEMPLATE_FILE = "/home/ocom/docker/nginx/reverseProxy.conf.tmpl"
template = templateEnv.get_template( TEMPLATE_FILE )

#template = Template ("""HostName: {{hostname}} for {% for map in maps %} {{ map.ipaddress }}:{{ map.internalPort }}, {% endfor %}""");

for hostName in mappings :
	shortHostLabel = hostName.split(".")[0]
	nginxConf = template.render (hostname=hostName, maps= mappings[hostName], shortHostName=shortHostLabel)
	filename = "/home/ocom/docker/nginx/sites-available/" + shortHostLabel
	f = open (filename, 'w')
	f.write (nginxConf);
	f.close();
	print "File for " + shortHostLabel + " generated!"

print "Done!"
